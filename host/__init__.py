#    Copyright 2021 KeinShin
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import logging
import os
import platform
import socket
import sys

logger = logging.getLogger("VISION")


class Python:
    @staticmethod
    def install(host):
        print("Installing python 3.9 in your machine")
        print(host)
        if host.lower() == "linux":
            os.system("bash host/linux/python.sh")
        else:
            os.system(f"Powershell.exe -File {os.getcwd()}\\host\\windows\\python.ps1")


class Machine(Python):
    def __init__(self, **args) -> None:
        pass

    def host(self):

        return self.gethost()

    def machine(self):
        return sys.platform

    def validate(self):
        version = self.version()

        host = self.host()
        if version <= 3.8:

            logger.info("Vision Only Works With python version 3.8 or later")
            if host.lower() in ("heroku", "railway"):
                logger.info("Python 3.8 or later not found.Installing Python3.9")
                return self.install("linux")
            else:

                while True:
                    a = input(
                        "Do you want to install? python3.8 or later (q to exit):  ",
                    )
                    if a.lower() != "q":
                        break
                    print("\nProcces Killed")
                    raise KeyboardInterrupt
                host = platform.system()
                print("Installing Python.....")
                if host.lower() in ("windows"):
                    self.install("windows")
                elif host.lower() == "linux":

                    self.install("linux")
                else:
                    logger.info(
                        "Vision do not supports ,Unix or other platform except Linux and Windows.  Please Contact Support for further help.",
                    )
            print("Please do start the userbot again after python is installed ")
            exit(1)
        else:
            logger.info("Compatible Python Version Found.")

    def version(self):
        version = f"{sys.version_info[0]}" + f".{sys.version_info[1]}"
        return float(version)

    @staticmethod
    def gethost():
        return socket.gethostname()
