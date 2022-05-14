
import sys

import Checker.standard_checker as a
import scrapper.find_link as fl

print(a.check4plagirism("src/text1.txt","src/text2.txt"))

#links = fl.get_url("Plagirism detector explained")
#for i in range(int(sys.argv[1])):
#    print(next(links))
