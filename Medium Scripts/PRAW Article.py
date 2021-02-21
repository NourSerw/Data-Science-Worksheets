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


url = "https://www.reddit.com/r/UpliftingNews/comments/lemy1b/student_who_made_30k_from_gamestop_donates_games/"
submission = reddit.submission(url=url)


# In[4]:


posts = []
for top_level_comment in submission.comments[1:]:
    if isinstance(top_level_comment, MoreComments):
        continue
    posts.append(top_level_comment.body)
posts = pd.DataFrame(posts,columns=["body"])


# In[5]:


posts


# In[6]:


indexNames = posts[(posts.body == '[removed]') | (posts.body == '[deleted]')].index


# In[7]:


posts.drop(indexNames, inplace=True)


# In[8]:


posts


# In[ ]:




