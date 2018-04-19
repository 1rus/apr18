from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os.path
import sys
from selenium.webdriver import FirefoxProfile
from browsermobproxy import Client
from framework.framedriver import FrameWebdriver
from framework.exceptions import ProfileNotFound
from selenium.webdriver.chrome.options import Options


cap_map = {
    "firefox": DesiredCapabilities.FIREFOX.copy(),
    "internet explorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "internetexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "ie": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "chrome": DesiredCapabilities.CHROME.copy(),
    "opera": DesiredCapabilities.OPERA.copy(),
    "phantomjs": DesiredCapabilities.PHANTOMJS.copy(),
    "htmlunitjs": DesiredCapabilities.HTMLUNITWITHJS.copy(),
    "htmlunit": DesiredCapabilities.HTMLUNIT.copy(),
    "iphone": DesiredCapabilities.IPHONE.copy(),
    "ipad": DesiredCapabilities.IPAD.copy(),
    "android": DesiredCapabilities.ANDROID.copy(),
    "edge": DesiredCapabilities.EDGE.copy(),
    "safari": DesiredCapabilities.SAFARI.copy()
}

os_map = {
    "Windows": "WINDOWS",
    "Windows 2000": "XP",
    "Windows 2003": "XP",
    "Windows XP": "XP",
    "Windows Vista": "VISTA",
    "Windows 2008": "VISTA",
    "Windows 7": "VISTA",
    "Windows 8": " WIN8",
    "Windows 8.1": "WIN8_1",
    "Windows 10": "WIN10",
    "Mac": "MAC",
    "Android": "ANDROID",
}

class Browser(object):

    def __init__(self, br_conf, all_conf):
        self.browser_config = br_conf
        self.c = all_conf
        profile = None
        caps = cap_map[br_conf["type"]]

        if br_conf["type"] == "firefox":
            s = sys.platform
            if s in br_conf["profiles"].keys() and br_conf["profiles"][s]:
                profile_path=os.path.join(self.c["sframe"]["base"],"support","profiles",br_conf["profiles"][s])
            elif br_conf["profiles"]["profile"]:
                profile_path=os.path.join(self.c["sframe"]["base"],"support","profiles",br_conf["profiles"]["profile"])
            else:
                profile_path = None

            if profile_path:
                if os.path.isdir(profile_path):
                    profile = FirefoxProfile(profile_path)
                else:
                    raise ProfileNotFound("Profile not found at %s" % profile_path)

        if "on_error" in all_conf["sframe"]["screenshots"]:
            if not all_conf["sframe"]["screenshots"]["on_error"]:
                caps["webdriver.remote.quietExceptions"] = True

        if "headless" in br_conf["profiles"].keys() and br_conf["profiles"]["headless"]:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            caps = chrome_options.to_capabilities()
            print("added headless to chrome")

        if "type" in all_conf["selenium"]["proxy"]\
                and all_conf["selenium"]["proxy"]["type"] == "browsermob":
            self.proxy = Client(all_conf["selenium"]["proxy"]["url"])
            self.proxy.add_to_capabilities(caps)

        if "grid" in all_conf["selenium"]["executor"]\
                and all_conf["selenium"]["executor"]["is grid"]:
            if br_conf["grid filters"]["platform"]:
                caps["platform"] = br_conf["grid filters"]["platform"].upper()
            if br_conf["grid filters"]["version"]:
                caps["version"] = str(br_conf["grid filters"]["version"])

        com_exe = "http://%s:%s/wd/hub" % (self.c["selenium"]["executor"]["host"], self.c["selenium"]["executor"]["port"])

        self.driver = FrameWebdriver(desired_capabilities=caps,command_executor=com_exe,browser_profile=profile)
