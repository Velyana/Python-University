def wow_such_much(start, end):
    doge_list = []
    for i in range(start, end):   
        if i%3 == 0 and i%5 == 0:
            doge_list.append("suchmuch")    
        elif i%3 == 0:
            doge_list.append("such")
        elif i%5 == 0:
            doge_list.append("much")
        else:
            doge_list.append(str(i))
    return doge_list


def count_doge_words(doge_sentence):
    count = 0   
    words = ['wow', 'lol', 'so', 'such', 'much', 'very']
    for i in  doge_sentence.split():
        if i in words:
            count += 1
    return count

