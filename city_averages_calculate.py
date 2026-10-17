def city_averages(weather):
    average_cleaned_dict = {}
    for city, values in weather.items():
        average_cleaned_dict[city] = sum(values["temp"])/len(values["temp"])
    return average_cleaned_dict

def extremes(averages):
    hottest = coldest = ''
    hot_temp = cold_temp = 0
    print(averages.items())
    for city, val in averages.items():
        if (val>=hot_temp):
            hot_temp = val
            hottest = city
    cold_temp = hot_temp
    for city, val in averages.items():
        if (val<=cold_temp):
            cold_temp = val
            coldest = city
    print("")
    print(f"{'Hottest city: ':<15}{hottest} ({hot_temp:.1f})")
    print(f"{'Coldest city: ':<15}{coldest} ({cold_temp:.1f})")