import os
import sys

import Checker.standard_checker as a
import scrapper.find_link as fl

from rich import print as rprint
from rich.progress import track
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

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
f_locationTEST = "src/test1.txt"
try:
    f_locationDUPL = sys.argv[1]
    got_file = True
except:
    f_locationDUPL = "src/text2.txt"

def main():
    global got_file
    global f_locationTEST
    global f_locationDUPL

    deapth = 10;

    os.system('cls||clear')
    rprint("- "*35)
    print(banner)
    rprint("  "*25+"[purple]v. 1.0.")
    rprint("- "*35)
    print()

    # Getting the file or DATA for file, if file not provided
    if not(got_file):
        choice = Prompt.ask("Would like to enter text manually or enter file location",
                            choices=["tm","l"])

        if choice == "l":
            f_locationDUPL = Prompt.ask("Enter text file location")
            got_file = True
        elif choice == "tm":
            DATA = getData_lines()
            os.system('cls||clear')
            rprint("- "*35)
            print(banner)
            rprint("  "*30+"[purple]v. 1.0.")
            rprint("- "*35)
            print()
        else:
            rprint("[red] Unexpected error occured!")
            exit()

    # Writing the DATA to file, if the file in not provided
    if not got_file:
        write_file(DATA, f_locationDUPL)

    search_keys = getKeyword(f_locationDUPL)

    url_and_percentage = {}
    url_list = fl.get_url(search_keys[0]+" "+search_keys[-1])
    if (len(url_list) <= deapth):
        deapth = url_list
    for i in track(range(deapth),
                   description="[cyan]Processing...      "):
        try:
            url_link = url_list[i]
            url_content = fl.get_content(url_link)
            write_file(url_content, f_locationTEST)
            url_and_percentage[url_link] = a.check4plagirism(f_locationTEST,
                                                           f_locationDUPL)
        except StopIteration:
            break
        except Exception as e:
            print(e)

    pretty_print_result(url_and_percentage)


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

def getKeyword(file_Location):
    '''
    To get the string to be used as a search item to
    get the url

    file_location : String of the location file

    return        : list of String of search item

    '''
    search_list = []
    with open(file_Location,"r") as file:
        line = file.readline()
        if ("." not in line) and (len(line.split()) < 10):
            search_list.append(line)
        try:
            for i in track(range(10),
                           description="Getting search keys"):
                line = file.readline()
                search_list.append(line.split('.')[0])
                search_list.append(line.split('.')[-1])
        except:
            rprint("[red]Unexpected Error occured in getKeyword function!")

    return filter_text(search_list)


def pretty_print_result(url_and_per):
    '''
    To pretty print the result in a table format

    url_and_per : Dictionary containing the url and percentage
                  of plagirism

    returns     : None
    '''

    # Sorting the key-value pair in dictionary to list
    result = sorted( url_and_per.items(), key=lambda x: x[1],
                    reverse=True )

    # Creating table using rich module
    table = Table(title="Result with Percentage of Plagiarism")
    table.add_column("No.",justify="left",style="cyan")
    table.add_column("URL",style="blue")
    table.add_column("Percentage %", justify="center",style="green")
    for i in range(len(result)):
        table.add_row(str(i+1)+".",result[i][0],str(result[i][1]))
    console = Console()
    console.print(table)

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
                       "select page","about","\n",""," "]

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

    content.clear()
    return contents


if __name__ == '__main__':
    main()









#------
# TEST
#------

#print(filter_text(fl.get_content(sys.argv[1])))


#print(fl.get_content(sys.argv[1]))

#print(a.check4plagirism("src/text1.txt","src/text2.txt"))

#links = fl.get_url("Plagirism detector explained")
#for i in range(int(sys.argv[1])):
#    print(next(links))
