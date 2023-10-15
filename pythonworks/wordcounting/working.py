text="hello,hii,hello,haii,hii,hello"
words=text.split(',')
word_count={}

for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)
print(max(word_count,key=lambda k:word_count.get(k)))
