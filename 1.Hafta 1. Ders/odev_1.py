"""ödev 1"""

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