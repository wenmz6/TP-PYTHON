print("Quelle est la moyenne obtenue?")
moyenne = input("Moyenne obtenue:")
moyenne = float(moyenne)

if moyenne < 10:
    print("failure")
elif moyenne < 12:
    print("success")
elif moyenne < 14:
    print("satis bene")
elif moyenne < 16:
    print("cum laude")
elif  moyenne < 18:
    print("magna cum laude")
else:
    print("summa cum laude")
