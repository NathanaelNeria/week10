text='this is a collection of words of nice words this is a fun thing it is'

text_list = text.strip().split()

for i in text_list:
    if i not in text_dict:
        text_dict[i] = 1
    else:
        text_dict[i] += 1

for each in text_dict:
    print("{:10s} -- {}".format(each, text_dict[each])