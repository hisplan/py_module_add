import os
import module

if __name__ == "__main__":

    module.init()
    module.add("samtools")

    os.system("samtools --version")
