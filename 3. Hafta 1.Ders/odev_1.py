# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, 
# Fizik, Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.
# Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.

dictionary = {"Arzu": "Matematik", "Heidi": "Fizik", "Ahmet": "Kimya"}

while True:

  choice = input("""Please choose related numbers for your processes  , choose number 2 for class query ,
  choose number 3 for adding new value to dictionary , choose number 4 to change value in the dictionary, choose 5 for exit """ )
  if choice == "1":       # isimden sınıf sorgusu yapmak için choose number 1 for name query
    print("Please enter name to find related class")
    ask_name = input("Please enter your name: ")
    if ask_name in dictionary:
      print(ask_name, "student's class is", dictionary[ask_name])
    else:
      print("Name not found, please enter valid name")

  elif choice == "2":  # sınıftan isim sorgusu yapmak için
    print("Please enter class to find related names")
    ask_class = input("Please enter your class name: ")
    print("Students in", ask_class, "class are: ")
    if ask_class in dictionary.values():
      for name, subject in dictionary.items():
        if subject == ask_class:
          print(name)
  elif choice == "3":  # yeni değer eklemek için
    ask_new = print("Please enter your new value: ")
    ask_new_name = input("Please enter your new name: ")
    ask_new_class = input("Please enter your new class: ")
    dictionary[ask_new_name] = ask_new_class  # yeni isim key olarak,  sınıf ise değeri olarak
    print(dictionary)
  elif choice == "4":  # değer değiştirmek için
    change_val = input("Please enter your name to change value: ")
    if change_val in dictionary:
      new_val = input("Please enter new value: ")
      dictionary[change_val] = new_val
      print(dictionary)
      print("Value changed successfully")
    else:
      print("Name not found, please enter valid name")
  elif choice == "5":
    print("Thank you for using our program")
    break
  else:
    print("Please enter valid choice")



