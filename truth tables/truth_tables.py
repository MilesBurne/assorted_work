#truth_tables by miles burne 8/10/19

#class for the truth tables
class TruthTable():
    #init
    def __init__(self):
        pass
    
    #creating an XOR gate
    def XOR(self,a,b):
        c = a+b
        if c == 1: #only 1 input must be 1
            return(1)
        else:
            return(0)

    #creates AND gate
    def AND(self,a,b):
        c = a+b
        if c == 2: #if both a and b are 1 
            return(1)
        else:
            return(0)

    #creates OR gate
    def OR(self,a,b):
        c = a+b #or gate requires at least 1 to be true(1)
        if c != 0:
            return(1)
        else: #if none are 1
            return(0)

    #creates NOT gate
    def NOT(self,a):
        #if value is 1 
        if a == 1:
            return(0)
        else:
            return(1)

    #creates NAND
    def NAND(self,a,b):
        #NAND is just NOT and AND
        AND = self.AND(a,b)
        NOT = self.NOT(AND)
        return(NOT)
    
    #creates NOR
    def NOR(self,a,b):
        #NOR is just NOT and OR
        OR = self.OR(a,b)
        NOT = self.NOT(OR)
        return(NOT)

#prints when 1 var
def print_format_1(a,c,first):
    #need to print column names for table
    if first==True:
        print("A |=| C")
    print(a+" |=| "+c) 

#prints when 2 var              
def print_format_2(a,b,c,first):
    #need to print column names for table
    if first==True:
        print("A | B |=| C")
    print(a+" | "+b+" |=| "+c)
    
def main():
    table = TruthTable()
    array1 = ["0","1"]
    array2 = ["00","01","10","11"]
    for x in array2:
        numb = list(x)
        a = int(numb[0])
        b = int(numb[1])
        c = table.NOR(a,b) #change table here
        if array2.index(x) == 0:
            first = True
        else:
            first = False
        print_format_2(str(a),str(b),str(c),first)

if __name__ == "__main__":
    main()
