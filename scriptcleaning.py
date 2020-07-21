import pandas as pd
import re
import os

file = open(r"FatherTime_Dialog.txt","r")
text = ""
for line in file:
    text += line
file.close()

regex = r'((,){0,}\[|\](,){0,})|((\d){0,},\d(,){0,})|(","|")|((\\){1,})'
subst = ""
text = re.sub(regex, subst, text, 0)

regex = r'(\/\d)'
subst = "\r"
text = re.sub(regex, subst, text, 0)

File_object = open(r"FatherTime_Dialog_clean.txt","w")

for line in text:
    File_object.write(line)