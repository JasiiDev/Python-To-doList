import ctypes
import os
from tkinter import filedialog
from tkinter import *
import time
root = Tk()
root.withdraw()
list = []
version = "1.0.2"


def messageBox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)

def clear():
    os.system('cls')

def WelcomeMessage():
    clear()
    print("Welcome to To-doList console list by JasiiDev")
    print("Ver: {}".format(version))

def typeMessage():
    print('[*] Option list>')
    print('[1] Add Item')
    print('[2] Remove Item')
    print('[3] Item List')
    print('[4] Quit')

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def getPath(type):
    appdataFolder = os.getenv('LOCALAPPDATA')
    path = os.path.join(appdataFolder, "To-DoList")
    fullPath = path + '/app.init'
    if type == 'init':
        return fullPath
    if type == 'file':
        lines = open(fullPath, 'r').readlines()
        listPath = lines[1]
        listPath = listPath.replace('Path=', '')
        fullListPath = listPath + '/list.txt'
        return fullListPath

def run():
    WelcomeMessage()
    while True:
        typeMessage()
        try:
            option = int(input('[?] Type option> '))
        except:
            messageBox('Error', 'Only> 1 or 2 or 3 or 4', 0)
            break


        if option == 1:
            while True:
                item = input('Type item (q for leave) > ')
                if item != 'q':
                    with open(getPath('file'), 'a') as f:
                        f.write(item + '\n')
                    f.close()
                else:
                    clear()
                    WelcomeMessage()
                    break
        if option == 2:
            clear()
            lines = open(getPath('file'), 'r').readlines()
            if len(lines) > 0:
                print('[Info] All Item List>')
                count = 0
                for i in lines:
                    count += 1
                    i = i.replace('\n', '')
                    print('{}. {}'.format(count, i))

                number = int(input('Type number: '))

                # f = open(getPath('file'), 'r')
                # lst = []
                filename = getPath('file')
                line_to_delete = number
                initial_line = 1
                file_lines = {}
                with open(filename) as f:
                    content = f.readlines()
                for line in content:
                    file_lines[initial_line] = line.strip()
                    initial_line += 1
                f = open(filename, "w")
                for line_number, line_content in file_lines.items():
                    if line_number != line_to_delete:
                        f.write('{}\n'.format(line_content))
                f.close()
                clear()
                WelcomeMessage()
                print('[Info] Item> {} deleted.'.format(line_to_delete))
            else:
                WelcomeMessage()
                print('[Info] Item list empty.')

        if option == 3:
            clear()
            lines = open(getPath('file'), 'r').readlines()
            if len(lines) > 0:
                print('[Info] Item list>')
                count = 0
                for i in lines:
                    count += 1
                    i = i.replace('\n', '')
                    print('{}. {}'.format(count, i))
                print('Press enter to continue or q (and enter) for remove all items.')
                optionList = input('[*] Type q or enter> ')
                if optionList == 'q':
                    file = open(getPath('file'), 'w')
                    file.close()
                    clear()
                    WelcomeMessage()
                    print('[Info] Item list deleted.')
                else:
                    clear()
                    WelcomeMessage()
            else:
                WelcomeMessage()
                print("[Info] List is empty.")


        if option == 4:
            clear()
            print('Thank u! By JasiiDev')
            time.sleep(2)
            break

#def test():
    #Some stuff

def loadBasics():
    appdataFolder = os.getenv('LOCALAPPDATA')
    path = os.path.join(appdataFolder, "To-DoList")
    fullPath = path + '/app.init'

    if not os.path.exists(path):
        os.mkdir(path)
        print("To-doList: Folder Created.")
        with open(fullPath, 'w') as f:
            f.write('#File from To-doList By JasiiDev\nPath=Unknown')

        folder_selected = filedialog.askdirectory(title='Selecciona una ruta de instalación')
        replace_line(fullPath, 1, 'Path={}'.format(folder_selected))
        print("To-doList: Folder route selected and saved.")
    else:
        if not os.path.exists(fullPath):
            with open(fullPath, 'w') as f:
                f.write('#File from To-doList By JasiiDev\nPath=Unknown')
            folder_selected = filedialog.askdirectory(title='Selecciona una ruta de instalación')
            replace_line(fullPath, 1, 'Path={}'.format(folder_selected))
            print("To-doList: Folder route selected and saved.")

    lines = open(fullPath, 'r').readlines()

    listPath = lines[1]
    listPath = listPath.replace('Path=', '')
    fullListPath = listPath + '/list.txt'
    if not os.path.exists(fullListPath):
        with open(fullListPath, 'w') as f:
            f.write('')
            print("To-doList: List File is created.")

    if os.path.exists(path) and os.path.exists(fullListPath):
        run()
        #test()

loadBasics()

#Coded by JasiiDev




