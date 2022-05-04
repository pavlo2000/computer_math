from datetime import date
import math
import sys
import pendulum
import magic
import calendar  
import re

print("Part 1")
print( """"
Буває часом сліпну від краси
Буває, часом сліпну від краси.
Спинюсь, не тямлю, що воно за диво,—
оці степи, це небо, ці ліси,
усе так гарно, чисто, незрадливо,
усе як є — дорога, явори,
усе моє, все зветься — Україна.
Така краса, висока і нетлінна,
що хоч спинись і з Богом говори.
"""
)

print("Part 2")
print("Python version ", sys.version)

print("Part 3")
print(pendulum.now().to_datetime_string())

print("Part 4")
r = float(input("Input radius "))
print(math.pi*r*r)

print("Part 5")
name = input("Input name ")
surname = input("Input surname ")
print("{} {}".format(name, surname))

print("Part 6")
l = list()
for i in range(0, 6):
    num = input("Input number ")
    l.append(num)
print("List ", l)
print("Tuple ", tuple(l))

print("Part 7")
print(magic.from_file('/Users/pavlohladii/Documents/Study/Computer_math/Lab_1/lab_1.py'))

print("Part 8")
color_list = ["Червоний", "Зелений", "Білий", "Чорний"]
print(color_list[0], color_list[-1])

print("Part 9")
exam_st_date = (11, 12, 2014)
print("Екзамен начнеться з: ", pendulum.datetime(
    int(exam_st_date[2]), int(exam_st_date[1]), int(exam_st_date[0])).to_datetime_string())

print("Part 10")
n = input("Number ")
print(int(n) + int(n*2) + int(n*3))

# print("Part 11")
# print(help(abs))

print("Part 12")
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
print(calendar.month(yy,mm))  

print("Part 13")
print("""рядок, якого вам не уникнути
це
це ....... багаторядковий
рядок heredoc --------> приклад
""")

print("Part 14")
now = pendulum.parse("2014/07/02")
future = pendulum.parse("2014/07/11")
delta = future - now
print(delta.in_words())
print(delta.in_days(), " days")

print("Part 15")
print("Can`t understand")

print("Part 16")
num = int(input("Number "))
print( 17 - num if num < 17 else abs(17-num)*2 )

print("Part 17")
num = int(input("Number "))
print( "100>num>1000" if num in range(100, 1000) else "1000>num>2000" if num in range(1000, 2000) else "num not correct" )

print("Part 18")
num1 = int(input("Number 1 "))
num2 = int(input("Number 2 "))
num3 = int(input("Number 3 "))
if num1 + num2 == num1 + num3 and num1 + num3 == num2 + num3:
    for i in range(0, 3):
        print(num1+num2)
        
print("Part 19")
string = input("String: ")
print( string if len(string) > 0 and string[0] in ["Є", "є"] else "Is " + string )

print("Part 20")
s = input("String: ")
n = int(input("Number: "))
print(s[0:n])

print("Part 21")
user_input = input("text: ")
num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
print("number" if re.match(num_format, user_input) else "not number")

print("Part 22")
user_input = input("text: ")
print(user_input.count('4'))

print("Part 23")
s = input("text: ")
n = int(input("Number: "))
print(s[0:2]*n if len(s)>2 else s*n)

print("Part 24")
golosni = "аеєиіїоуюя"

letter = input("Input letter for reading:\n")
if letter.lower() in golosni:
    print("Golosna")
else:
    print("Prygolosna")

print("Part 25")
r = list()
n = int(input("Input list len: "))
for i in range(0, n):
    r.append(int(input("Input list len: ")))
n = int(input("Input tests number: "))
for i in range(0, n):
    t = int(input("Input list len: "))
    print("In" if t in r else "No")
