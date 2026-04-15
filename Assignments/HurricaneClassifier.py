wind_speed = int(input("Please enter the wind speed of the hurricane in miles per hour:\n->"))

def hurricane_category(wind_speed):
    try:
        if (wind_speed >= 157):
            return "That is a Category 5 Hurricane."

        elif (wind_speed < 157 and wind_speed >= 130):
            return "That is a Category 4 Hurricane."
          
        elif (wind_speed < 130 and wind_speed >= 111):
            return "That is a Category 3 Hurricane."

        elif (wind_speed < 111 and wind_speed >= 96):
            return "That is a Category 2 Hurricane."

        elif (wind_speed < 96 and wind_speed >= 74):
            return "That is a Category 1 Hurricane."
    
    except (wind_speed < 74):
        print("You are overreacting. That is not a Hurricane.")

print(hurricane_category(wind_speed))