import pyperclip as pc

text = pc.paste()

text = text.split("\n")
for line in text:
    print("* " + line)
