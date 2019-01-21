## Practice for Chapt 9.10
# List Modification, 2nd last question
# numbs = [5, 10, 15, 20, 25]
# for i in range(len(numbs)):
#     numbs[i] = numbs[i] + 5
# print(numbs)

# List Modification, last question
# lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
# larger_nums = []
# for nums in lst_nums:
#     nums = nums * 2
#     larger_nums.append(nums)
# print(larger_nums)

## Practice for Chapt 9.11
# s = "ball"
# r = ""
# for item in s:
#     #order is reversed becos concat happens first
#    r = item.upper() + r
#    # to see how the accumulator happens
#    print(r)

# str1 = "I love python"
# # HINT: what's the accumulator? That should go here.
# chars = []
# for s in str1:
#     s = s
#     chars.append(s)
# print(chars)

# output = ""
# for i in range(35):
#     output = output + "a"
# print(output)

# Practice for Chapt 9.15
# classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
# upp = []
# upper = []
# low = []
# lower = []
# # print(len(classes))
# for c in classes:
#     c = c.split(" ")
#     if c[0] == "MATH" and int(c[1]) >= 300:
#         upp.append(c)
#     elif c[0] == "PSYCH" and int(c[1]) >= 400:
#         upp.append(c)
#     elif c[0] == "ENG" and int(c[1]) >= 200:
#         upp.append(c)
#     else:
#         low.append(c)
#
# for c in upp:
#     c[1] = str(c[1])
#     c = c[0] + " " + c[1]
#     upper.append(c)
#
# for c in low:
#     c[1] = str(c[1])
#     c = c[0] + " " + c[1]
#     lower.append(c)
#
# print("upper:",upper)
# print("lower:",lower)
# # print(len(upper))
# # print(len(lower))

# question 4
# import keyword
#
# test = ["else", "integer", "except", "elif"]
# keyword_test = []
#
# for word in test:
#     keyword_test.append(keyword.iskeyword(word))
# print(keyword_test)

#question 5
# import string
# nums = string.digits
# is_num = []
# u = []
# chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']
#
# for c in chars:
#     if c in nums:
#         is_num.append(tuple((c,True)))
#     else:
#         is_num.append(tuple((c,False)))
# print(is_num)

# winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
# z_winners = winners
# z_winners.reverse()
# print(z_winners)
