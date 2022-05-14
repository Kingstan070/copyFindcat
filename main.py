import os
import sys

import Checker.standard_checker as a
import scrapper.find_link as fl

from rich import print as rprint

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
print(sys.argv[1])

f_locationTEST = "src/text1.txt"
f_locationDUPL = "src/text2.txt"

os.system('cls||clear')
print(banner)

def write_file(data, f_location):
    pass
#print(a.check4plagirism("src/text1.txt","src/text2.txt"))

#links = fl.get_url("Plagirism detector explained")
#for i in range(int(sys.argv[1])):
#    print(next(links))
