import pandas as pd
import re

text = """
msgid ""
msgstr ""
"Project-Id-Version: Shin Megami Tensei: Devil Summonner: Soul Hackers\n"
"Report-Msgid-Bugs-To: tradusquare@gmail.com\n"
"POT-Creation-Date: 25/10/2018\n"
"PO-Revision-Date: \n"
"Last-Translator: \n"
"Language-Team: TraduSquare\n"
"Language: es\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"'

msgctxt "0"
msgid ""
"{FF05}{006D}{FF19}{C7B7}Monitor{C7B8}{FF16}Hello. Welcome to the\n"
"Amami Net terminal.\n"
"{FF03}{FF00}"
msgstr ""

msgctxt "1"
msgid "{FF05}{006E}> What will you do?{FF00}"
msgstr ""

msgctxt "2"
msgid "Save{FF00}"
msgstr ""

msgctxt "3"
msgid "Install{FF00}"
msgstr ""

msgctxt "4"
msgid "Check Mail{FF00}"
msgstr ""

msgctxt "5"
msgid "Exit{FF00}"
msgstr ""

msgctxt "6"
msgid "Algon Main Building 2F{FF00}"
msgstr ""

msgctxt "7"
msgid ""
"You have 1 new message.\n"
"{FF03}{FF02}Would you like to read it?{FF00}"
msgstr "" """


# REMOVE fields we do not need, quotes, and scripted blocks, leaving FF16 as it = player name
regex = r'(?!\})\w{1,}\{C7B8\}|.*\w{1,}\{FF00\}|(">.*)|(".{0,}-.*)|(?!msgstr)(msg.*)|("Language:.*)|(\{.{4}\})(?!\{FF16\})|(<.*>)|(\[.*\])|(#\. .*)|"|\\n'
subst = ""
text = re.sub(regex, subst, text, 0)

# CONVERT \n to _space_
regex = r'(\n|\r)'
subst = " "
text = re.sub(regex, subst, text, 0)

# REPLACE each 'msgstr '(with variable space)(include successive matches) into a line break as these designate each game chunk of dialog
regex = r'((msgstr {1,}){1,})'
subst = "\r"
text = re.sub(regex, subst, text, 0)

# REPLACE multiple _space_ into a single _space_
regex = r' {1,}'
subst = " "
text = re.sub(regex, subst, text, 0)

df = pd.DataFrame(pd.array([text]))
df.to_csv('clean_script.csv')