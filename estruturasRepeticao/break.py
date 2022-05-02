# Exemplo 1
for i in range(1, 11):
    if i == 7:
        break
    print(i)
print("Exit")

#Exemplo 2
while True:
    keyboard = input("Insert 'exit' to exit: ")
    if keyboard == 'exit':
        break