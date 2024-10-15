def main():
    cars = int(input("Enter amt of cars: "))
    people = int(input("Enter amt of people: "))
    seats = cars * 5
    if seats > people:
        print("not enough seats")
        main()
    else:
        CALC = people - seats
    cars = (CALC / 5) * 10
    print("total cars needed",cars)
main()