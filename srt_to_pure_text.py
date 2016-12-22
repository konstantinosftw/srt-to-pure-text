import re

file = raw_input("Enter file name.\nIf the tile is not in tha same folder as this script, paste its whole path.\n\n> ")

if file[-4:] != (".srt", ".SRT"):

	file += ".srt"

f = open(file)

cont = f.read()
f.close()

text = re.sub(r'\d+\n\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n', '', cont)

print(text)

new_f = open(file.strip('.srt')+".txt", "w")

new_f.write(text)
new_f.close()

print('Done!')
