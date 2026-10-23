units=int(input("Enter a consumption:   "))
if units<100:
    print("Low consumption")
elif units<200:
    print("Moderate consumption")
elif units<300:
    print("High consumption")
else:
    print("Very high consumption")


