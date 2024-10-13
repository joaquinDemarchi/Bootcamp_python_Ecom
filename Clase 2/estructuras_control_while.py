import time

cont = 1
"""
while cont <= 10:
    print(f"Hola {cont}")
    # cont = cont + 1
    cont += 1
    time.sleep(2)
"""

while True:
    # pass
    if cont % 2 == 0:
        print(f"Hola {cont}")
    # else:
    #    continue
    
    cont += 1
    time.sleep(2)

    if cont == 10:
        break




