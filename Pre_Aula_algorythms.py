import random
import math

def main():
    myArr = []

    print("Selecione o tamanho de vetor que será ordenado:\n1 - 5! = 120 elementos\n2 - 10! = elementos\n3 - 15! = elementos")

    user_input = input()

    if user_input == '1':
        inputAux = math.factorial(5)
    elif user_input == '2':
        inputAux = math.factorial(10) 
    elif user_input == '3':
        inputAux = math.factorial(15)       
    else:
        print('Input invalido')

    random_list = [random.randint(0,inputAux) for i in range(inputAux)]

    tam = len(random_list)

    quick_sort(random_list, 0, tam - 1)




def quick_sort(list,low,high):

    while low < high:
        
        pi = dividir(list, low, high)

        quick_sort(list, low, pi - 1)

        quick_sort(list,pi + 1, high)


def dividir(arr, low, high):
    pivo = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivo:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1

