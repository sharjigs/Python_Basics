# Lists

mylist = [1,2,3]
print("Integer", mylist)
mylist = ['asdd', 45, 56,6.76, 6/7]
print("combo", mylist)
print("combo Length", len(mylist))
mylist= ['a', 'b', 'c']
print("First Element :- ", mylist[0])
print("All Element :- ", mylist[:])

mylist[0]= ' tytyyt'

print('mutable', mylist)

mylist.append('Manish')
print("Append Item in List", mylist)
mylist.extend(['sad','asd'])
print("Append List in List", mylist)

mylist.pop()
print("Remove Last Item from list", mylist)
mylist.pop(0)
print("Remove Specific Item from  list", mylist)

mylist.reverse()
print("Reverse List", mylist)

mylist.sort()
print("Sort My List", mylist)


mylist = [1, 2, ['x', 'y', 'z']]
print("Nested List", mylist[2][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]
print('List Comprehension' ,first_col)
