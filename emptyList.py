# write a python script to create a list of this list 
# should contain all the numbers divisible by 2 from 5-50

# list = []

# for i in range(5,50):
#     i%2 == 0
#     list.append(i)

# print(list)


# write a code to check the duplicate in 2 list and print the 3rd list which has ele of l1 and l2

list1 = [1,2,3,4,5,6]
list2 = [2,6]
list4 = []
for element in list1:
    if element in list2:
        list4.append(element)

print(list4)

list3 = list1 + list2

print(list3)