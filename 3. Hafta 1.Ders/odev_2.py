 #Sayılardan oluşan bir boyutlu array oluşturulur. Arrayi oluştururken sayıların veri tipini integer olarak belirtilir. Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır. 
 #İki ve üç boyutlu arrayler oluşturulur. Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır. 
 #Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır 
 #Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur. Bu arrayler satır ve sütun bazında birleştirilir.

import numpy as np

# 1 boyutlu array oluşturma
array_1d = [2, 3, 4, 5, 6, 7]
print("dimension: ", len(array_1d))  # arrayin boyutu
print("size: ", len(array_1d))  # arrayin eleman sayisi

# 2 boyutlu array oluşturma
array_2d = [[1, 2, 3], [4, 5, 6]]
print("dimension:", len(array_2d))
print("size:", len(array_2d) * len(array_2d[0]))
print("row:", len(array_2d))  # arrayin satır sayısı
print("column:", len(array_2d[0]))  # arrayin sütun sayısı
print("Slice of 2d array:", array_2d[1:])  # arrayin belirli bir bölümünü alma (slicing)
print("first element:", array_2d[0][0])  # indexleme
print("second element:", array_2d[0][1])


# 3 boyutlu array oluşturma
array_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("dimension:", len(array_3d))
print("size:", len(array_3d) * len(array_3d[0]) * len(array_3d[0][0]))
print("row:", len(array_3d))  # arrayin satır sayısı
print("column:", len(array_3d[0]))  # array sütun sayısı
print("Slice of 3d array:", array_3d[1:])  # slicing
print("first element:", array_3d[0][0][0])  # indexleme
print("second element:", array_3d[0][0][1])


# Numpy ile array oluşturma

# 1 boyutlu array oluşturma
numpy_array_1d = np.array([2,3,4,5,6,7], dtype = int)
print("dimension: " , numpy_array_1d.ndim)   # arrayin boyutu
print("size: ", numpy_array_1d.size)         # arrayin eleman sayisi

# 2 boyutlu array oluşturma
numpy_array_2d = np.array([[1,2,3],[4,5,6]])
print("dimension:" ,numpy_array_2d.ndim)
print("size:",numpy_array_2d.size)
print("row:",numpy_array_2d.shape[0])        # arrayin satır sayısı
print("column:",numpy_array_2d.shape[1])     # arrayin sütun sayısı
print("Slice of 2d array:" ,numpy_array_2d[1:4]) # arrayin belirli bir bölümünü alma (slicing)
print("first element:",numpy_array_2d[0,0]) # indexleme
print("second element:",numpy_array_2d[0,1])


# 3 boyutlu array oluşturma
numpy_array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("dimension:",numpy_array_3d.ndim)
print("size:",numpy_array_3d.size)
print("row:",numpy_array_3d.shape[0])    # arrayin satır sayısı
print("column:",numpy_array_3d.shape[1]) # array sütun sayısı
print("Slice of 3d array:" ,numpy_array_3d[1:4]) # slicing
print("first element:",numpy_array_3d[0,0,0]) # indexleme
print("second element:",numpy_array_3d[0,0,1])

# sıfılardan oluşan array

zeros = np.zeros((2,2))
print("zeros array:\n",zeros)

# birlerden oluşan array
ones = np.ones((2,2))
print("ones array:\n",ones)

# array birleştirme

hstack = np.hstack((zeros,ones))
print("hstack array:\n",hstack)

vstack = np.vstack((zeros,ones))
print("vstack array:\n",vstack)

