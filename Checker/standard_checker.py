from difflib import SequenceMatcher

def check4plagirism(testfile, text):
    '''
    testfile : receives the test file
    text     : reveives the text file to be tested for plagirism
    
    returns  : float value percentage of plagirism in text file
    '''
    with open(testfile) as file1, open (text) as file2:
        filedata = file1.read()
        file2data = file2.read()
        similarity = SequenceMatcher(None, filedata, file2data).ratio()
        return (similarity*100)
