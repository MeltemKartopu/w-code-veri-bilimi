import pandas as pd 

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],


  "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],


"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

# sözlüğü dataframe'e dönüştürme 
sozluk_df = pd.DataFrame(sozluk)
sozluk_df
# 2.indexte bulunan kategori.(Sadece kategori bilgisi) 
sozluk_df.iloc[2,0] # index numarası ve sütun indexi ile erişim
# 2.indexte bulunan ürün.(Sadece ürün bilgisi)
sozluk_df.iloc[2,1]
# 4.indexten 9.indexe kadar olan veriler. (Kategori,ürün,fiyat bilgisi beraber) 
sozluk_df.iloc[4:9]
#1.indexten 6.indexe kadar olan ürünler. (Sadece ürün bilgisi) 
sozluk_df.iloc[0:7,1:2]    


#giyim kategorisinde bulunan ürünler gösterilir.  
kategori_giyim = sozluk_df.loc[sozluk_df["Kategori"] == "Giyim", ["Ürün"]]
print(kategori_giyim)
# Ayakkabı kategorisinde bulunan ürünler gösterilir. 
kategori_ayakkabı = sozluk_df.loc[sozluk_df["Kategori"] == "Ayakkabı", ["Ürün"]]
print(kategori_ayakkabı)
# Aksesuar kategorisinde bulunan ürünler gösterilir. 
kategori_aksesuar = sozluk_df.loc[sozluk_df["Kategori"] == "Aksesuar", ["Ürün"]]
print(kategori_aksesuar)

# giyim kategorisinde fiyatı 300'den fazla ürünler gösterilir.  
kategori_giyim = sozluk_df.loc[(sozluk_df["Kategori"] == "Giyim") & (sozluk_df["Fiyat"] > 300)]
# Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir. 
kategori_ayakkabı = sozluk_df.loc[(sozluk_df["Kategori"] == "Ayakkabı") & (sozluk_df["Fiyat"] < 600)]
print(kategori_ayakkabı)
# Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir. 
kategori_aksesuar = sozluk_df.loc[(sozluk_df["Kategori"] == "Aksesuar") & (sozluk_df["Fiyat"] > 100)]
print(kategori_aksesuar)