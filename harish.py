#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

import os
import string

imgcv2.imread("mypic.jpg") 

msg input ("Enter secret message:")

password = input("Enter a passcode:")
d={}
c={}
for i in range(225):
    d[chr(i)] = i

    c[i] = chr(1)

m = 0

n = 0
z = 0

for i in range (len (msg)):

    img[n, m, 2] = d[msg[i]]

    n = n + 1
    m = m+1
    z = (z + 1) * 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedimage.jpg") 
message = ""

n = 0
m = 0

z = 0

pas = input ("Enter passcode for Decryption")

if password == pas:

    for i in range(len(msg)):

        message = message + c[img[n, m, z]]

        n = n+1

        m = m + 1
        z = (z + 1) * 3

        print("Decryption message:", message)

else:

    print("YOU ARE NOT auth")


# In[ ]:




