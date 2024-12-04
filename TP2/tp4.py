print("introduire volume et pression")

volume = input("volume: ")
pressure = input("pression: ")

try:
    volume = float(volume)
    pressure = float(pressure)
except:
    print("erreur générale")
    exit()

p_threshold = 2.3
v_threshold = 7.41

problemes = 0

if volume > v_threshold:
    print("volume de l'enceinte doit diminuer")
    problemes += 1

if pressure > p_threshold:
    print("la pression de l'enceinte doit augmenter")
    problemes += 1

if problemes == 2:
    print("stop pressurisation")
else:
    print("tout va bien")
