a=str(input('are you "Tel aviv" resident (yes/no):'))
if a=="yes":
    b=int(input("what your age: "))
    if b>65:
        print("זכאי להנחה")
    else:
        print("אתה צעיר מידי להנחה")
if a=="no":
    print("the count is only for resident")
else:
    print("not valid informaition")