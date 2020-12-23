a1 = input("Lütfen ilk değeri giriniz:(String değeri 'string' şeklinde giriniz) ")
a2 = input("Lütfen ikinci değeri giriniz:(String değeri 'string' şeklinde giriniz)  ")
a3 = input("Lütfen üçüncü değeri giriniz:(String değeri 'string' şeklinde giriniz)  ")
a4 = input("Lütfen dördüncü değeri giriniz:(String değeri 'string' şeklinde giriniz)  ")
a5 = input("Lütfen beşinci değeri giriniz:(String değeri 'string' şeklinde giriniz)  ")


if type(eval(a1)) == float:
    x1='Float'
elif type(eval(a1)) == int:
    x1='Integer'
elif type(eval(a1)) == bool:
    x1='Bool'
else:
    x1='String'   

if type(eval(a2)) == float:
    x2='Float'
elif type(eval(a2)) == int:
    x2='Integer'
elif type(eval(a2)) == bool:
    x2='Bool'
else:
    x2='String' 

if type(eval(a3)) == float:
    x3='Float'
elif type(eval(a3)) == int:
    x3='Integer'
elif type(eval(a3)) == bool:
    x3='Bool'
else:
    x3='String'    

if type(eval(a4)) == float:
    x4='Float'
elif type(eval(a4)) == int:
    x4='Integer'
elif type(eval(a4)) == bool:
    x4='Bool'
else:
    x4='String'

if type(eval(a5)) == float:
    x5='Float'
elif type(eval(a5)) == int:
    x5='Integer'
elif type(eval(a5)) == bool:
    x5='Bool'
else:
    x5='String'
   

print("Girdiğiniz ilk değer {} ve tipi {}".format(a1,x1))
print("Girdiğiniz ikinci değer {} ve tipi {}".format(a2,x2))
print("Girdiğiniz üçüncü değer {} ve tipi {}".format(a3,x3))
print("Girdiğiniz dördüncü değer {} ve tipi {}".format(a4,x4))
print("Girdiğiniz beşinci değer {} ve tipi {}".format(a5,x5))

