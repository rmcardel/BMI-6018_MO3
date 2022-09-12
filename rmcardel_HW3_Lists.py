#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""BMI 6018 Fall 2022 

Instructions: For this assignment, please return all answers as variables in your
.py file. You will quickly note that you will need to find answers outside the
class lectures. This is not an accident! You will need to become professionally
comfortable with looking things up via the python docs and google. 

Ensure that all variables are labelled according to the example. IE the answer
to problem 1 part c should be labelled one_c. While all questions are answerable
with a single line of code, you are free to use helper variables so long as they
are helpfully/informatively named. 

I should be able to open your .py file and run it without errors. I will **not** be 
debugging your code for you. If your file does not run, it will **not** be graded. 
If you are unsure if your file will run, open up a chpc terminal and test it there.

For this assignment, please only use base python files types. That is: there 
should be no import calls in your file save my use of sys at the end.

Example Problem

0.a Create a list of strings
0.b Using a str method, capitalize one of the elements in the list using a slice
0.c Coerce one character of the list to display as a hex

zero_a = ['first','second','third','fourth','fifth']
zero_b = zero_a[1].upper()
zero_c = hex(ord(zero_a[1][1]))

"""

#Start your assignment here
print("Assignment 3")


# ## Problem 1: Lists, Sets and Coersion

# In[1]:


#1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = list(range(0,10))
print(one_a)


# In[3]:


#1.b Add 3 to the 5th indexed element
# https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/
one_b = one_a.copy()
one_b.insert(5, 3)
print(one_b)

# Umang told me in the discussion "It means add the number 3 to the list at the 5th index"


# In[4]:


#1.c Coerce all elements in the list to floats using list comprehension
# https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
one_c = [float(i) for i in one_b]
print(one_c)


# In[5]:


#1.d Coerce the list to a set
one_d = set(one_c)
print(one_d)


# In[7]:


#1.e Using a method, append int 10 to the set
one_e = one_d.copy()
one_e.add(int(10))
print(one_e)


# In[8]:


#1.f Using a method, pop an item from the set
one_f = one_e.copy()
one_f.pop()
print(one_f)


# In[9]:


#1.g Using a length counting function, count the number of items in the set
one_g = one_f.copy()
print(len(one_g))


# In[10]:


#1.h Check if the number of items in the set is the same as the number of items in the list
# https://www.pythonforbeginners.com/basics/compare-two-lists-in-python
def compare(one_g, one_c):
    if len(one_g) != len(one_c):
        return False
    else:
        return True

print("one_h: The set and the list contain the same number of elements:",compare(one_g, one_c))


# In[11]:


#1.i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
one_i = one_a + list(one_g)
print(one_i)


# In[12]:


#1.j Coerce 1.i to a set
one_j = set(one_i)
print(one_j)


# In[13]:


#1.k Count the number of elements in the 1.j
one_k = len(one_j)
print(one_k)


# ## Problem 2: Dictionary woes

# In[14]:


#2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named 
#  two_a, ensure the key names are the same as the dictionary names.
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

two_a = {
    "two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango" : two_patient_dictionary_dango,
    "two_patient_dictionary_mochi" : two_patient_dictionary_mochi
}
print(two_a)


# In[18]:


#2.b Using keys, retrieve the Dango's name from 2.a
two_b = two_patient_dictionary_dango["name"]
print(two_b)

#or

two_b = two_patient_dictionary_dango.get("name")
print(two_b)


# In[19]:


#2.c Using keys, update the value of Mochi's year to 2018. This should not be a variable and should simply update 2.a.
two_patient_dictionary_mochi["year"] = 2018
print(two_a)


# In[20]:


#2.d Manually create a dictionary that has a single level and contains each patient as the key and the year as the value. Set 
# Mochi's year to 2019.
two_d = {
  "Kinoko" : "2021",
  "Dango" : "2019",
  "Mochi" : "2019"
}
print(two_d)


# In[21]:


#2.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print(two_e)


# In[22]:


#2.f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print(two_f)


# In[23]:


#2.g Use the zip function to combine 2.e and 2.f into a dictionary again
# https://stackoverflow.com/questions/209840/how-can-i-make-a-dictionary-from-separate-lists-of-keys-and-values
two_g = dict(zip(two_e, two_f))
print(two_g)


# ## Problem 3: Set combinations

# In[24]:


#3.a Is set E a subset of set A

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

three_setE.issubset(three_setA)


# In[25]:


#3.b Is set E a strict subset of set A
# https://www.pythontutorial.net/python-basics/python-issubset/
three_setE < three_setA


# In[26]:


#3.c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print(three_c)


# In[27]:


#3.d Create a set that is the union of sets C, D and E
# https://www.pythontutorial.net/python-basics/python-set-union/
three_d = set.union(three_setC, three_setD, three_setE)
print(three_d)


# In[28]:


#3.e add 9 to the set
three_e = three_d.copy()
three_e.add(9)
print(three_e)
# 9 was already in the set, so this did not change anything.


# In[31]:


#3.f Using == compare this set to the list in one_a
one_a == three_e
three_f = False
print(three_f)


# In[32]:


#3.g Explain why they are not the same. What would you need to change if you wanted this to be True?
three_g = 'They would need to both be either sets or lists (could convert one), and they would need to contain the exact same elements.'
print(three_g)


# ## Problem 4: Changing variable types
# 
# For each step you will modify a variable, then append the type of the variable
# to a list. Do not recreate the list variable, it should be a running list of 
# types.

# In[33]:


#4.a Create a variable of type int with the value of 8
four_a = int(8)
print(four_a)
print(type(four_a))


# In[55]:


#4.b Create an empty list
four_list = []
print(four_list)


# In[56]:


#4.c Using type(), add the type of 4.a to this list
four_list.append(type(four_a))
print(four_list)


# In[57]:


#4.d Add 0.39 to 4.c
four_list.append(0.39)
print(four_list)


# In[58]:


#4.e append the type of 0.39 to the list
four_list.append(type(four_list[-1]))
print(four_list)


# In[59]:


#4.f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no decimal places,
# and append to list.
four_list.append(int(0.39**-10))
print(four_list)


# In[60]:


#4.g append the type to the list
four_list.append(type(four_list[-1]))
print(four_list)


# ## Problem 5: More variable type changes
# 
# Continue from where you left off in Problem 4.

# In[52]:


# 5.a Manually create a dictionary where the values are items in the list from where we left in problem 4, and the keys should
# be their index in the list. Print the dictionary.
five_a = {
  0 : "<class 'int'>",
  1 : 0.39,
  2 : "<class 'float'>",
  3 : 12284,
  4 : "<class 'int'>"
}
print(five_a)


# In[61]:


#5.b Add 300 and coerce it into a string (Umang said this means to add it "to the list from problem 4")
five_b = four_list.copy()
five_b.append("300")
print(five_b)


# In[62]:


#5.c append the type to the list
five_c = five_b.copy()
five_c.append(type(five_c[-1]))
print(five_c)


# In[64]:


#5.d slice the string up to the 2nd element
five_d = '300'[:2]
print(five_d)
type(five_d)


# In[66]:


#5.e append the type to the list
five_e = five_c.copy()
five_e.append(type(five_d))
print(five_e)


# In[71]:


#5.f use list comprehension to convert this into a new list of integers
# Umang said this means "create a list of the integers of the string '30', so the list would be [3,0]"
# https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/

five_f = list([int(x) for x in five_d])
print(five_f)

# or

five_f = list(map(int,five_d))        
print(five_f)


# In[73]:


#5.g append the type to the list
five_g = five_e.copy()
five_g.append(type(five_f))
print(five_g)


# In[74]:


#5.h append the type of three_setA to the list
five_h = five_g.copy()
five_h.append(type(three_setA))
print(five_h)


# In[ ]:




