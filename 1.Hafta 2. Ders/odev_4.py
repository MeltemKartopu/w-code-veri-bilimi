""" 

Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
Tercihe göre kalan hak bilgisi verilir. """

user_name2 = input("Please enter your name: ")
user_password2 = int(input("Please enter your password: "))
password = 140396
user_entrance_right = 0

while user_entrance_right < 3:
    if user_password2 == password:
        print("Access is successful")
        break
    else:
        print("Access Denied, please try again")
        user_entrance_right += 1
        if user_entrance_right == 3:
            print("You have exceeded the number of attempts")
            break
        else:
            print(f"You have {3 - user_entrance_right} attempts left")
            user_password2 = input("Please enter your password: ")
