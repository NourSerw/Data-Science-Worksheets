#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import praw
from praw.models import MoreComments


# In[2]:


reddit = praw.Reddit(user_agent="Comment Extraction (by /u/INSERTUSERNAME)",
                     client_id="CLIENT_ID", client_secret="CLIENT_SECRET")


# In[3]:


posts = []
for submission in reddit.subreddit("UpliftingNews").top("all"):
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])


# In[4]:


posts


# In[5]:


indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index


# In[6]:


posts.drop(indexNames, inplace=True)


# In[7]:


posts


# In[ ]:




