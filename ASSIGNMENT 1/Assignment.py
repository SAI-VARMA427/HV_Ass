#Question 1 :

number1=float(input("enter the value of Number1: "))
number2=float(input("enter the value of Number2: "))
number3=float(input("enter the value of Number3: "))
number4=float(input("enter the value of Number4: "))
number5=float(input("enter the value of Number5: "))
Sum=number1+number2+number3+number4+number5
if number1 < 0 or number2<0 or number3<0 or number4<0 or number5<0 :
    print("enter a positive nuumber")
else:
    print("The sum of all numbers is : ",Sum)
x=open("data.txt","a")
print("the value of number1:",number1,file=x)
print("the value of number2:",number2,file=x)
print("the value of number3:",number3,file=x)
print("the value of number4:",number4,file=x)
print("the value of number5:",number5,file=x)
print("the values of all numbers: ",Sum,file=x)



#Question 2:


Cars={}
name = input("enter a brandname: ")
color = input("enter the color: ")
Cars[name] = color
x=open("data.txt","a")
print("the details: ",Cars,file=x)
print(Cars)