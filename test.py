def checkNum(num):
    if(num % 2 == 0):
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")    

num_input = int(input("Digite um número: "))   
checkNum(num_input)  