import polib
import pandas as pd
import re
import os

#po = polib.pofile('Scripts/es/CENT_TWR.EVE.po')
po = ""
text = " lINEbREAK\n"

# Add breaks after each line (Or else Regex will eat EVERYTHING.
#for filename in os.scandir('Scripts/es/'):
for filename in os.scandir('Scripts/nocturneBFs/'):
#for filename in os.scandir('Scripts/raidouBFs'):
    po = polib.pofile(filename)
    for line in po:
        txt = str(line.msgid).splitlines()
        for tx in txt:
            text += tx + " \n"
        text += "lINEbREAK\n"

"""REMOVE fields we do not need such as {####} engine commands, however leaving FF8# as it = player name
It's unknown at this time how the player name will be inserted into the text using NLP"""
# previous regex we might want to refer to = r'(".{0,}-.*)|(?!msgstr)(msg.*)|("Language:.*)|(?!\{FF16\})(\{.{4}\})|(<.*>)|(\[.*\])|(#\. .*)|"|\\n'
# remove everything before FF00 & C7B8, lines that start with >, keep FF80 & FF81, remove all other {####}, remove <tags>, remove linebreaks & returns
# es
#regex = r'.*(\{FF00\}|\{C7B8\})|(>.*)|(?!\{FF8\d\})(\{.{4}\})|(<.*>)|\n|\r'
# nocturne
regex = r'.*(\{FF00\}|\{C7B8\})|(?!\{FF8\d\})(\{.{4}\})|(<.*>)|(\[.*\])|(#\. .*)|"|\\n'

subst = ""
text = re.sub(regex, subst, text, 0)

regex = r'((.*You\s\w*\snot.*|.*You\sobtained.*|.*Your\sparty.*|The\s\w*\seffect)(\s\S{1,}){0,}|(?=lINEbREAK))'
# #regex = r'(.*a(\s\w{1,}){1,}\.\sWill\syou.*)|(\s{0,}You\sdid\snot\sopen\sthe.*)'
subst = ""
text = re.sub(regex, subst, text, 0)

#will get rid of 'will you open it' 'what will you do', but not the lines preceeding 'will you open it'
regex = r'((?!.+gather)(.*[wW]ill\syou)(\s{1,2}(?!lINEbREAK)\S{1,}){0,})'
subst = ""
text = re.sub(regex, subst, text, 0)

regex = r'(\.{2,}|\n|\r)' 
subst = ""
text = re.sub(regex, subst, text, 0)

regex = r'\s{2,}'
subst = " "
text = re.sub(regex, subst, text, 0)

regex = r'((lINEbREAK)\s{0,1}){1,}'
subst = "\r"
text = re.sub(regex, subst, text, 0)

# df = pd.DataFrame(pd.array([text]))
# df.to_csv('clean_script.csv')
File_object = open(r"clean_script.txt","w")

for line in text:
    File_object.write(line)