# -*- coding: utf-8 -*-

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publickey = key.publickey()

class RSA():
    def __init__(self):
        self.encryptKeyword = [] # şifrelenmiş kelimelerin tutulduğu kısımdır
        self.decryptKeyword = [] # şifreden çıkarılmış kelimelerin tutulduğu kısımdır

    def KelimeleriBol(self,text):
        """RSA belirli bir kelime uzunluğu şifreleniyor.Bu yüzden bir metin verdiğimizde şifrelemensei imkansız
        Burada verilen metin boşluklarla ayrılıp list'e çeviriliyor
        """
        return text.split(" ")

    def SifreYap(self,text):
        bolunmus = self.KelimeleriBol(text) # Bölünmüş list'i al
        for i in bolunmus:  # içersinde dolaş
            enc =publickey.encrypt(i.encode("utf-8"),32) # utf-8 encode ederek şifrele
            self.encryptKeyword.append(enc) # daha sonra -> encryptKeyword ekle
        return self.encryptKeyword
    def SifreKir(self):
        for i in self.encryptKeyword: # şifrelenmiş dizi içersnde dolaş
            dec = key.decrypt(i)      # şifrelenmiş kelimeyi çıkar
            self.decryptKeyword.append(dec) # bunu ekle -> decryptKeyword
            # daha sonra bu butun diziyi al aralarına boşluk ekleyerek bir araya getir.
        return  " ".join(self.decryptKeyword).decode("UTF-8").encode("UTF-8")

