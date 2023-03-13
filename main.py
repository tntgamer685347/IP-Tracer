import os, requests, urllib.request 
from datetime import datetime
from colorama import Fore, just_fix_windows_console, Style

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
YELLOW = Fore.YELLOW
LY = Fore.LIGHTYELLOW_EX
RESET = Fore.RESET
BOLD = '\033[1m'

ERROR = f"[{RED}E{RESET}]: "
INFO = f"[{LY}Info{RESET}]: "
INPUT = f"{BLUE}[{CYAN}?{BLUE}]{RESET }"

def printBanner(_win32):
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    banner = f"""{YELLOW}{BOLD}  {RED}{BOLD}_{YELLOW}{BOLD}          _______                      
 {RED}{BOLD}(_){YELLOW}{BOLD}        |__   __|                     
  _ _ __ ______| |_ __ __ _  ___ ___ _ __ 
 | | '_ \______| | '__/ _` |/ __/ _ \ '__|
 | | |_) |     | | | | (_| | (_|  __/ |   
 |_| .__/      |_|_|  \__,_|\___\___|_|   
   | |                                    
   |_|{RESET}{YELLOW}{BOLD}                                                                           
    Your IP address: {external_ip}{BOLD}
    Type Help For Help!{RESET}{BOLD}
    """
    print(banner)
    

    #if _win32:
    #    pyshade.Mode.Horizontal(pyshade.colors.yellow_to_red, banner)
    #else:
    #    print(pyshade.Mode.Horizontal(pyshade.colors.yellow_to_red, banner))

def clear(_win32):
    if _win32:
        os.system('cls')
        printBanner(_win32)
    else:
        os.system('clear')
        printBanner(_win32)

try:
    import win32api
    _win32 = True
except:
    _win32 = False

if _win32:
    try:
        just_fix_windows_console()
    except:
        pass
else:
    pass

clear(_win32)

def getInfo(IP):
    api_url = f"http://ip-api.com/json/{IP}"
    try:
        r = requests.get(api_url)
        js = r.json()
        return (js)
    except:
        return None

def getInfoJson(IP):
    Info = getInfo(IP)
    try:
        succ = Info['status']
        try:
            country = Info['country']
        except:
            country = 'Error'
        try:
            countryCode = Info['countryCode']
        except:
            countryCode = 'Error'
        try:
            region = Info['region']
        except:
            region = 'Error'
        try:
            regionName = Info['regionName']
        except:
            regionName = 'Error'
        try:
            city = Info['city']
        except:
            city = 'Error'
        try:
            timezone = Info['timezone']
        except:
            timezone = 'Error'
        try:
            zipcode = Info['zip']
        except:
            zipcode = 'Error'
        try:
            ISP = Info['isp']
        except:
            ISP = 'Error'
        try:
            org = Info['org']
        except:
            org = 'Error'
        try:
            asn = Info['as']
        except:
            asn = 'Error'
        try:
            latidude  = Info['lat']
        except:
            latidude = 'Error'
        try:
            longtitude = Info['lon']
        except:
            longtitude = 'Error'
        if not longtitude == 'Error' or not latidude == 'Error':
            location = str(latidude)+', '+str(longtitude)
        else:
            location = "Error"
        return succ, country, countryCode, region, regionName, city, timezone, zipcode, ISP, org, asn, location, latidude, longtitude
    except Exception as e:
        #print(f'{ERROR}Invalid IP or Private IP!, exc: {e}')
        return 'Error','Error','Error','Error','Error','Error','Error','Error','Error','Error','Error','Error','Error','Error',
    

#printBanner(_win32)

while True:

    option = input(f'{INPUT}-> ')
    option = option.lower()

    if option == "help":
        print(f'{INFO}[Track -> <Lets You Track an <PUBLIC>or<ipv6> ip address>] (More Modules Will come!)')
    elif option == "track":
        clear(_win32)
        IP = input(f'{INPUT}Ip Address -> ')
        succ, country, countryCode, region, regionName, city, timezone, zipcode, ISP, org, asn, location, latidude, longtitude  = getInfoJson(IP)
        date = datetime.now()
        clear(_win32)
        print()
        print()
        print('   }'+RED+'─────────────────────────────────────────────────────────'+RESET+"{")
        print('}'+RED+'─────────────────────────'+CYAN+'IP Information'+RED+'─────────────────────────'+RESET+"{")
        print('   }'+RED+'─────────────────────────────────────────────────────────'+RESET+"{")
        print()
        print()
        print(f'{YELLOW}{BOLD}IP Address{RESET}    {BOLD}>    {CYAN}{BOLD}{IP}{RESET}')
        print(f'{YELLOW}{BOLD}Country code{RESET}  {BOLD}>    {CYAN}{BOLD}{countryCode}{RESET}')
        print(f'{YELLOW}{BOLD}Country{RESET}       {BOLD}>    {CYAN}{BOLD}{country}{RESET}')
        print(f'{YELLOW}{BOLD}Date & Time{RESET}   {BOLD}>    {CYAN}{BOLD}{date}{RESET}')
        print(f'{YELLOW}{BOLD}Region code{RESET}   {BOLD}>    {CYAN}{BOLD}{region}{RESET}')
        print(f'{YELLOW}{BOLD}Region{RESET}        {BOLD}>    {CYAN}{BOLD}{regionName}{RESET}')
        print(f'{YELLOW}{BOLD}City{RESET}          {BOLD}>    {CYAN}{BOLD}{city}{RESET}')
        print(f'{YELLOW}{BOLD}Zip Code{RESET}      {BOLD}>    {CYAN}{BOLD}{zipcode}{RESET}')
        print(f'{YELLOW}{BOLD}Time Zone{RESET}     {BOLD}>    {CYAN}{BOLD}{timezone}{RESET}')
        print(f'{YELLOW}{BOLD}City{RESET}          {BOLD}>    {CYAN}{BOLD}{city}{RESET}')
        print(f'{YELLOW}{BOLD}ISP{RESET}           {BOLD}>    {CYAN}{BOLD}{ISP}{RESET}')
        print(f'{YELLOW}{BOLD}Organisation{RESET}  {BOLD}>    {CYAN}{BOLD}{org}{RESET}')
        print(f'{YELLOW}{BOLD}ASN{RESET}           {BOLD}>    {CYAN}{BOLD}{asn}{RESET}')
        print(f'{YELLOW}{BOLD}Latitude{RESET}      {BOLD}>    {CYAN}{BOLD}{latidude}{RESET}')
        print(f'{YELLOW}{BOLD}Longtitude{RESET}    {BOLD}>    {CYAN}{BOLD}{longtitude}{RESET}')
        print(f'{YELLOW}{BOLD}Location{RESET}      {BOLD}>    {CYAN}{BOLD}{location}{RESET}')
        input()
        clear(_win32)
            
    elif option == "clear":
        clear(_win32)
    else:
        print(f'{ERROR}No Module With That Name Found')
