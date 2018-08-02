
# coding: utf-8

# In[1]:


#2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
#it is a vowel, False otherwise.

def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True


if __name__ == "__main__":
    print (is_vowel(1))
    print (is_vowel('a'))
    print (is_vowel('b'))


# In[4]:


#Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words .
#Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#Here 2,3 and 4 are the lengths of the words in the list.


def word(str_lst):
    ct_lst =[len(x) for x in str_lst]
    return ct_lst
str_lst =['ab','cde','erty']
word(str_lst)

