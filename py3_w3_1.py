#question1
# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# list = list()
# count = 0
# rainfall = rainfall_mi.split(", ")
# for rain in rainfall:
#     rain = float(rain)
#     if rain >= 3.0:
#         list.append(rain)
#         count = count + 1
# num_rainy_months = len(list)
# print(num_rainy_months)

#question 2
# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# #
# # Write your code here.
# words = sentence.split(" ")
# print(words)
# list = list()
# for word in words:
#     if word[0] == word[-1]:
#         list.append(word)
# same_letter_count = len(list)
# print(same_letter_count)

#question 3
# items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
# list = list()
# for item in items:
#     if "w" in item:
#         list.append(item)
# acc_num = len(list)
# print(acc_num)

#question 4
# sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
# words = sentence.split(" ")
# list = list()
# for word in words:
#     if "a" in word or "e" in word:
#         list.append(word)
# num_a_or_e = len(list)
# print(num_a_or_e)

#question 5
# s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# vowels = ['a','e','i','o','u']
#
# # Write your code here.
# list = list()
# for word in s:
#     for vowel in vowels:
#         if vowel in word:
#             print(vowel)
#             list.append(vowel)
# num_vowels = len(list)
# print(num_vowels)
