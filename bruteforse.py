import os
import zipfile
import os
from time import time
def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
cls()
banner = '\n ###################################\n'

banner += ' [любой символ] Начать перебор\n'

print( banner)

a=input(" [?] Введите число : ")





def main(file_path, word_list):
    try:
        zip_ = zipfile.ZipFile(file_path)
    except zipfile.BadZipfile:
        print( "Это не zip архив")
        quit()

    password = None 
    i = 0 
    c_t = time()
    with open(word_list, "r") as f: 
        passes = f.readlines() 
        for x in passes:
            i += 1
            password = x.split("\n")[0]
            try:
                zip_.extractall(pwd=password.encode())
                t_t = time() - c_t 
                print( "\n [*] Пароль найден\n" + " [*] Пароль: "+password+"\n" )
                quit()
            except Exception:
                pass
        print( "Пароль не найден")
        quit()
        
main('test.zip', 'passes.txt')
