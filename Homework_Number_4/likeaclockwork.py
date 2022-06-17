import datetime
from time import strftime

now = datetime.datetime.now()
print(str(now))
string = strftime("%H:%M:%S")
print(string)
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
