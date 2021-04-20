lst=['abc',123,1.5,True]
print(lst)
print(lst[0])
lst[0]='xyz' #changing using index
print(lst)
lst.insert(1,2) #insert 2 at 1st index
print(lst.pop())
lst.append([1,2,3,1]) #appends to the list
lst.extend([1,2,3,1]) #Extends the list 
print(lst)
lst.remove(1) #Removes first occurance
print(lst)
