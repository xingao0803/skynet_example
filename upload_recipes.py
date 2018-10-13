import os

for lib in ["A", "B", "C", "D", "F", "G"]:
    os.system('cd recipes/%s && conan create . "LIB_%s/1.0@jfrog/stable" && conan upload "LIB_%s/*@jfrog/stable" -r demo-arti -c ' % (lib, lib, lib))
