#adders.py by Miles Burne 7/10/19

#creates the class to hold the adder
class Adder():
    #init, class takes a and b as integers of 1 or 0.
    def __init__(self):
        pass

    #creating an XOR gate for the adders
    def XOR(self,a,b):
        c = a+b
        if c == 1: #only 1 input must be 1
            return(1)
        else:
            return(0)

    #creates AND gate for adders
    def AND(self,a,b):
        c = a+b
        if c == 2: #if both a and b are 1 
            return(1)
        else:
            return(0)

    #creates OR gate for adders
    def OR(self,a,b):
        c = a+b #or gate requires at least 1 to be true(1)
        if c != 0:
            return(1)
        else: #if none are 1
            return(0)
        
    #creating a half adder
    def half_adder(self,a,b):
        sum_0 = self.XOR(a,b) #finds sum
        carry_0 = self.AND(a,b) #finds carry
        return(sum_0, carry_0)

    #creates a full adder
    def full_adder(self,a,b,carry_in):
        sum_1, carry_1 = self.half_adder(a,b) #finds first output of half adder
        sum_out, carry_2 = self.half_adder(sum_1, carry_in) #finds final output of  half adder
        carry_out = self.OR(carry_1,carry_2)
        return(sum_out, carry_out)

#class to string together the adders, reliant on Adder class
class Adder_String():
    #init
    def __init__(self):
        self.adder = Adder()
        self.cur_carry = 0 #holds the value of the next carry
        self.cur_sum = [] #holds the value of the sums
        self.first_use = True #used for the first use of a new sum

    #called to add sum to sumlist
    def add_sum(self,a):
        self.cur_sum.insert(0,a) #adds to 0th position as binary displayed from right to left
        
    #executed if this is the first added value of a new sum
    def first_sum(self,a,b):
        got_sum, self.cur_carry = self.adder.half_adder(a,b)
        self.add_sum(str(got_sum))
        self.first_use = False
        
    #class to add new values
    def add_value(self,a,b):
        #checks if this is the first added value
        if self.first_use == True:
            self.first_sum(a,b)
        else: #otherwise full adder to be used
            got_sum, self.cur_carry = self.adder.full_adder(a,b,self.cur_carry)
            self.add_sum(str(got_sum))

    #returns final binary number
    def get_final(self):
        self.cur_sum.insert(0, str(self.cur_carry))
        return(self.cur_sum)

    #ends the current sum and returns value
    def end_sum(self):
        return_array = self.cur_sum.insert(0, self.cur_carry)
        #reseting values
        self.cur_sum = []
        self.cur_carry = 0
        self.first_use = True
        return(return_array)


#defines the format for printing the output array
def print_format(array):
    output = "".join(array)
    print("carry:",output[0],"out:",output[1:]) #uses indicies to select what to show
    
#function to add two binary numbers (taken as strings), A and B MUST be same length
def add_binary(a,b):
    #creates instance of Adder_String
    adders = Adder_String()
    #creates two new lists from strings
    a_values = list(a)
    b_values = list(b)
    for x in range(1, len(a_values)+1):
        length = len(a_values) #used to iterate through array backwards
        a_val = a_values[length-x]
        b_val = b_values[length-x] 
        adders.add_value(int(a_val),int(b_val))
    print(a,"+",b,"=")
    print_format(adders.get_final())
    adders.end_sum()

#takes user input for the program
def user_input():
    number_a = input("a: ")
    number_b = input("b: ")
    end = input("enter 1 to end: ")
    if end != 1:
        end = 0
    return(number_a, number_b,end)
if __name__ == "__main__":
    end = 0 #for while loop
    print("Please enter only numbers 1 and 0, and ensure they are in direct order, and the same length. Example: '0101'")
    while end == 0:
        a,b,end = user_input()
        print()
        add_binary(a,b)
        print()

    
