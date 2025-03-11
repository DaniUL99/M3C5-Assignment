# Exercise 1

birds = ["magpie", "blackbird", "robin", "sparrow"]

for bird in birds:
    print(bird)

# Exercise 2

def suma_uno(num_one, num_two, num_three):
    print(num_one + num_two + num_three) 

suma_uno(1, 2, 3)

# Exercise 3

suma_dos = lambda num_one, num_two, num_three: num_one + num_two + num_three

print(suma_dos(1, 2, 3))

# Exercise 4

nombre = 'Enrique'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

if nombre in lista_nombre:
    print("Está en la lista")
else:
    print("No está en la lista")
