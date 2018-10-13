import time
from conans import ConanFile

class FConan(ConanFile):
    name = "LIB_F"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/xingao0803/skynet_example"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("LIB_B/1.0@%s/%s" % (self.user, self.channel))

    def build(self):
        self.output.warn("Building library...")
        time.sleep(2)
