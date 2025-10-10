import random

# Oyun Ayarları
tekrarSayisi = 0
hakSayisi = 7
baslangicSayisi = 0
bitisSayisi = 1000
rastgeleSayi = random.randrange(baslangicSayisi,bitisSayisi)
kullaniciSayisi = 0

# print("Gizli Bilgi : ",rastgeleSayi)


while tekrarSayisi<hakSayisi and kullaniciSayisi!=rastgeleSayi:
    print(baslangicSayisi," ile ", bitisSayisi, " arasında bir sayı girerek tahminde bulunun..:")
    kullaniciSayisi = int(input())
    tekrarSayisi = tekrarSayisi+1 #tekrarSayisi+=1, tekrarSayisi++

    if kullaniciSayisi==rastgeleSayi:
        print("Tebrikler sayıyı doğru tahmin ettiniz.")
        #tekrarSayisi=3
        #break

    else:
        if tekrarSayisi>=hakSayisi:
            print("Tüm haklarınız bitti sayıyı doğru tahmin edemediniz. Gerçek sayı : ",rastgeleSayi)
        else:
            if rastgeleSayi>kullaniciSayisi:
                print("Daha yüksek bir sayı giriniz.")
            else:
                print("Daha düşük bir sayı giriniz.")

            
            