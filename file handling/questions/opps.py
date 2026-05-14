"""class Car:
    def accelerate(self):  # self is used to represent the instance of class and used to access the method\function of class and also the attribute of the class
        print("car is accelerating")
c1 = Car()
c1.accelerate() """  # class is nothing but template or blueprint for making an object


"""class Car:
    def accelerate(self):
        print("car is accelerating")
    def brake(self):
        print("car is stoping")   
c1 = Car()
c1.brake()   
c2 = Car()
c2.accelerate()  """



'''class Bank:
    def deposit(self,amount):
        print("deposit a money")
    def withdraw(self,withdraw_money):
        print("withdraw a money")
c1 = Bank()
c1.deposit(4000)
c2 = Bank()  

c2.withdraw(2500)'''






class List_operation():
    l = [1,2,3,4,5,6,7,8,9]
    def extract_even(self,l):
        l1 = []
        for i in l:
            if i % 2 == 0:
                l1.append(i)
        return l1
    def extract_odd(self,l):
        l1 = []
        for i in l:
            if i % 2 != 0:
                l1.append(i)
        return l1 
oper1 = List_operation()
print(oper1.l)  # give complete given list
print(oper1.extract_even(oper1.l))  
print(oper1.extract_odd(oper1.l))                       
