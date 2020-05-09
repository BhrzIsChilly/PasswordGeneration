import random

Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Special_Characters = "~!@#$%^&*()_"
Numbers = "1234567890"
Chosen_Characters = []
Chosen_Special_Characters = []
Chosen_Numbers = []
Password = ""
Nums_amt = 0
S_Character_amt = 0
Character_amt = 0

def Amount_of_Characters():
    num = random.randint(1, 9)
    return(num)

def Character_chooser(A_o_C, Char):
    global Chosen_Characters
    global Character_amt
    for i in range(A_o_C):
        Chosen_Characters += [random.choice(Char)]
        Character_amt += 1
    return(Chosen_Characters)

def Special_Character_chooser(A_o_C, S_Char):
    global Chosen_Special_Characters
    global S_Character_amt
    for i in range(A_o_C):
        Chosen_Special_Characters += [random.choice(S_Char)]
        S_Character_amt += 1
    return(Chosen_Special_Characters)

def Number_chooser(A_o_C, Num):
    global Chosen_Numbers
    global Nums_amt
    for i in range(A_o_C):
        Chosen_Numbers += [random.choice(Num)]
        Nums_amt += 1
    return(Chosen_Numbers)

def Assembler(A_o_C, C_c, S_C_c, N_c, Pword):    
    global Character_amt
    global S_Character_amt
    global Nums_amt
    global Total_characters
    x = 1
    y = 3
    while True:
        if Total_characters != 0:
            chooser = random.randint(x, y)
            if chooser == 1 and Character_amt > 1:
                temp_num = random.randint(0, len(C_c)-1)
                Pword += C_c[temp_num]
                C_c.pop(temp_num)
                Total_characters -= 1
                Character_amt -= 1
            elif chooser == 1 and Character_amt == 1:
                Pword += C_c[0]
                C_c.pop(0)
                Total_characters -= 1
                Character_amt -= 1
            else:
                pass
            if chooser == 2 and S_Character_amt > 1:
                temp_num = random.randint(0, len(S_C_c)-1)
                Pword += S_C_c[temp_num]
                S_C_c.pop(temp_num)
                Total_characters -= 1
                S_Character_amt -= 1
            elif chooser == 1 and S_Character_amt == 1:
                Pword += S_C_c[0]
                S_C_c.pop(0)
                Total_characters -= 1
                S_Character_amt -= 1
            else:
                pass
            if chooser == 3 and Nums_amt > 1:
                temp_num = random.randint(0, len(N_c)-1)
                Pword += N_c[temp_num]
                N_c.pop(temp_num)
                Total_characters -= 1
                Nums_amt -= 1
            elif chooser == 1 and Nums_amt == 1:
                Pword += N_c[0]
                N_c.pop(0)
                Total_characters -= 1
                Nums_amt -= 1
            else:
                pass
        else:
            break
    return(Pword)

A = Amount_of_Characters()
B = Character_chooser(Amount_of_Characters(), Characters)
C = Special_Character_chooser(Amount_of_Characters(), Special_Characters)
D = Number_chooser(Amount_of_Characters(), Numbers)
Total_characters = Nums_amt + S_Character_amt + Character_amt

print("Your password is: " + Assembler(A, B, C, D, Password))
