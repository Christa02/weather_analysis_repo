def heavy_rain(day_index,val_weather,limit):

    city_rain_list = []
    for city, values in sorted(val_weather.items()):
        current_day_rain = values["rain"][day_index]
        if (current_day_rain>=limit): # Checks whether rain of the particular day exceeds the limit
            city_rain_list.append((city,current_day_rain)) 
    return city_rain_list # Returns a list having tuples where values are city and corresponding rain of the day given (dat_index)

def day_city_heavy_rain_print(day, city_heavy_rain, limit):
    print(f"{day}:", end="")
    for day, (city,num) in enumerate(city_heavy_rain):
            # Check if it is the last item in the list and to avoid ',' at end
            if (day == len(city_heavy_rain) - 1):
                # Adds '\n ' to the end so that new line will be added once all elemts of the particular day ('city_heavy_rain') is printed
                print(f" {city} {num} mm", end="\n")
            else:
                print(f" {city} {num} mm", end=",") # Adds ', ' to the end so that all values of the particular day will be printed in same line
