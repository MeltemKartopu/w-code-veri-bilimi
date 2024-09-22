"""
Ödev-3: Bir önceki örnek geliştirilir.


 Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
 Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
 Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
 Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder

 """
user_name = input("Please enter your username: ")
user_password = input("Please enter your password: ")
password_length = len(user_password)

while True:
  if password_length > 5 and password_length < 10:
    print("Your account is ready")
    break
  else :
    print(f"You have entered {password_length} characters. Your password must be more than 5 to less than 10 digit")
    user_password = input("Please enter your password: ")
    password_length = len(user_password)
