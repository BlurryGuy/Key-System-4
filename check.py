import requests
from colorama import *
import time
import sys
import socket

r = requests.get('http://jsonip.com')
address = r.json()['ip']
allowed_ips = {hash("53.152.21.1"), hash("153.22.135.3")}
allowed_pcs = {hash("DESKTOP-MRPNUES"), hash("DESKTOP-ZGJAUHES")}
this_is_my_array = {hash("key1"), hash("key2"), hash("key3")}
pc = socket.gethostname()

def check_ip(ip):
    if hash(ip) in allowed_ips:
         return "Success"
    else:
         return "Failure"

def check_pc(pc_name):
    if hash(pc) in allowed_pcs:
       return "Success"
    else:
         return "Failure"

def print01(chat):
    for i in chat:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)

print01(Fore.GREEN + "> " + Fore.RESET + "Enter your key: ")

user_input = input("")

try:

   if hash(user_input) in this_is_my_array:
   
      print01(Fore.GREEN + "> " + Fore.RESET + "Valid Key!")
      time.sleep(1.3)
      print01(Fore.GREEN + "\n> " + Fore.RESET + "Checking your IP!")
      time.sleep(1.3)
      if check_ip(address) == "Success":
         print01(Fore.GREEN + "\n> " + Fore.RESET + "Whitelisted IP!")
         time.sleep(1.3)
         print01(Fore.GREEN + "\n> " + Fore.RESET + "Checking PC Name!")
         time.sleep(0.6)
         if check_pc(pc) == "Success":
            print01(Fore.GREEN + "\n> " + Fore.RESET + "Whitelisted PC Name!")
            
            # do stuff here
            
         else:
             print01(Fore.RED + "\n> " + Fore.RESET + "Non-Whitelisted PC Name!")
             input()
      else:
           print01(Fore.RED + "\n> " + Fore.RESET + "Non-Whitelisted IP!")
           input()
      input()   
   else:

      print01(Fore.RED + "> " + Fore.RESET + "Invalid Key!")
      
      input()
except:
      print01("You tried to check if a string exists in a non-existing array or put wrong variable / array name!")
      
      input()
