import PyPDF2
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re

# Step 1: PDF 로드
file_path = 'Infinite-Jest.pdf'
pdf_reader = PyPDF2.PdfReader(file_path)

# Specify 페이지들 분석
page_number = 10  # 원하는 페이지 입력
page_text = pdf_reader.pages[page_number].extract_text()

# Step 2: 텍스트 접근
text = page_text.lower()
text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
words = text.split()

# Step 3: 단어수 빈도 측정
stopwords = set(STOPWORDS)
filtered_words = [word for word in words if word not in stopwords]
word_freq = {word: filtered_words.count(word) for word in set(filtered_words)}

# Step 4: 워드 클라우드 생성
wordcloud = WordCloud(width=800, height=800, background_color='black', 
                      max_font_size=350, stopwords=stopwords, 
                      font_path='c:/Windows/fonts/malgun.ttf')
wordcloud.generate_from_frequencies(word_freq)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
