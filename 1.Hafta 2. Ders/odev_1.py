"""
Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;


 10000 ve altındaysa maaşından %5 kesinti olur.
 25000 ve altındaysa maaşından %10 kesinti olur.
 45000 ve altındaysa maaşından %25 kesinti olur.
 Diğer koşullarda %30 kesinti olur.

Bu durumlara göre kullanıcının yeni maaşı yazdırılır.
"""

user_salary = input("Please enter your monthly salary: ")
user_salary = int(user_salary)

if user_salary < 10000:
  print(user_salary - (user_salary * 0.05))
elif user_salary <= 25000:
  print(user_salary - (user_salary * 0.10))
elif user_salary <= 45000:
  print(user_salary - (user_salary * 0.25))
else:
  print(user_salary - (user_salary * 0.30))