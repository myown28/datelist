#~~~ Pratham-code ~~~
#~~ DATALIST ~~
import os
import time

os.system('cls')
print("DATA LIST MAKING")
A = input("filename\n")

while True:
    os.system('cls')
    print(f"DATA LIST MAKING {A}")
    a = input("enter e for edit or c for close\n")
    if a == 'e':
      a1 = input("taxt\n")
      f = open(f"{A}", "a")
      f.write(f"{a1}\n")
      f.close()
    
    else:
        print('exit')
        time.sleep(1)
        exit()
        

