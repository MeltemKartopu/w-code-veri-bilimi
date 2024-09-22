#Sayılardan oluşan bir boyutlu array oluşturulur.
#Arrayi oluştururken sayıların veri tipini integer olarak belirtilir. 
#Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır. 
#İki ve üç boyutlu arrayler oluşturulur. Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır. 
#Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. 
#Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır 
#Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array **oluşturulur**. Bu arrayler satır ve sütun bazında birleştirilir. 

# indexleme yap
main_list = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

# 3 değerine ulaşmak için indexleme
print(main_list[3])

# Hi-kod değerine ulaşmak için indexleme
print(main_list[5])

#4.7 değerine ulaşmak için indexleme
print(main_list[6])

# 9,3,8.4 ve Hi-kod değerlerine ulaşmak için
print(main_list[2:6])

# 8.4, Hi-kod, "False", 4.7 değerlerine ulaşmak için slicing
print(main_list[4::])

#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.
new_list = []
for element in main_list:
  if type(element) == str:
    new_list.append(element)  # list_name.append(item)
    print(new_list)

fruits = ["kiwi","pineapple","apple", "strawberry"]
for index in range(len(fruits)):
  print("{}. indexte bulunan meyve: {}".format(index,fruits[index]))