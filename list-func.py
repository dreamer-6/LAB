from functools import reduce
number = [ 1,2,3,4,5,6,7,8,9,10]

students = [
    {"name":"Lana", "age":35,"grade":96},
    {"name":"Abel", "age":32,"grade":92},
    {"name":"Rose", "age":30,"grade":85},
    {"name":"Bille", "age":33,"grade":76}
    ]

fruits = ["Apple","Banana","Grape","Pinapple","Papaya","Orange"]

squre_value = list(map(lambda x: x**2,number))
singer_name = list(map(lambda x: x["name"],students))
fruit_upper = list(map(lambda x: x.upper(),fruits))

top_singer = list(filter(lambda x: x["grade"] > 85,students))
search = list(filter(lambda x: "A" in x, students))
even = list(filter(lambda x: x%2==0,number))

product = reduce(lambda x,y: x+y,number)
sum = reduce(lambda x,y: x*y,number)

print("Squre Value: ",squre_value)
print("Singers: ",singer_name)
print("Upper: ",fruit_upper)
print("Top Signers: ", top_singer)
print("Search: ",search)
print("Even number: ",even)
print("Sum of Product: ",product)
print("Product of sum: ",sum)