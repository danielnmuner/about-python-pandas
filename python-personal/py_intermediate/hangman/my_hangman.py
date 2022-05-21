import os
import random
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def header():
    print('\n'*2)
    print(''.center(50,'-'))
    print(''' _   _                  ___  ___            
| | | |                 |  \/  |            
| |_| | __ _ _ __   __ _| .  . | __ _ _ __  
|  _  |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ 
| | | | (_| | | | | (_| | |  | | (_| | | | |
\_| |_/\__,_|_| |_|\__, \_|  |_/\__,_|_| |_|
                    __/ |                   
                   |___/                 '''.center(100,'*'))
    print(''.center(50,'-'))
    print('\n'*2)

def footer():
    print('\n'*2)
    print(''.center(50,'-'))
    print(''' _____ _   _       _____                _ 
|_   _| | ( )     |  ___|              | |
  | | | |_|/ ___  | |__  __ _ ___ _   _| |
  | | | __| / __| |  __|/ _` / __| | | | |
 _| |_| |_  \__ \ | |__| (_| \__ | |_| |_|
 \___/ \__| |___/ \____/\__,_|___/\__, (_)
                                   __/ |  
                                  |___/ '''.center(100,'*'))
    print(''.center(50,'-'))


def get_word():
    word = random.choice(read_file()).upper().strip()
    return word


def read_file():
    
    with open('./country.csv','r',encoding='utf-8') as data:
        dat=[line.strip() for line in data]
        return dat


def eval_letter(word,blanks):
    user_letter = input('Ingresa una Lettra: ').upper()
    assert len(user_letter) == 1, 'Ingresa una Sola Letra'
    for i,l in enumerate(word):
        if l == user_letter:
            blanks[i]=user_letter
        else:
            continue   
    return ''.join([str(blank) for blank in blanks])


def get_answer():
    word = get_word() 
    blanks = ['_' for blank in range(len(word))]
    player = eval_letter(word,blanks)
    while True:
        screen_clear()
        print(eval_letter(word,blanks))
        if eval_letter(word,blanks) == word:
            break


def run():
    header()
    get_answer()
    footer()

if __name__ == '__main__':
    run()