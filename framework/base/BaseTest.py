import os.path

class BaseTestCase(object):

    def prepare_screenshots_dir(self):
        class_dir = os.path.join(os.path.join(self.config['sframe']['output'], self.__class__.__name__))
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
        method_dir = os.environ["SCREENSHOTS_DIR"] = os.path.join(class_dir, self.current_method)
        if not os.path.exists(method_dir):
            os.makedirs(method_dir)

        return method_dir 