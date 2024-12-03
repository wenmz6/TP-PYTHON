print("saisissez les angles")
angle_1 = input("Angle 1: ")
angle_2 = input("Angle 2: ")
angle_3 = input("Angle 3: ")

try:
    angle_1= int(angle_1)
    angle_2= int(angle_2)
    angle_3 = int(angle_3)
except:
    print("pas de lettre ni de symbole")
    exit()



if angle_1 + angle_2 + angle_3 == 180:
    if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("rectangle")

    if angle_1 == angle_2 == angle_3:
        print("equilatéral")
    elif angle_1 == angle_2 or angle_1 == angle_3 or angle_3 == angle_2:
        print("isocèle")
    else:
        print("scalène")
else:
    print("ce n'est pas un triangle")

    

