# darslarim
python
Rekursiya
Rekursiya - bu funksiya o'zini chaqirganda.
Rekursiya keng tarqalgan matematik va dasturlash tushunchasidir. Bu funksiya o'zini o'zi chaqirishini anglatadi. Buning afzalligi shundaki, siz natijaga erishish uchun ma'lumotlarni sikl bilan ko'rib chiqishingiz mumkin.

Dasturchi rekursiya bilan juda ehtiyot bo'lishi kerak, chunki hech qachon tugamaydigan yoki ortiqcha xotira yoki protsessor quvvatidan foydalanadigan funksiyani yozishga o'tish juda oson bo'lishi mumkin. Biroq, to'g'ri yozilganda, rekursiya dasturlash uchun juda samarali va matematik jihatdan oqlangan yondashuv bo'lishi mumkin.

MisolO'zingizning Python serveringizni oling
5 dan pastga qarab sanaydigan oddiy rekursiv funksiya:
1
def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)g
    countdown(n - 1):

countdown(5)
Bazaviy holat va rekursiv holat
Har bir rekursiv funksiya ikkita qismdan iborat bo'lishi kerak:

Bazaviy holat - Rekursiyani to'xtatadigan shart
Rekursiv holat - o'zgartirilgan argument bilan o'zini chaqiradigan funksiya
Bazaviy holat bo'lmasa, funksiya o'zini abadiy chaqiradi va bu stekning toshib ketishi xatosiga olib keladi.

Misol
Bazaviy holat va rekursiv holatni aniqlash:

def factorial(n)
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))
Bazaviy holat juda muhim. Rekursiv funksiyangiz oxir-oqibat bajariladigan shartga ega ekanligiga doimo ishonch hosil qiling.


REKLAMALARNI OLIB TASHLASH

Fibonachchi ketma-ketligi
Fibonachchi ketma-ketligi klassik misol bo'lib, unda har bir son oldingi ikkitasining yig'indisidir. Ketma-ketlik 0 va 1 dan boshlanadi:

0, 1, 1, 2, 3, 5, 8, 13, ...

Ketma-ketlik cheksiz davom etadi, har bir son oldingi ikkitasining yig'indisi bo'ladi.

Ketma-ketlikdagi ma'lum bir sonni topish uchun rekursiyadan foydalanishimiz mumkin:

Misol
Fibonachchi ketma-ketligidagi 7-sonni toping:

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
Ro'yxatlar bilan rekursiya
Rekursiya bir vaqtning o'zida bitta elementni qayta ishlash orqali ro'yxatlarni qayta ishlash uchun ishlatilishi mumkin:

Misol
Ro'yxatdagi barcha elementlarning yig'indisini hisoblang:

def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
Misol
Ro'yxatdagi maksimal qiymatni toping:

def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

REKLAMALARNI OLIB TASHLASH

Rekursiya chuqurligi chegarasi
Pythonda rekursiyaning qanchalik chuqur bo'lishi mumkinligi bo'yicha cheklov mavjud. Standart cheklov odatda 1000 ta rekursiv chaqiruvlar atrofida bo'ladi.

Misol
Rekursiya chegarasini tekshiring:

import sys
print(sys.getrecursionlimit())
Agar sizga chuqurroq rekursiya kerak bo'lsa, limitni oshirishingiz mumkin, ammo ehtiyot bo'ling, chunki bu ishdan chiqishga olib kelishi mumkin:

Misol
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
