!pip install nltk
import nltk
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
text="""Hello mr. how are you dowing tody? the weather is great,and city is awesome.
The sky is pinkish-blue.you shouldn't eat carboard"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)
#%%
from nltk.tokenize import word_tokenize 
tokenized_word = word_tokenize(text)
print(tokenized_word)
from nltk.probability import FreqDist
fdist=FreqDist(tokenized_word)
print(fdist)
fdist.most_common(2)
#frequency distribution plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)
filtered_sent=[]
for w in tokenized_sent:
  if w not in stop_words:
    filtered_sent.append(w)
print("tokenized Sentence:",tokenized_sent)
