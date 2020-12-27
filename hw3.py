import random
 
selamlama = input("What is your name? ")
 
print("Welcome ", selamlama)
 
kelimeler = ['araba', 'direksiyon'] 
 
kelime = random.choice(kelimeler)
  
print("Başlıyoruz...")
 
tahminler = ''
 

hakAdet = 10
 
 
while hakAdet > 0:
 
    hataSayi = 0
     
    for char1 in kelime: 

        if char1 in tahminler: 
            print(char1)
             
        else: 
            print("_")

            hataSayi += 1
             
 
    if hataSayi == 0:
        print("Kazandın!") 
         
        print("Kelime: ", kelime) 
        break
    tahmin = input("Bir kelime giriniz: ")
     
    tahminler += tahmin 
     
    if tahmin not in kelime:
         
        hakAdet -= 1
        
        print("Hatalı")
         
        print("Kalan hakkın ", + hakAdet)
                 
        if hakAdet == 0:
            print("Kaybettin!")