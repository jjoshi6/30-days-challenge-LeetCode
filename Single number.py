#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4"""

# function to find the once  
# appearing element in array 
def findSingle( ar, n): 
      
    res = ar[0] 
      
    # Do XOR of all elements and return 
    for i in range(1,n): 
        res = res ^ ar[i] 
      
    return res 
  
# Driver code 
ar = [2, 3, 5, 4, 5, 3, 4] 
print ("Element occuring once is", findSingle(ar, len(ar))) 
        


# In[ ]:




