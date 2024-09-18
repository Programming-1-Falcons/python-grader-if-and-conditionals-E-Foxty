grade = int(input("What grade did you get this time? "))
bar = 0

while grade >= bar:
    if bar <= 50:
        print("F", end = ".")
    elif bar <= 60:
        print("D", end = "#")
    elif bar <= 75:
        print("C", end = ".")
    elif bar <= 88:
        print("B", end = "$")
    elif bar <= 100:
        print("A", end = ".")
    elif bar > 100:
        print("Y0u d1d !t y@ur ins#ne!3+'!", end = ".")
    bar = bar + 1


233