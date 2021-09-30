#pip install pyshorteners

import pyshorteners
import os

os.system("clear")

print("""
this LİNK SHORTENER was created by Berat

github.com/Ermsberat
""")

link = input("Link: ")

s = pyshorteners.Shortener()

new_link = s.tinyurl.short(link)
print(new_link)
