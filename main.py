import random

harfler = "_-*1234567890öçşüğqwertyuopasdfghjklizxcvbnmÖÇŞÜĞQWERTYUOPASDFGHJKLIZXCVBNM"
while True:
    sifre = ""
    asd = int(input("kaç harfli olcak şifren?"))
    for i in range(asd):
        sifre += random.choice(harfler)
        
    print(sifre)
