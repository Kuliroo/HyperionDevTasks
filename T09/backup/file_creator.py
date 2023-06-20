'''import os

file_path = 'E:\Dropbox\Dropbox\JW23010007376\DataScience(Fundamentals)\T09\file.txt'

if os.path.isfile(file_path):
    print('File already exists')
else:
    with open(file_path, 'w')as file:
        file.write('Hello, Wordl!')
    print('File created')

file_name = input("Please provide file name: ")

f = open(file_name, "a")
f.write("XXXXX")
f.close()'''

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

