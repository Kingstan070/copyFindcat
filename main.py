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

def filter_text(content):
    '''
    To filter unwanted content from the web content

    content : String containing the web content

    returns : Returns the filtered list

    '''
    # Discard if the element is this
    black_list_full = ["share","learn more","all rights reserved",
                       "featured","search form","search","all categories",
                       "sign up for our newsletter", "sign up",
                       "select page","about"]

    # Discard if the element constains this
    black_list_few = ["https:/","http:/","recent blog posts",
                      "inc. all rights reserved."]
    '''
    # THIS IS NOT WORKING ! WHY!!!!!!!!!!!
    lg = len(content)
    for j in range(lg):
        l = len(content)
        for i in range(0,l):
            if content[i].strip() == '':
                content.pop(i)
                break
            else:
                for full in black_list_full:
                    if content[i].lower().strip() == full:
                        content.pop(i)
                        break
                for few in black_list_few:
                    if few in content[i]:
                        content.pop(i)
                        break
                break
    '''

    l = len(content)
    contents = []

    for i in range(l):
        test_element = content[i].lower().strip()
        if test_element in black_list_full:
            continue
        elif any(few in test_element for few in black_list_few):
            continue
        contents.append(content[i].strip())

    return contents












#------
# TEST
#------

print(filter_text(fl.get_content(sys.argv[1])))


#print(fl.get_content(sys.argv[1]))

#print(a.check4plagirism("src/text1.txt","src/text2.txt"))

#links = fl.get_url("Plagirism detector explained")
#for i in range(int(sys.argv[1])):
#    print(next(links))
