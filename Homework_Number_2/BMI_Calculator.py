print ("Здравствуйте! Вас представляет кульлятор индекса массы тела")
print("Давайте знакомится, как вас зовут?")
name = input()
print (name + ", " "пожалуйста, напишите ваш рост(В сантиметрах)")
height=int(input())
print (name + ", " "а сколько вы весите?(В килограммах)")
mass=int(input())
Bodymass =  mass/(height/100)**2
print (name + ", " "Ваш индекс массы тела: ", Bodymass)
check1 = Bodymass-16
check2 = 40-Bodymass
print("16","="*int(check1)+"|"+"="*int(check2) ,"40")