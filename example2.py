import urllib.request, re 
from collections import Counter

n = 1 #size of n-gram

#You can substitute the link below with any web page with plain text
url = 'http://www.gutenberg.org/cache/epub/76/pg76.txt' 

page = urllib.request.urlopen(url)

contents = page.read()
#contents = contents[:len(contents)/500] #smaller data/less memory option

words = re.findall(r'\w+', contents) #Regular expression to find all words

ngrams = [] #A list to store the ngrams
i = 0

while i < len(words):
    ngrams.append(tuple(words[i:i+n])) #Splits "words" into n sized tuples
    i += n

print (Counter(ngrams)) #Calculates the frequency of each n-gram
