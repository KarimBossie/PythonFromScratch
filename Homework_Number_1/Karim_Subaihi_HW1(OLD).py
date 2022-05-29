#Question #1: Counting symbols in a sentence
text1 = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
text2 = "Количество символов -"
print (text2, len(text1))

#Question #2: Reverse the sentence
print (text1[::-1])

#Question #3: Titling
print (text1.title())

#Question #4: Upper cases
print (text1.title().swapcase().upper())

#Question 5: Find various letters
v1 = "нд"
v2 = "ам"
v3 = "о"
c1 = text1.count(v1)
c2 = text1.count(v2)
c3 = text1.count(v3)
print("нд =",c1,"ам =", c2,"о =", c3)

#Question 6: Own things
print (text1[0:3])
print (text1[3:6])
print (text1[6:9])
print (text1[9:12])

#Question 7: Initial string
print (text1)
aa