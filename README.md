# copyFindcat
copyFindcat is a python script which sraps throught internet to find any possible plagirism.
The script manily consist of two files `scrapper` and `Checker`.
The `scrapper` file consist of function which deals with finding the content from internet and `Checker` has the function which compares two text and returns the percentage of plagiriasm.

##Installation

### Installing `virtualenve` if not installed
 Assuming python and pip is already in the system.
 
 For Unix/macOS:
```
python3 -m pip install --user virtualenv
```
 For windows:
```
py -m pip install --user virtualenv
```
### Getting Started

  For Unix/masOS:
  
 ```
 git clone https://github.com/Kingstan070/copyFindcat.git
 cd copyFindcat
 pip install -r requirements.txt
 ```
 
  For windows:
Download the zip file and extract. And open a command prompt on file location.
```
pip install -r requirements.txt
```
## Running the project
To run the project
```
python -m main
```
Also, can pass the location of the text as an argument (file location should be relative to the `main.py`)

```
python -m main <file_location>
```
e.g. `python -m main src/text2.txt`

Also, can mention whether to display visual representation of plagiriasm or not.
For visual representation just add `show`
```
python -m main <file_location> show
```
