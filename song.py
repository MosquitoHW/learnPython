
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import numpy as np
from PIL import Image
abel_mask = np.array(Image.open("down2.jpg"))   #背景图片

text_from_file_with_apath = open('song.txt').read()  #要分词文件song.txt
'''
#英文文件
L = []
with open ('test.txt') as song:
    f = song.readlines()
    print(f)
for line in f:
    line = line.strip('\n')
    word = line.split(' ')
    for k in word:
        L.append(k)
s = (' ').join(L)
print(s)
'''
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
wordcloud1 = WordCloud(background_color='white',    # 设置背景颜色
            max_words = 200,            # 设置最大现实的字数
            stopwords = STOPWORDS,        # 设置停用词
            font_path = ('C:/Users/Windows/fonts/simkai.ttf'),# 设置字体格式，如不设置显示不了中文
            mask=abel_mask,
            max_font_size = 100,            # 设置字体最大值
            random_state = 50,            # 设置有多少种随机生成状态，即有多少种配色方案
            scale=.70).generate(wl_space_split)
# thul = thulac.thulac(seg_only = True)
#thul.f('song.txt','song_hw.txt')
image_colors = ImageColorGenerator(abel_mask)
wordcloud1.recolor(color_func=image_colors)
plt.imshow(wordcloud1,interpolation='bilinear')
plt.axis("off")
plt.show()
