# Sorting array withouth sort method and sorted function - from the web
new_list = []
my_list = [-15, -26, 15, 1, -34, 23, -64, 23, 76]

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list)



# Sorting array withouth any method or function - from the web
l = [64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]

print(l)