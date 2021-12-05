#Loki Function

def lokipoint(lokilist):
    lokicombination = ("Y", "Y", "Y", "Y", "N")
    userlokicombination = lokilist
    lokipoints = 0
    for trait in range(5):
        if lokicombination[trait] == userlokicombination[trait].upper():
            lokipoints += 1
    return lokipoints

user = ["N","Y","N","Y","n"]
point = lokipoint(user)
print(point)
