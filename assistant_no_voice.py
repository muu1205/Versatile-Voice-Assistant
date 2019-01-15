import webbrowser
import os
from google.cloud import translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C://Users//Owner//PycharmProjects//web//project.json'

def translatee(s):
    source = format(input("What do you want to translate?\n"))
    translate_client = translate.Client()
    target = s
    translation = translate_client.translate(source, target_language=target)
    print(u'Translation: {}'.format(translation['translatedText']))


def open_(s):
    if(s.find('facebook')!=-1):
        webbrowser.open_new_tab("https://www.facebook.com")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "facebook")
        os.system("adb shell input tap 136 339")
    elif(s.find('instagram')!=-1):
        webbrowser.open_new_tab("https://www.instagram.com")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "instagram")
        os.system("adb shell input tap 136 339")
    elif (s.find('twitter') != -1):
        webbrowser.open_new_tab("https://www.twitter.com")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "twitter")
        os.system("adb shell input tap 136 339")
    elif (s.find('youtube') != -1):
        webbrowser.open_new_tab("https://www.youtube.com")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "youtube")
        os.system("adb shell input tap 136 339")
    elif (s.find('google') != -1):
        webbrowser.open_new_tab("https://www.google.com")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "chrome")
        os.system("adb shell input tap 136 339")
    elif(s.find('calculator')!=-1):
        os.system("start calc.exe")
        os.system("adb shell input tap 540 1667")
        os.system("adb shell input tap 471 145")
        os.system("adb shell input text " + "calculator")
        os.system("adb shell input tap 136 339")
    elif (s.find('notepad') != -1):
        os.system("start notepad.exe")
    elif (s.find('ms paint') != -1):
        os.system("start mspaint.exe")

def close(s):
    if (s.find('Calculator') != -1 or s.find('calculator') != -1):
        os.system("taskkill /F /IM calc.exe")
    elif (s.find('Notepad') != -1 or s.find('notepad') != -1):
        os.system("taskkill /F /IM notepad.exe")
    elif (s.find('Ms Paint') != -1 or s.find('ms paint') != -1):
        os.system("taskkill /F /IM mspaint.exe")

def search(s):
    if (s.find('google') != -1):
        s = s.replace('search', '')
        s = s.replace('on google', '')
        s = s.strip()
        webbrowser.open_new_tab("http://google.com/search?q=" + s)
        os.system("adb shell input tap 342 258")
        os.system("adb shell input text " + s)
        os.system("adb shell input tap 985 1856")
    elif (s.find('youtube') != -1):
        s = s.replace('search', '')
        s = s.replace('on youtube', '')
        s = s.strip()
        webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + s)
    elif (s.find('facebook') != -1):
        s = s.replace('search', '')
        s = s.replace('on facebook', '')
        s = s.strip()
        webbrowser.open_new_tab("https://www.facebook.com/search/top/?q=" + s)
    elif (s.find('twitter') != -1):
        s = s.replace('search', '')
        s = s.replace('on twitter', '')
        s = s.strip()
        webbrowser.open_new_tab("https://twitter.com/search?q=" + s)
    elif (s.find('instagram') != -1):
        s = s.replace('search', '')
        s = s.replace('on instagram', '')
        s = s.strip()
        webbrowser.open_new_tab("https://instagram.com/" + s)

def call(s):
    os.system("cd C:\platform-tools")
    os.system("adb shell am start -a android.intent.action.CALL -d tel:" + s)

def text(numb):
        msg=input("What do you want to text?\n")
        os.system('adb shell am start -a android.intent.action.SENDTO -d sms:' + numb + ' --es sms_body "' + msg + '" --ez exit_on_sent false')
        os.system("adb shell input tap 1011 1859")

def text_w(numb):
    msg = input("What do you want to text?\n")
    os.system("adb shell am start -n com.whatsapp/.Main")
    os.system("adb shell input tap 890 132")
    os.system("adb shell input text " + numb)
    os.system("adb shell input tap 489 420")
    os.system("adb shell input tap 444 1166")
    os.system("adb shell input text " + msg)
    os.system("adb shell input tap 1021 1127")

s = input()
s.lower()

if(s.find('translate')!=-1):
    dict = {'bengali': 'bn', 'czech': 'cs', 'french': 'fr', 'hindi': 'hi', 'japanese': 'ja', 'kannada': 'kn',
            'malayalam': 'ml', 'punjabi': 'pa', 'russian': 'ru', 'spanish': 'es', 'tamil': 'ta', 'telugu': 'te',
            'urdu': 'ur'}
    s=s.replace('translate to','')
    s=s.strip()
    translatee(dict[s])
elif(s.find('open')!=-1):
    open_(s)
elif(s.find('close')!=-1):
    close(s)
elif(s.find('search')!=-1):
    search(s)
elif(s.find('call')!=-1):
    s = s.replace('call', '')
    s = s.strip()
    cont = {'parmeet': '7--------2', 'abhishek': '8--------8', 'rushil': '9--------5'}
    number = cont[s]
    call(number)
elif(s.find('text')!=-1):
    s = s.replace('text', '')
    s = s.strip()
    if(s.find('on whatsapp')!=-1):
        s = s.replace('on whatsapp', '')
        s = s.strip()
        cont = {'parmeet': '7--------2', 'abhishek': '8--------8', 'rushil': '9--------5'}
        number = cont[s]
        text_w(number)
    else:
        cont = {'parmeet': '7--------2', 'abhishek': '8--------8', 'rushil': '9--------5'}
        number = cont[s]
        text(number)
