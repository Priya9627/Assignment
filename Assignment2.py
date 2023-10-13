#!/usr/bin/env python
# coding: utf-8

# In[1]:


# WAP for loop that prints the numbers from 1 to 10
for i in range(1,11):
    print(i)


# In[2]:


# Create a list of fruits(e.g.,["Apple","banana","Cherry"]) and write a for loop to print each fruit in the list
fruits=['Apple','Banana','Mango','Cherry']
for x in fruits:
    print(x)


# In[3]:


# Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

sum=0
for i in range(1,51):
    if i%2==0:
        sum=sum+i
print(sum)


# In[4]:


# Create a list of integers, and using a for loop, find and print the largest number in the list.
numbers = [23, 45, 12, 67, 89, 34, 56, 78]

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("The greatest number in the list is:", max_number)


# In[5]:


# Write a Python program that uses a for loop to find and print all the prime numbers between 1 and 100. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.
n=100
for i in range(2,n+1):
    for j in range(2,n+1):
        if i%j==0:
            break
    if i==j:
        print(i,end=",")


# In[6]:


# Write a Python program that takes a list of dictionaries, where each dictionary represents a person with keys "name" and "age." Find and print the average age of all the people in the list.

People=[{"name":"Aakash","age":29},
        {"name":"Madhu","age":28},
        {"name":"Ravi","age":27},
        {"name":"Meera","age":29}
       ]
total_age=0
count=len(People)
for person in People:
    total_age=total_age+person["age"]
if count>0:
    Average_age=total_age/count
else:
    Average_age=0
print("Average age of people:",Average_age)


# In[3]:


# Create a dictionary representing a simple inventory system for a store. Implement a function that allows you to update the quantity of items in the inventory by specifying the item name and the new quantity.

inventory = {
    'item1': 10,
    'item2': 20,
    'item3': 15,
}

def update_inventory(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print("New Uptaded Value item is: " , inventory[item_name])
    else:
        print( "item_name not found in inventory.")


update_inventory('item2', 30)  # Updated the quantity of 'item2' to 30
update_inventory('item4', 5)   # Tried to update a non-existing item

# Updated inventory after function calls

print(inventory)



# In[ ]:





# In[ ]:




