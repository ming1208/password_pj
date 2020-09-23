#!/usr/bin/env python
# coding: utf-8

# In[23]:


pw = 'a123456'
nbr = 3
while nbr > 0 :
    ip = input('請輸入密碼: ') 
    if pw == ip :
       print('登入成功') 
       break
    elif nbr-1 >= 1 :
        nbr = nbr - 1      
        print('密碼錯誤還有', nbr,'次機會')       
    else:
        print('密碼已錯誤三次，禁止登入')
        break  
    


# In[ ]:





# In[ ]:





# In[ ]:




