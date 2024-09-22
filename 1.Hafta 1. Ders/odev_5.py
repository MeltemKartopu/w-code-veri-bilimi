"""Ödev 5"""

variable1 = "GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ"   # GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ" ifadesini bir değişkene tanımlanır.
variable2 = variable1.split(" ")   # İfadedeki her bir kelimeyi ("Gelecek Hayalim: W-Code", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
print(variable2)
variable3 = variable1.upper()  # İfadeyi hepsini büyük harf olacak hale çevrilir. ("GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ")
print(variable3)
variable4 = variable1.lower()  # İfadeyi hepsini küçük harf olacak hale çevrilir.("gelecek hayalim: w-code veri bilimi atölyesi")
print(variable4)

#0123456789  ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

numbers = "0123456789"
even_num = numbers[::2] # 0 1 2 3 .. index numarasına göre 2 şer 2 şer
print(even_num)
odd_numbers = numbers[1::2]
print(odd_numbers)  # 1. indexten başla 2 atla
