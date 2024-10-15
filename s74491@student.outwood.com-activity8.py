def main():
    global Passangers
    global cost
    cost = 3
    Passangers = int(input("Input amount of passangers: "))
    distance = int(input("Input the amount of distance: "))
    if distance > 1:
        cost = 2 + (distance-1)*2
    else:
        cost = 3
    if Passangers >= 5:
        cost = cost * 1.5
main()

print("Cost of the journey is £",cost)