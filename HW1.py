from collections import Counter
mylist = [2,2,1,1,1,2,2]
counter_list = Counter(mylist)
most_common = counter_list.most_common(1)
least_common = counter_list.most_common()[:-2:-1]
max_element = most_common[0][0]
min_element = least_common[0][0]
print(max_element,',',min_element)

