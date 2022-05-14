import os
import sys

import Checker.standard_checker as a
import scrapper.find_link as fl

from rich import print as rprint
from rich.progress import track
from rich.prompt import Prompt

banner = '''
 _____                  ______ _           _ _____       _   
/  __ \                 |  ___(_)         | /  __ \     | |  
| /  \/ ___  _ __  _   _| |_   _ _ __   __| | /  \/ __ _| |_ 
| |    / _ \| '_ \| | | |  _| | | '_ \ / _` | |    / _` | __|
| \__/| (_) | |_) | |_| | |   | | | | | (_| | \__/| (_| | |_ 
 \____/\___/| .__/ \__, \_|   |_|_| |_|\__,_|\____/\__,_|\__|
            | |     __/ |                                    
            |_|    |___/                                     


'''
got_file = False
try:
    f_locationTEST = sys.argv[1]
    got_file = True
except:
    f_locationTEST = "src/text1.txt"
    f_locationDUPL = "src/text2.txt"

#os.system('cls||clear')
#print(banner)

def write_file(data, f_location):
    '''
    To clear the text and add the text from
    the list data

    data       : list of strings
    f_location : string with the location
                 of text file

    returns    : None

    '''
    data = [i+"\n" for i in (data)]
    with open(f_location, 'w') as f1:
        f1.write("")
    with open(f_location, 'a') as f1:
        f1.writelines(data)

def getData_lines():
    '''
    To get the text with different lines

    returns  : List of, strings of lines

    '''
    try:
        i = 0
        lines = [""]
        lines[0] = input("Enter the text     : ")
        while True:
            i += 1
            lines.append(Prompt.ask("Ctrl+C to Exit     "))
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        print()
        return lines


print(fl.get_content(sys.argv[1]))

#print(a.check4plagirism("src/text1.txt","src/text2.txt"))

#links = fl.get_url("Plagirism detector explained")
#for i in range(int(sys.argv[1])):
#    print(next(links))
