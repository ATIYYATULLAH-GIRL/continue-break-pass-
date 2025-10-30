x=int(input("ENTER A NUMBER: "))
if x%20==0:
    print("TWIST")
elif x%15==0:
    pass
elif x%3==0:
    print("BUZZ")
elif x%5==0:
    print("FIZZ")
else:
    print(x)