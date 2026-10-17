def city_averages(weather):
    average_cleaned_dict = {}
    for city, values in weather.items():
        average_cleaned_dict[city] = sum(values["temp"])/len(values["temp"])
    # Returns dictionary having average of the clean temperatures of a city
    return average_cleaned_dict

def extremes(averages):
    hottest = coolest = ''
    hot_temp = 0
    for city, val in averages.items():
        if (val>=hot_temp): # Checks for temperature higher than current hottest temperature
            hot_temp = val
            hottest = city
    cool_temp = hot_temp # Assigns cool temperature initially as the hottest temperature
    for city, val in averages.items():
        if (val<=cool_temp): # Checks for temperature lower than current coolest temperature
            cool_temp = val
            coolest = city
    print("")
    print(f"{'Hottest city: ':<15}{hottest} ({hot_temp:.1f})")
    print(f"{'Coolest city: ':<15}{coolest} ({cool_temp:.1f})")