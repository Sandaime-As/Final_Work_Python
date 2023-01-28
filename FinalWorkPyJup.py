#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sympy as sp


# In[6]:


# Уравнение

x=sp.Symbol('x')
expr=sp.sin(x)**2-sp.cos(x)**2
expr


# In[14]:


# 1. Определить корни

expr_solve=sp.solve(expr)
expr_solve


# In[8]:


# 2. Производная

expr_diff=sp.diff(expr)
expr_diff


# In[15]:


# 3. Убывание функции

fall_exp=sp.solve(expr_diff<0)
fall_exp


# In[16]:


# 4. Возрастание функции

rise_exp=sp.solve(expr_diff>0)
rise_exp


# In[17]:


# 5. График

graph=sp.plot(expr)


# In[19]:


# 6. Вычислить вершину

peak_exp=sp.solve(expr_diff)
peak_exp


# In[21]:


# 7. Промежутки, на котором f > 0

rise_exp_origin=sp.solve(expr>0)
rise_exp_origin


# In[25]:


# 8. Промежутки, на котором f < 0

fall_exp_origin=sp.solve(expr<0)
fall_exp_origin


# In[ ]:




