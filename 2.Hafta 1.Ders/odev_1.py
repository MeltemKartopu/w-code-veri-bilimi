
# • Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

pi_value = float(input("Enter the value of pi: "))
radius_value = int(input("Enter the value of radius: "))

def circle_area():
    area = pi_value * (radius_value ** 2)
    print(f"The area of the circle is: {area}")

circle_area()

# • Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. 
#   Format metodunu kullanılarak ekrana yazdırılır.

user_factorial_val = int(input("Enter a number to calculate its factorial: "))

def factorial():
  result = 1
  for i in range(1, user_factorial_val + 1): # i değişkenine 1 atadık 1 den başlayarak girilen faktöriyel değerin bir fazlasına kadar (dahil değil) i değişkeni ile çarp
    result *= i
  return result

factorial_result = factorial()
print(f"The factorial of {user_factorial_val} is: {factorial_result}")

# • Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun.

from datetime import date

def find_age():
  user_born = input("Please enter your birthdate in YYY-MM-DD format : ").split("-")
  user_born = date(int(user_born[0]), int(user_born[1]), int(user_born[2]))   # date() fonksiyonu üç parametre alır: yıl, ay ve gün.
  current_date = date.today().year   # şimdiki tarihten sadece yılı almak için
  print(f"your age is {current_date - int(user_born.year)}")

find_age()

"""
• Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim)
emekliliğine (yıl) kaldı." yanıtını versin."""

from datetime import date

def find_age():
  user_born = input("Please enter your birthdate in YYY-MM-DD format : ").split("-")
  user_born = date(int(user_born[0]), int(user_born[1]), int(user_born[2]))   # date() fonksiyonu üç parametre alır: yıl, ay ve gün.
  current_date = date.today().year   # şimdiki tarihten sadece yılı almak için
  return current_date - int(user_born.year) # yaş değerini döndürmesi için print yerine return eklendi
user_age = find_age()
print(f"your age is {user_age}")

def find_retirement_age(user_age):
    user_name = input("Please enter your name: ")
    retirement_age = 65
    if  user_age  >=  retirement_age:
        print("You are retired")
    elif user_age < retirement_age:
        print(f"There are {retirement_age - user_age} years left to be retired for {user_name}")

find_retirement_age(user_age)