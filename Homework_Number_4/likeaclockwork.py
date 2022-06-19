import datetime
from time import strftime

TRN = datetime.datetime.now()
print(str(TRN))
string = strftime("%H:%M:%S")
print(string)

hours,minutes,seconds = string.split(":")
print(hours)
print(minutes)
print(seconds)




zero = { 0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_zero in zero.values():
    print(value_zero)

one = { 0:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_one in one.values():    
    print (value_one)

two = {  0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_two in two.values():
    print(value_two)

three= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_three in three.values():    
    print (value_three)

four= { 0:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" )}
for value_four in four.values():    
    print (value_four)    

five= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
        2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
        3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
        4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        5:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
        6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_five in five.values():    
    print (value_five)

six = {  0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_six in six.values():
    print(value_six)

seven= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" )}
for value_seven in seven.values():    
    print (value_seven)

eight= { 0:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5:  ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6:  ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_eight in eight.values():    
    print(value_eight)

nine = { 0: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         1: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         2: ("\u2B1B" "\u2B1C" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         3: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" ),
         4: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         5: ("\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1B" "\u2B1C" "\u2B1B" ),
         6: ("\u2B1B" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1C" "\u2B1B" )}
for value_nine in nine.values():
    print(value_nine)

sep_one = { 0: ("\u2B1B" "\u2B1B" "\u2B1B"),
            1: ("\u2B1B" "\u2B1C" "\u2B1B"),
            2: ("\u2B1B" "\u2B1C" "\u2B1B"),
            3: ("\u2B1B" "\u2B1B" "\u2B1B"),
            4: ("\u2B1B" "\u2B1C" "\u2B1B"),
            5: ("\u2B1B" "\u2B1C" "\u2B1B"),
            6: ("\u2B1B" "\u2B1B" "\u2B1B")}
for value_sep_one in sep_one.values():
    print(value_sep_one)

sep_two = { 0: ("\u2B1B" "\u2B1B" "\u2B1B"),
            1: ("\u2B1B" "\u2B1B" "\u2B1B"),
            2: ("\u2B1B" "\u2B1B" "\u2B1B"),
            3: ("\u2B1B" "\u2B1B" "\u2B1B"),
            4: ("\u2B1B" "\u2B1B" "\u2B1B"),
            5: ("\u2B1B" "\u2B1B" "\u2B1B"),
            6: ("\u2B1B" "\u2B1B" "\u2B1B")}
for value_sep_two in sep_two.values():
    print(value_sep_two)

print(list(string))
x1=list(string)
x2=x1[0]
x3=x1[1]
x4=x1[2]
x5=x1[3]
x6=x1[4]
x7=x1[5]
x8=x1[6]
x9=x1[7]
z2=int(x2)
z3=int(x3)
z5=int(x5)
z6=int(x6)
z8=int(x8)
z9=int(x9)


print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)
print(x8)
print(x9)




if z2==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z2==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z2==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])

if z3==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z3==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z3==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
elif z3==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
elif z3==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
elif z3==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
elif z3==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
elif z3==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
elif z3==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
elif z3==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])

if z5==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z5==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z5==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
elif z5==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
elif z5==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
elif z5==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
elif z5==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
elif z5==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
elif z5==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
elif z5==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])

if z6==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z6==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z6==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
elif z6==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
elif z6==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
elif z6==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
elif z6==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
elif z6==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
elif z6==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
elif z6==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])

if z8==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z8==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z8==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
elif z8==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
elif z8==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
elif z8==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
elif z8==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
elif z8==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
elif z8==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
elif z8==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])

if z9==0:
        print(zero[0])
        print(zero[1])
        print(zero[2])
        print(zero[3])
        print(zero[4])
        print(zero[5])
        print(zero[6])
elif z9==1:
        print(one[0])
        print(one[1])
        print(one[2])
        print(one[3])
        print(one[4])
        print(one[5])
        print(one[6])
elif z9==2:
        print(two[0])
        print(two[1])
        print(two[2])
        print(two[3])
        print(two[4])
        print(two[5])
        print(two[6])
elif z9==3:
        print(three[0])
        print(three[1])
        print(three[2])
        print(three[3])
        print(three[4])
        print(three[5])
        print(three[6])
elif z9==4:
        print(four[0])
        print(four[1])
        print(four[2])
        print(four[3])
        print(four[4])
        print(four[5])
        print(four[6])
elif z9==5:
        print(five[0])
        print(five[1])
        print(five[2])
        print(five[3])
        print(five[4])
        print(five[5])
        print(five[6])
elif z9==6:
        print(six[0])
        print(six[1])
        print(six[2])
        print(six[3])
        print(six[4])
        print(six[5])
        print(six[6])
elif z9==7:
        print(seven[0])
        print(seven[1])
        print(seven[2])
        print(seven[3])
        print(seven[4])
        print(seven[5])
        print(seven[6])
elif z9==8:
        print(eight[0])
        print(eight[1])
        print(eight[2])
        print(eight[3])
        print(eight[4])
        print(eight[5])
        print(eight[6])
elif z9==9:
        print(nine[0])
        print(nine[1])
        print(nine[2])
        print(nine[3])
        print(nine[4])
        print(nine[5])
        print(nine[6])
    
#Я Пытался сделать и через функции и через гену, и склеить как то.... кароч..  Я - Чайник.
#Буду благодарен Вам, если после отчитки, скините готовую, чтоб посмотреть что там и как там)))....
#Заранее спасибо)