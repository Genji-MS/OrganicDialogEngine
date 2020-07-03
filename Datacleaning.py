import polib
import pandas as pd
import re

#TODO : add Cleaning of entire folder
po = polib.pofile('Scripts/es/CENT_TWR.EVE.po')

text = " lINEbREAK\n"

"""
PATTERN can be: 
{####} line
line
line
This will add breaks after each line (Or else Regex will eat EVERYTHING.
And specify the sentence breaks as .po is designed for a game and has numerious linebreaks that we want to join"""

for line in po:
    txt = str(line.msgid).splitlines()
    for tx in txt:
        text += tx + " \n"
    text += "lINEbREAK\n"


"""REMOVE fields we do not need such as {####} engine commands, however leaving FF80/FF81 as it = player name"""
# previous regex we might want to refer to = r'(".{0,}-.*)|(?!msgstr)(msg.*)|("Language:.*)|(?!\{FF16\})(\{.{4}\})|(<.*>)|(\[.*\])|(#\. .*)|"|\\n'
# remove everything before FF00 & C7B8, lines that start with >, keep FF80 & FF81, remove all other {####}, remove <tags>, remove linebreaks & returns
regex = r'.*(\{FF00\}|\{C7B8\})|(>.*)|(?!\{FF80\}|\{FF81\})(\{.{4}\})|(<.*>)|\n|\r'
subst = ""
text = re.sub(regex, subst, text, 0)

regex = r'( lINEbREAK){1,}'
subst = "\r"
text = re.sub(regex, subst, text, 0)


df = pd.DataFrame(pd.array([text]))
df.to_csv('clean_script.csv')