
# coding: utf-8

# ### Superliga Argentina
# 
# https://sofifa.com/league/353
# 
# Recordar desactivar el JavaScript.
# 
# Obtener la lista de equipos de la liga `(nombre, ID)`. Por ejemplo:
# 
# ```
# [(River Plate, 1876), (San Lorenzo de Almagro, 1013), ...]
# ```

# In[3]:


import requests
from scrapy.http import TextResponse

r = requests.get('https://sofifa.com/league/353')
response = TextResponse(r.url, body=r.text, encoding='utf-8')


# In[7]:


equipos = response.xpath('/html/body/section/section/aside/div[2]/table/tbody/tr/td[1]/a/text()').extract()

equipos 


# In[6]:


OA = response.xpath('/html/body/section/section/aside/div[2]/table/tbody/tr/td/span/text()').extract()

OA


# In[5]:


type (OA)


# In[7]:


import numpy
OA = list(map(int, OA))
numpy.mean(OA)


# In[8]:


OA


# In[14]:


import requests
from scrapy.http import TextResponse

r2 = requests.get('https://sofifa.com/league/7')
response = TextResponse(r.url, body=r.text, encoding='utf-8')


# In[18]:


equipos2 = response.xpath('/html/body/section/section/aside/div[2]/table/tbody/tr/td[1]/a/text()').extract()

equipos2


# In[21]:


OA2 = response.xpath('/html/body/section/section/aside/div[2]/table/tbody/tr/td[*]/span/text()').extract()

OA2


# In[20]:


import numpy
OA2 = list(map(int, OA2))
numpy.mean(OA2)

