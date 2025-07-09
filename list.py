list=[1,2,3,4,5,6,7,8,9,10]

# # #search by index
# print(list[7])

# # #search by value
# print(list.index(6))

# # #type 
# print(type(list))
# print(list)

# # #modify:give index number for change the value of that 
# list[2]=3
# print(list)

# # #insert :index number and value
# list.insert(7,8)
# print(list)

# # #append :last of the list
# list.append(11)
# print(list)

# # #remove:give value for remove
# list.remove(3)
# print(list)

# # #pop: give index number for delete   LIFO
# pop_value=list.pop(7)
# print(pop_value)
# print(list)

# # reverse
# list.reverse()
# print(list)

# # for loop
# for i in list:
#      print(i)

# list.reverse()
# print(list)

# # enumrates
# for i,j in enumerate(list):
#     print(i,j)

# # square of numbers
# for x in range(len(list)):
#     list[x]=list[x]**2
# print(list)

# # comprehension loop
# square=[num**2 for num in range (len(list))]
# print(square)

# list1=[1,2,3,4]
# list2=[5,6,7,8]
# pair=[[i,j] for i in list1 for j in list2 ]
# print(pair)

# word=["tanvi","palak","priya","kushwaha"]
# length=[len(i) for i in word]
# print(length)

#print(list[5:8])