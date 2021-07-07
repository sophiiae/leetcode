def top_k_words(s, k):
    '''
    function name: top_k_words
    input :String s, Integer k
    output: List of String
    '''
    import string
    for i in s:
        if i in string.punctuation:
            s = s.replace(i, ' ')
    s = s.lower().strip().split(" ")
    while '' in s:
        s.remove('')
    dic_s = list(set(s))
    dic = {}
    for i in range(len(dic_s)):
        dic[dic_s[i]] = 0
    
    for i in range(len(dic_s)):
        for j in range(len(s)):
            if dic_s[i] == s[j]:
                dic[dic_s[i]] += 1
    
    word_li = []
    value_li = []
    
    for word, value in dic.items():
        word_li.append(word)
        value_li.append(value)
        
    value_li_copy = value_li.copy()
    value_li_copy.sort()
    value_li_copy.reverse()
    
    most_popular = value_li_copy[:k]
    index = []
    for i in range(k):
        if most_popular[i] in value_li:
            index.append(value_li.index(most_popular[i]))
    
    output = []
    for i in range(k):
        output.append(word_li[index[i]])
    
    return output

s = '  i love python, he love  coding in python. the course is about python.'
print(top_k_words(s, 2))
