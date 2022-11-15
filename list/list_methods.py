cantanes = ['2pac', 'Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1, 2, 7, 4, 5, 3, 8, 6]

# Order
print(numeros)
numeros.sort()
print(numeros)

# Add new elements
cantanes.append("Natos y Waor")
print(cantanes)
cantanes.insert(1, "David Bisbal")

#  Delete elements
cantanes.pop(1) #  remove by an index
cantanes.remove('Bad Bunny')

print(cantanes)

numeros.reverse() #  reverse the list
print(numeros)

# Search element
print('Drake ' in cantanes)

# count element
print(cantanes)
print(len(cantanes))

# How many times is a number
print(numeros.count(8))

# get index
print(cantanes.index("Drake"))


# join lists
cantanes.extend(numeros)
print(cantanes)

