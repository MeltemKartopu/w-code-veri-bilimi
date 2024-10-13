"""ödev 1"""

# Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

# Tam sayıdan ondalıklı sayıya dönüştürme
sayi = 10
ondalikli_sayi = float(sayi)
print(ondalikli_sayi)  

# Ondalıklı sayıdan tam sayıya dönüştürme
ondalikli_sayi = 10.5
tam_sayi = int(ondalikli_sayi)
print(tam_sayi)  

# Sayıdan metne dönüştürme
sayi = 20
metin = str(sayi)
print(metin)  

# Metinden sayıya dönüştürme
metin = "30"
sayi = int(metin)
print(sayi)  

# Listeyi metne dönüştürme
liste = [1, 2, 3]
metin = str(liste)
print(metin) 

# Metni listeye dönüştürme (virgülle ayrılmış değerler)
metin = "kiraz, armut, çilek"
liste = metin.split(",")
print(liste) 