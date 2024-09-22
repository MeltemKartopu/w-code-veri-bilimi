# Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır,
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)

user_name = input("Please enter your username: ")
user_password = input("Please enter your password: ")
password_length = len(user_password)

if password_length == 6:
    print("Your account is ready to use")
elif password_length < 6:
    print("Your password must be 6 digit or more ")
else :
    print("Your password must be 6 digit or less")
    user_password = input("Please enter your password: ")