
M = ['magical unicorns',19,'hello',98.98,'world']

I = [2,3,1,7,4,12]

S = ['magical','unicorns']


#test cases loaded above
#function defined below
def listmustest(x): 
    i = 0
    tot = 0
    kindi = 0
    kindf = 0
    kinds = 0
    trick = 0
    types = 0
    NewStr = ""
    #initializing vaariables above
    while i < len(x):               #iterating through the list
        if type(x[i]) == int or type(x[i]) == float:  #catching both int and float types
            tot += x[i]             #building the sum
        if type(x[i]) == int:       #logging int type
            kindi += 1
            if kindi > 1:           #preventing multiple int calculating as >1 type
                kindi = 1
        if type(x[i]) == float:     #logging float type
            kindf += 1
            if kindf > 1:           #preventing multiple floats calculating as >1 type
                kindf = 1
        if type(x[i]) == str:       #checking for string type
            NewStr = NewStr + ' ' + x[i]        #building NewString
            kinds += 1              #logging string type
            if kinds > 1:           #preventing multiple strings calculating as >1 type
                kinds = 1
        if type (x[i]) != str and type (x[i]) != float and type (x[i]) != int:
            trick += 1
        i += 1
    types = kinds + kindf + kindi   #calculating number of types present
    if types > 1 :                  # determining if string is mixed types
        print "The list you entered is of mixed types."
    elif types == 1 and kindi == 1 : # checking if type int is the only type
        print "The list you entered is of Integer type."
    elif types == 1 and kindf == 1 : #checking if type float is the only type
        print "The list you entered is of Float type"
    elif types == 1 and kinds == 1 : #checking if type string is the only type
        print "The list you entered is of String type"
    else :                                  
        print "Tricky tricky!"
        if trick > 1:
            print "You tried to sneak ", trick, "past me!"
    if tot != 0 or kindi == 1 or kindf == 1 :
        print "Sum:", tot
    if kinds == 1:
        print "String:", NewStr
    if kindf == 1:
        print "Thought you could fool me with a float? Nope!"
        
listmustest(M)  #calls the function

'''
expected output for testcase M:
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

expected output for testcase I:
"The list you entered is of integer type"
"Sum: 29"

expected output for testcase S:
"The list you entered is of string type"
"String: magical unicorns"
'''