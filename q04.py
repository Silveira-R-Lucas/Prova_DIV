def join_text(text1, text2):
    return text1 + "," + text2
    

def get_input_and_print():
    input1 = input("Digite o primeiro texto: ")
    input2 = input("Digite o segundo texto:")
    print(join_text(input1,input2))

get_input_and_print()