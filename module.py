import os
import subprocess
import re


def init():
    # if MODULEPATH is not defined
    if not "MODULEPATH" in os.environ:
        with open(os.environ["MODULESHOME"] + "/init/.modulespath", "r") as fin:
            paths = []
            for line in fin.readlines():
                # skip comments
                if line.startswith("#"):
                    continue
                # remove comments at the end of each line
                match = re.search(r"^(.*?)[\t\n]", line)
                if not match:
                    continue
                # skip empty lines
                if not match.group(1):
                    continue
                paths.append(match.group(1))

    # if LOADEDMODULES is not defined
    if not "LOADEDMODULES" in os.environ:
        os.environ["LOADEDMODULES"] = ""


def add(module_name):

    (output, error) = subprocess.Popen(
        ["/usr/bin/modulecmd", "python", "add", module_name], stdout=subprocess.PIPE
    ).communicate()

    exec(output)

