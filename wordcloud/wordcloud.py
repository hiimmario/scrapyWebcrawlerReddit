from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

import csv

file = open("C:/Users/reimar/PycharmProjects/chatbot/reddit_crawler/reddit_crawler_scrapy/reddit_5th.csv", "rt")
reader = csv.reader(file)

text = ''

for index, row in enumerate(reader):
    if index != 0 and (len(row) != 0):
        text += row[0] + ' '

print(text)

file.close()

img = Image.open("C:/Users/reimar/PycharmProjects/chatbot/wordcloud/snoo_head.png")
alice_mask = np.array(img)

stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, colormap='cool', scale=2, mode='RGBA')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file("C:/Users/reimar/PycharmProjects/chatbot/wordcloud/snoo_head_test.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

