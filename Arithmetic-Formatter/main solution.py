weight = float(input("enter weight "))
metrics = input("enter Metric symbol (k= kg)(p= pounds) ")


if metrics.upper() == "K":
    i = float(weight) * 0.45
    print("Weight =" +str(i) + "Pounds" )
elif metrics.upper() == "P":
    i = float(weight) / 0.45
    print("Weight=" + str(i) + "Kg" )
else:
    "Invalid entry"


