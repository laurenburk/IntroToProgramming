wind_speed = int(input("Please enter the wind speed of the hurricane in miles per hour:\n->"))

if (wind_speed >= 157):
    print("That is a Category 5 Hurricane")

elif (wind_speed < 157 and wind_speed >= 130):
    print("That is a Category 4 Hurricane.")
          
elif (wind_speed < 130 and wind_speed >= 111):
    print("That is a Category 3 Hurricane.")

elif (wind_speed < 111 and wind_speed >= 96):
    print("That is a Category 2 Hurricane.")

elif (wind_speed < 96 and wind_speed >= 74):
    print("That is a Category 1 Hurricane.")

else:
    print("That is more of a Tropical Storm than a Hurricane.")