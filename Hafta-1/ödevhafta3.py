# -*- coding: utf-8 -*-

Hafta 3

ödev 1
"""

# prompt: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

# Tam sayıdan ondalıklı sayıya dönüştürme
sayi = 10
ondalikli_sayi = float(sayi)
print(ondalikli_sayi)  # Çıktı: 10.0

# Ondalıklı sayıdan tam sayıya dönüştürme
ondalikli_sayi = 10.5
tam_sayi = int(ondalikli_sayi)
print(tam_sayi)  # Çıktı: 10

# Sayıdan metne dönüştürme
sayi = 25
metin = str(sayi)
print(metin)  # Çıktı: "25"

# Metinden sayıya dönüştürme
metin = "30"
sayi = int(metin)
print(sayi)  # Çıktı: 30

# Listeyi metne dönüştürme
liste = [1, 2, 3]
metin = str(liste)
print(metin) # Çıktı: "[1, 2, 3]"

# Metni listeye dönüştürme (virgülle ayrılmış değerler)
metin = "elma,armut,muz"
liste = metin.split(",")
print(liste) # Çıktı: ['elma', 'armut', 'muz']

"""Ödev 2"""

#  İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.
ali = 23
Veli = 45
Ayşe = 12

print(ali > Veli)
print(ali < Veli)
print(ali == Veli)
print(ali != Veli)
print(ali >= Veli)
print(ali <= Veli)

"""Ödev 3"""

#Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.

ask_user1 = input("Please enter first value: ")
ask_user2 = input("Please enter second value: ")

print("Addition: ", int(ask_user1) + int(ask_user2))
print("Subtraction: ", int(ask_user1) - int(ask_user2))
print("Multiplication: ", int(ask_user1) * int(ask_user2))

"""Ödev 4"""

# Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.

user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")
user_city = input("Please enter your city: ")
user_job = input("Please enter your job: ")
print(f"My name is {user_name}, and my age is: {user_age}, I live in {user_city} Im a {user_job}")

"""Ödev 5"""

degisken1 = "GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ"   # GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ" ifadesini bir değişkene tanımlanır.
degisken2 = degisken1.split(" ")   # İfadedeki her bir kelimeyi ("Gelecek Hayalim: W-Code", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
print(degisken2)
degisken3 = degisken1.upper()  # İfadeyi hepsini büyük harf olacak hale çevrilir. ("GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ")
print(degisken3)
degisken4 = degisken1.lower()  # İfadeyi hepsini küçük harf olacak hale çevrilir.("gelecek hayalim: w-code veri bilimi atölyesi")
print(degisken4)

#0123456789  ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

sayilar = "0123456789"
cift_sayilar = sayilar[::2] # 0 1 2 3 .. index numarasına göre 2 şer 2 şer
print(cift_sayilar)
tek_sayilar = sayilar[1::2]
print(tek_sayilar)  # 1. indexten başla 2 atla
