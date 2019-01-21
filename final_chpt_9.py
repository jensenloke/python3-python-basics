# Question 1
# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# score = scores.split(" ")
# score_list = list()
# for i in range(len(score)):
#     score[i] = int(score[i])
#     if score[i] >= 90:
#         score_list.append(score[i])
# a_scores = len(score_list)
# print(a_scores)

# Question 2
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# org_words = org.split(" ")
# org_words_no_stop = list()
# for words in org_words:
#     if words not in stopwords:
#         org_words_no_stop.append(words)
# #print(org_words_no_stop)
# acro = ""
# for words in org_words_no_stop:
#     w = words[0].upper()
#     acro = acro + w
# print(acro)

# Question 3
# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"
#
# sent_words = sent.split(" ")
# sent_words_no_stop = list()
# for words in sent_words:
#     if words not in stopwords:
#         sent_words_no_stop.append(words)
# print(sent_words_no_stop)
#
# acro = ""
# list = list()
# for words in sent_words_no_stop:
#     w = words[0:2].upper()
#     list.append(w)
# acro = ". ".join(list)
# print(acro)

# Question 4
# p_phrase = "was it a car or a cat I saw"
# p_phraselist = p_phrase.split(" ")
# r_phraselist = p_phraselist[:]
# r_phraselist.reverse()
# rlist = list()
# for word in r_phraselist:
#     word = word[::-1]
#     rlist.append(word)
# r_phrase = " ".join(rlist)
# # print(rlist)
# print(r_phrase)
# print(p_phrase == r_phrase)

# Question 5
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    item = item.split(", ")
    #print(item)
    merchandise = item[0]
    merchandise_quantity = item[1]
    price = item[2]
    s = "The store has {} {}, each for {} USD "
    print(s.format(merchandise_quantity,merchandise,price))
