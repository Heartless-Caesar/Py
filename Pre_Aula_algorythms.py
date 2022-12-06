import random

def main():

    print("Selecione o tamanho de vetor que será ordenado:\n1 - 5 elementos\n2 - 10 elementos\n3 - 15 elementos")

    user_input = input()

    if user_input == '1':
        inputAux = 5
    elif user_input == '2':
        inputAux = 10 
    elif user_input == '3':
        inputAux = 15       
    else:
        print('Input invalido')
        

    random_list = [random.randint(0,inputAux + 100) for i in range(inputAux)]
    random_list_2 = [random.randint(0,inputAux + 100) for i in range(inputAux)]

    print(f"Desordenada {random_list}\n")

    tam = len(random_list)

    quick_sort(random_list, 0, tam - 1)

    bubble_sort(random_list_2)
        


def quick_sort(list,low,high):

    if low < high:
        
        pi = dividir(list, low, high)

        quick_sort(list, low, pi - 1)

        quick_sort(list,pi + 1, high)

        


def dividir(arr, low, high):
    pivo = arr[high]
    quick_comp = 0
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivo:
            quick_comp = quick_comp + 1
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    print(f"Comparacoes Quick = {quick_comp}")
    return i + 1


def bubble_sort(arr):
    bubble_comp = 0
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                bubble_comp = bubble_comp + 1
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

    print(f"Comparacoes Bubble {bubble_comp}")            


main()
