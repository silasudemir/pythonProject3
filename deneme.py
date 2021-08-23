from sarki import *

print("""*********************************************************

Şarkı Programına Hoşgeldiniz...

İşlemler;

1. Şarkı Göster

2. Şarkı Sorgula

3. Şarkı Ekle

4. Şarkı Sil

Çıkmak için 'q' ya basınız :)

*********************************************************""")

sarki = Kitaplık()

while True:

    islem = input("Yapacağınız İşlem: ")

    if(islem == "q"):
        print("Program Sonlandırılııyor..........")
        print("Tekrar dinlemeyi unutma :(........ yine gel.....")
        break

    elif (islem == "1"):
        sarki.sarkilari_goster()

    elif (islem == "2"):
        adı = input("Hangi şarkıyı istersiniz ? ")
        print("Şarkılar arasından istediğiniz aranıyor..........")
        time.sleep(3)

        sarki.sarki_sorgula(adı)

    elif (islem == "3"):
        adı = input("İsim: ")
        sanatçı = input("Sanatçı: ")
        dinleyenkişi_sayısı = float(input("Dinleyen Kişi Sayısı: "))
        süresi = float(input("Süresi: "))

        yeni_sarki = Şarkı(adı,sanatçı,dinleyenkişi_sayısı,süresi)

        print("Şarkınız ekleniyor...Bu biraz sürebilir...")
        time.sleep(3)

        sarki.sarki_ekle(yeni_sarki)
        print("Şarkı başarıyla eklendi...")

    elif(islem == "4"):
        adı = input("Hangi şarkıyı listenizden çıkarmak istiyorsunuz ?")

        yanıt = input("Emin misiniz ? E/H")
        if(yanıt == "E"):
            print("Şarkı siliniyor...")
            time.sleep(3)
            sarki.şarkı_sil(adı)
            print("Şarkı başarıyla silindi...")

    else:
            print("Geçersiz işlem....")










