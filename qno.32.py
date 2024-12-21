weather = input("What is the today? (sunny/rainy): ")
if weather == "sunny":
    print("The weather is sunny! Please go outdoor activities like  hiking or picnic.")
elif weather == "rainy":
    has_rain_gear = input("Do you have a raincoat or umbrella? (yes/no): ")
    if has_rain_gear == "yes":
        print("You can visit a nearby mall or museum.")
    else:
        print("better stay at home and watch some movies you like.")
