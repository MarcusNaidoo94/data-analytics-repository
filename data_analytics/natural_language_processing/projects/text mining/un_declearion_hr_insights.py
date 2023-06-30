#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.

# Read the text file
with open('un_declaration_hr_text_data.txt', 'r') as file:
    text = file.read()

# Split the text into terms
terms = text.split('\n')

# Remove empty lines and leading/trailing whitespaces
terms = [term.strip() for term in terms if term.strip()]


for term in terms:
    print(term)


# In[3]:


#2.

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords

# Read the text file
with open('un_declaration_hr_text_data.txt', 'r') as file:
    text = file.read()

# Set up the stopwords
stop_words = set(stopwords.words('english'))

# Generate word frequencies
word_frequencies = {}
words = text.split()
for word in words:
    if word.lower() not in stop_words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='black').generate_from_frequencies(word_frequencies)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[4]:


#3.

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

# Read the document
with open('un_declaration_hr_text_data.txt', 'r') as file:
    document = file.read()

# Tokenize the document into words
words = document.split()

# Set up the stopwords
stop_words = set(stopwords.words('english'))

# Filter out stop words and convert to lowercase
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count the frequencies of the terms
term_frequencies = Counter(filtered_words)

# Get the top 25 frequent terms
top_terms = term_frequencies.most_common(25)

# Separate the terms and frequencies
terms, frequencies = zip(*top_terms)

# Generate the bar plot
plt.figure(figsize=(12, 6))
plt.bar(terms, frequencies)
plt.xticks(rotation=45)
plt.xlabel('Terms')
plt.ylabel('Count')
plt.title('Top 25 Frequent Terms')
plt.tight_layout()
plt.show()


# In[ ]:




