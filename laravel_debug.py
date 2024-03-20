#!/usr/bin/python3

import requests as req
import urllib3
from multiprocessing.dummy import Pool
from colorama import Fore, Style
from os import system, name
from os.path import exists

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class LaravelDebugScanner:
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        }

    def clear_screen(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def scan_site(self, site):
        try:
            r = req.get(f"{site}/_ignition/health-check", timeout=300, headers=self.header, verify=False)
            if '{"can_execute_commands":true}' in r.text and r.status_code == 200:
                print(f"{Fore.GREEN + '[+]' + Style.RESET_ALL} {Fore.GREEN + r.url + Style.RESET_ALL}")
                with open("laravel-log.txt", "a") as wr:
                    wr.write(site + "\n")
            else:
                print(f"{Fore.RED + '[!]' + Style.RESET_ALL} {site} => NOT FOUND!")
        except:
            pass

    def main(self):
        print(Fore.GREEN + """ 
        +---------[ Laravel Debug Scanner ]---------+
        + Github   : github.com/MadExploits         +
        + Telegram : t.me/@MadShells                +
        + Laravel Debug Scanner                     +
        +-------------------------------------------+
        """ + Style.RESET_ALL)
        
        input_file = input("List : ")
        if exists(input_file):
            thread = input("Thread : ")
            with open(input_file, "r") as f:
                websites = f.read().split("\n")
                with Pool(int(thread)) as pool:
                    pool.map(self.scan_site, websites)
                    pool.close()
                    pool.join()
        else:
            print("File not found")

if __name__ == "__main__":
    scanner = LaravelDebugScanner()
    scanner.clear_screen()
    scanner.main()
