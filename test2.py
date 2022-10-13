def checkString(alvo,string):
    if(string != None and alvo in string):
        print(f'A string "{string}" contém o alvo "{alvo}"')
    else:
        print(f'A string "{string}" não contém o alvo "{alvo}"')
    

checkString("olá","olá joão")    