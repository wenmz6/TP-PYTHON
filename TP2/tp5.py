 # print("Combien pèses-tu?")
weight = input("Combien pèses-tu? (kg): ")
height = input("Quelle taille fais-tu? (M): ")
sexe_input=input("Etes-vous un homme ou une femme (f/m): ")

try:
    weight = float(weight)
    height = float(height)
except:
    print("recommence, mais mieux")
    exit()


body_mass_index = weight/(height**2)
print("Votre bmi est %.2f" % body_mass_index)

# pi = 0
# if sexe_input == "f":
#     pi = femme_pi
# else: 
#     pi = homme_pi

# pi = femme_pi if sexe_input == "f" else homme_pi



if body_mass_index < 18.5:
    print("Vous êtes en sous-poids")
elif body_mass_index <= 25:
    print("Votre poids est normal")
elif body_mass_index <= 32:
    print("Vous êtes en surpoids voire obèse")
else:
    print("Vous êtes mega gros")

homme_pi = ((height*100)-100) - ((height*100)-150)/4
femme_pi = ((height*100)-100) - ((height*100)-120)/4
pi=0

if sexe_input =="f":
    pi=femme_pi
else:
    pi=homme_pi

print("Votre poids idéal est:", pi)

delta_poids = weight - pi
if delta_poids > 0:
    print("Vous devez perdre %d kg." % delta_poids)
else:
    print("Vous devez prendre %d kg." % (delta_poids*-1))
