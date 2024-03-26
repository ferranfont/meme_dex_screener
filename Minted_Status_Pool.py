#!/usr/bin/env python
# coding: utf-8

# In[1]:


# New Minted tokens and status
import pandas as pd

# Set the maximum column width to None to display the full width of DataFrame columns
pd.set_option('display.max_colwidth', None)

# Replace 'minted_tokens_tarde26.csv' with the path to your CSV file
file_path = 'minted_tokens_tarde26.csv'
df = pd.read_csv(file_path, index_col=False)

print(df.tail(50))


# In[2]:


df['TokensPool'] = (df['TokensPool'] / 1000000).round(0)

# Round the 'SolanasPool' values to 2 decimal places
df['SolanasPool'] = df['SolanasPool'].round(2)

df['TokensPoolPerc'] = df['TokensPoolPerc'].str.rstrip('%').astype(float) / 100


# In[3]:


df['DateCreation'] = pd.to_datetime(df['DateCreation'])
# Remove timezone information
df['DateCreation'] = df['DateCreation'].dt.tz_localize(None)


df['DateRevokeMint'] = pd.to_datetime(df['DateRevokeMint'])
# Remove timezone information
df['DateRevokeMint'] = df['DateRevokeMint'].dt.tz_localize(None)

df['DateFreezeAccount'] = pd.to_datetime(df['DateFreezeAccount'])
# Remove timezone information
df['DateFreezeAccount'] = df['DateFreezeAccount'].dt.tz_localize(None)

df['DatePool'] = pd.to_datetime(df['DatePool'])
# Remove timezone information
df['DatePool'] = df['DatePool'].dt.tz_localize(None)


# In[4]:


df.info()


# In[5]:


df.tail()


# # Top_memes

# In[7]:


# VARIABLES PARA EL FILTRO
SOLANAS = 5
BURNED = 0.89

# Creating a sub-DataFrame based on the specified conditions
sub_df = df[
    (df['RevokeMint'] == True) &
    (df['FreezeAccount'] == True) &
    (df['PoolCreated'] == True) &
    (df['SolanasPool'] > SOLANAS) &
    (df['TokensPoolPerc'] > BURNED)
]


# In[8]:


sub_df

