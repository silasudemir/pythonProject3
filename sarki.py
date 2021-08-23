import sqlite3

import time

class Şarkı():

    def __init__(self,adı,sanatçı,dinleyenkişi_sayısı,süresi):

        self.adı = adı
        self.sanatçı = sanatçı
        self.dinleyenkişi_sayısı = dinleyenkişi_sayısı
        self.süresi = süresi

    def __str__(self):

        return "Şarkı Adı: {}\nSanatçı: {}\nDinlenme Sayısı: {}\nSüresi: {}\n".format(self.adı,self.sanatçı,self.dinleyenkişi_sayısı,self.süresi)

class Kitaplık():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarki.db")

        self.cursor = self.baglanti.cursor()

        sor = "Create Table If not exists şarkılar (adı TEXT,sanatçı TEXT,dinleyenkişi_sayısı INT,süresi INT )"

        self.cursor.execute(sor)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilari_goster(self):

        sor = "Select * From şarkılar"

        self.cursor.execute(sor)

        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Şarkı Bulunmuyor...")

        else:
            for i in şarkılar:
                şarkı = Şarkı(i[0],i[1],i[2],i[3])
                print(şarkı)

    def sarki_sorgula(self,adı):

        sor = "Select * From şarkılar where adı = ? "

        self.cursor.execute(sor,(adı,))

        şarkılar = self.cursor.fetchall()

        if (len(şarkılar) == 0):
            print("Böyle bir şarkı kitaplıkta bulunmuyor....")

        else:
            şarkı = Şarkı(şarkılar[0][0],şarkılar[0][1],şarkılar[0][2],şarkılar[0][3])

            print(şarkı)

    def sarki_ekle(self,şarkı):

        sor = "Insert into şarkılar Values(?,?,?,?)"

        self.cursor.execute(sor,(şarkı.adı,şarkı.sanatçı,şarkı.dinleyenkişi_sayısı,şarkı.süresi))

        self.baglanti.commit()

    def şarkı_sil(self,adı):

        sor = "Delete From şarkılar where adı = ?"

        self.cursor.execute(sor,(adı,))

        self.baglanti.commit()







