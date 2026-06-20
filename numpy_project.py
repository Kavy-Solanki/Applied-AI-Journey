import numpy as np 

def open_file(name):
    try:
        with open(name, "r") as file:
            print("File Found")
            return True
    except FileNotFoundError:
        print("File not found!")
        return False

while True:
    print("NOTE: Pls Make Sure the file contains on numbers, separated by some separator.")
    name = input("Enter the file name(with extension): ")
    if(open_file(name)):
        break
    print("Pls Enter a Valid File Name.")

sep = input("What separator(',' '.' , etc) does the file has: ")
try:
    filedata = np.genfromtxt(name, delimiter=sep)
    filedata = filedata.astype("float32")
    print(f"The average Makrs are:{np.mean(filedata)}")
    print(f"The Highest marks are:{np.max(filedata)}")
    print(f"The Lowest marks are:{np.min(filedata)}")
    print(f"The standard deviation is:{np.std(filedata)}")
except Exception:
    print("An Error Has Occurred.")
    print("The File Contains data other than Numbers.")