list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 0]
list3 = [9, 86, 54, 258, 56]

print("Index: ",list1[0])
print("Slice: ", list1[0:3])

list1.append(0)
print("Append: ",list1)

list1.extend(list2)
print("Extend: ", list1)


list1.insert(5,6)
print("Insert: ",list1)

list1.remove(0)
print("Remove: ",list1)

popped_number = list1.pop(6)
print("Poped List: ",list1)
print("Pooped Element: ",popped_number)

list1.sort()

print("Length: ",len(list1))