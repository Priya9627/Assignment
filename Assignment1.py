#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# WAP to find the greater num

num_1 = int(input("Enter the 1st number: "))
num_2 = int(input("Enter the 2nd number: "))
if num_1>num_2:
    print("num_1 is greater than num_2")
elif num_1 == num_2:
    print("they both are equal")
else:
    print("num_1 is less than num_2")
    


# In[ ]:


# WAP that asks the user for a month(1-12) and then prints the corresponding season("Spring","Summer","Fall", or "Winter")

m=int(input("Enter month number:"))
l1=[[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
if m in l1[0]:
    print("Winter")
elif m in l1[1]:
    print("Summer")
elif m in l1[2]:
    print("Fall")
elif m in l1[3]:
    print("Spring")
else:
    print("Invalid month number")



# In[ ]:


# WAP that determines whether a given year is a leap year not

year=int(input("Enter year:"))
if year % 400 ==0 :
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 ==0 :
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# In[ ]:


# WAP that takes an integer as input and checks if it's positive,negative, or zero.Print an appropriate message

num=int(input("Enter number:"))
if num<0:
    print("Negative")
elif num==0:
    print("Zero")
elif num>=0:
    print("Positive")


# In[ ]:


# WAP that asks the user for their age and gender.Based on their age and gender,print message like "You are young man" or "You are an old women"

Age=int(input("Enter Age:"))
Gender=input("Enter Gender:")
if Age<=40 and Gender=="M":
    print("You are a young man")
elif Age>40 and Gender=="F":
    print("You are an old women")



# In[ ]:


# WAP that takes a temperature in Celcius and converts it into Fahrenheit. Display the result with an appropriate message

Celcius=float(input("Enter Temp in Celcius:"))
Fahrenheit=(1.8*Celcius)+32
print("Temp in Fahrenheit:",Fahrenheit)


# In[ ]:


# WAP that calculates the shipping cost based on the weight of package. Use the following rules:
# Weight<=2 pounds:5.00- 2 pounds<Weight<=10 pounds:10.00
# Weight>10 pounds:$15

Weight=float(input("Enter weight in pounds:"))
if Weight<=2:
    print("Shipping cost is $5.00")
elif Weight>2  and Weight<=10:
    print("Shipping cost is $10.00")
elif Weight>10:
    print("Shipping cost is $15")


# In[ ]:


# WAP that asks the user for three numbers and then prints them in ascending order

num1=int(input("Enter First number : "))
num2=int(input("Enter Second number : "))
num3=int(input("Enter Third number : "))
if num1<num2 and num1<num3:
    if num2<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num3,num2
elif num2<num1 and num2<num3:
    if num1<num3:
        x,y,z=num2,num1,num3
    else:
        x,y,z=num2,num3,num1
else:
    if num1<num2:
        x,y,z=num3,num1,num2
    else:
        x,y,z=num3,num2,num1
print("Numbers in ascending order are :",x,y,z)



# In[ ]:


# WAP that checks if a given year is a "century year"(end in 00). If it's a century year check it's a leap year

year=int(input("Enter year:"))
if year%100==0:
    print("Century year")
else:
    print("Not Century year")
if year%4==0 and year%400==0:
    print("Leap year")


# In[ ]:


# WAP that asks the user for a no and then determines if it's even or odd. Print an appropriate message

n=int(input("Enter a number:"))
if n%2==0:
    print("Even")
else:
    print("Odd")

