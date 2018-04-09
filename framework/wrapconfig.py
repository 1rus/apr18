import os
import os.path
import sys
import yaml
import time
import logging.config


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
            cls._instance._data = {}
        return cls._instance

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __contains__(self, item):
        if item in self._data:
            return True
        return False

    def prepare(self, conf_file="sframe.yaml"):
        cwd = os.path.join(os.getcwd())
        if not os.path.exists(os.path.join(cwd, "conf")):
            cwd = os.path.dirname(os.path.join(os.getcwd()))
        config_dir = os.path.join(cwd, "conf")
        if not os.path.exists(os.path.join(config_dir, conf_file)):
            print("Config file %s does not exist" % os.path.join("conf", conf_file))
            sys.exit()
        for root, dirs, files in os.walk(config_dir):
            for f in files:
                if f.endswith(".yaml") and not f.startswith("log"):
                    file_path = os.path.join(root, f)
                    section_name = f[:-5]
                    with open(file_path, "r") as o:
                        if section_name in self._data.keys():
                            self._data[section_name].update(yaml.load(o).items())
                        else:
                            self._data[section_name] = yaml.load(o)
                    o.close()
        if "OUTPUT_DIR" not in os.environ.keys():
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
            log_dir = os.path.join(cwd, "output", timestamp, "logs")
            os.makedirs(log_dir)
        else:
            log_dir = os.path.join(os.environ["OUTPUT_DIR"], "logs")
            timestamp = str(os.environ["OUTPUT_DIR"])[-19:]
        self._data["sframe"]["output"] = os.environ["OUTPUT_DIR"] = os.path.join(cwd, "output", timestamp)
        self._data["sframe"]["base"] = cwd
        lfc = os.path.join(config_dir, "logger.yaml")
        if os.path.exists(lfc):
            with open(lfc, "r") as o:
                logger = yaml.safe_load(o.read())
                if "handlers" in logger.keys():
                    for head in logger["handlers"]:
                        for item in logger["handlers"][head]:
                            if item == "filename":
                                logger["handlers"][head][item] = os.path.join(log_dir, logger["handlers"][head][item])
            logging.config.dictConfig(logger)
        else:
            log_file_name = os.path.join(log_dir, "%s.xml" % timestamp)
            logging.basicConfig(filename=log_file_name, level=logging.INFO)
        return self._data
