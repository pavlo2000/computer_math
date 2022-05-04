s = input("Введіть рядок для пошуку паліндрому ")


            
def get_longer_palindrom(s):
    if s == s[::-1]:
        return "Рядок є паліндромом"

    for i in range(1, len(s)-1):
        for ii in range(0, i + 1):
            sub_string = s[ii:len(s) - i + ii]
            if sub_string == sub_string[::-1]:
               return "Рядок є паліндромом: " + sub_string
           
print(get_longer_palindrom(s))