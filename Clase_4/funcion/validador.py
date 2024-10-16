def todo_es_un_numerico(valor):
    return valor.isnumeric()

def rango_valido(valor):
    return (999999 < valor < 100000000)

if __name__ == '__main__':
    print("**************************************")
    print("estoy en el modulo del validador")
    print(todo_es_un_numerico("asdasd"))
    print(todo_es_un_numerico("123123123"))
    print("VALIDADOR -> __name__", __name__)
    print("**************************************")