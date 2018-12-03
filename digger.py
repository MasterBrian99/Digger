#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Coded By Sameera a.k.a άλφα Χ

import os
import sys
import requests
import http.client


my_ip = requests.get("https://ident.me/").content.decode("UTF-8")


version = "2.0"


def logo():
    if sys.platform == 'win32':
        wlogo()
    else:
        llogo()


def wlogo():
    print('''
 _____  _
|  __ \(_)
| |  | |_  __ _  __ _  ___ _ __
| |  | | |/ _` |/ _` |/ _ \ '__|
| |__| | | (_| | (_| |  __/ |
|_____/|_|\__, |\__, |\___|_|
           __/ | __/ |       v2.0
          |___/ |___/

 [Coded By Sameera a.k.a άλφα Χ]

    {1} Whois lookup
    {2} Traceroute
    {3} DNS Lookup
    {4} Reverse DNS Lookup
    {5} GeoIP Lookup
    {6} Port Scan
    {7} HTTP Header Check
    {8} URL Extractor
    {9} robots.txt Checker
    {10} Update
    {11} Exit
''')


def llogo():
    print('''\033[31m
 _____  _
|  __ \(_)
| |  | |_  __ _  __ _  ___ _ __
| |  | | |/ _` |/ _` |/ _ \ '__|
| |__| | | (_| | (_| |  __/ |
|_____/|_|\__, |\__, |\___|_|
           __/ | __/ |       v2.0
          |___/ |___/

\033[37m[Coded By Sameera a.k.a άλφα Χ]
     \033[32m

    {1} Whois lookup
    {2} Traceroute
    {3} DNS Lookup
    {4} Reverse DNS Lookup
    {5} GeoIP Lookup
    {6} Port Scan
    {7} HTTP Header Check
    {8} URL Extractor
    {9} robots.txt Checker
    {10} Update
    {11} Exit
''')


logo()


def check_status():
    print("\t [#] Checking the availability of API server...")
    request = requests.get("https://hackertarget.com")
    http = request.status_code
    if http == 200:
        print("\t [#] API Server is Online")
    else:
        print("\t [!] Oops Error occured, Server offline")
        exit()


def quit():
    alpha = input("Are You Sure?[yes/no] - ").lower()
    if alpha == "yes":
        exit()
    if alpha == "no":
        logo()
        choice()


def choice():
    try:
        selection = input("Digger:- ")
        if selection == '1':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/whois/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter IP or Domain for lookup:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/whois/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '2':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/mtr/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter IP or Domain for lookup:- ")
                check_status()
                result2 = requests.get("https://api.hackertarget.com/mtr/?q=" + new)
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
            if digg == "yes":
                quit()
            if digg == "no":
                logo()
                choice()
            else:
                exit()

        elif selection == '3':
            dig = str(input("Enter Domain - "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/dnslookup/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '4':
            dig = str(input("IP Address / IP Range / Domain Name - "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/reversedns/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '5':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/geoip/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter ip address:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/geoip/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '6':
            dig = str(input("Do You Wish to Dig Your Own Information[yes/no] - ").lower())
            if dig == "yes":
                check_status()
                result = requests.get("https://api.hackertarget.com/nmap/?q=" +
                                      my_ip).content.decode("UTF-8")
                print(result)
                exit()
            if dig == "no":
                new = input("Enter ip address:- ")
                check_status()
                result2 = requests.get(
                    "https://api.hackertarget.com/nmap/?q=" + new).content.decode("UTF-8")
                print(result2)
                exit()
            else:
                digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                if digg == "yes":
                    quit()
                if digg == "no":
                    logo()
                    choice()
                else:
                    exit()

        elif selection == '7':
            dig = str(input("Enter web address:- "))
            check_status()
            result = requests.get(
                "https://api.hackertarget.com/httpheaders/?q=" + dig).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '8':
            website = str(input("Enter web address:-"))
            website = website.replace("http://", "")
            website = website.replace("https://", "")
            website = ("https://" + website)
            check_status()
            result = requests.get("https://api.hackertarget.com/pagelinks/?q=" +
                                  website).content.decode("UTF-8")
            print(result)
            exit()

        elif selection == '9':
            dig = str(input("Enter web address:- "))
            check = requests.get(dig + '/robots.txt')
            if '<html>' in check.text:
                print("Robots.txt not found")
            else:
                print("Robots.txt found.")
                print(check.text)

        elif selection == '10':
            print("Checking for updates...")
            digger = requests.get(
                "https://raw.githubusercontent.com/Sameera-Madhushan/Digger/master/digger.py").content.decode("UTF-8")
            if version not in digger:
                co = input(
                    "A new version of Digger is available. Would you like to update?[yes/no] - ").lower()
                if co == "yes":
                    os.system(
                        'cd .. && rm -r Digger && git clone https://github.com/Sameera-Madhushan/Digger')
                if co == "no":
                    logo()
                    choice()
                else:
                    digg = str(
                        input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
                    if digg == "yes":
                        quit()
                        if digg == "no":
                            logo()
                            choice()
                        else:
                            exit()
            else:
                print("Digger is Upto Date.")
                exit()

        elif selection == '11':
            quit()

        else:
            digg = str(input("Sorry!Invalid Selection. Do You Wish to Quit[yes/no] - ").lower())
            if digg == "yes":
                quit()
            if digg == "no":
                logo()
                choice()
            else:
                exit()

    except(KeyboardInterrupt):
        print("Programme Interrupted")
    except requests.exceptions.ConnectionError:
        print('Your Internet is Offline')
        exit


choice()

'''
- References -
https://hackertarget.com/ip-tools/
'''
