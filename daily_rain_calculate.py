def totaL_daily_rain(val_days,val_weather):
    daily_rain = {}
    wettest_day_rain = 0
    for index, day in enumerate(val_days): # Enumerate used to get index and value of the tuple 'val_days'
        total_day_rain = 0
        for city in val_weather.values():
            # Total rain of the city calculated by adding up all the 'index'(corresponds to index of 'val_days' tuple) elemnt of 'city["rain"]' dictionary
            total_day_rain += city["rain"][index] 
        daily_rain[day] = total_day_rain # Dictionary where key is the 'day name' and value is the corresponding 'total temperature' 
        if (total_day_rain > wettest_day_rain):
            wettest_day_rain = total_day_rain
            wettest_day = day # Wettest day assigned if total temperature of the day is higher that 'wettest_day_rain' value

    print("")
    print("RAINFALL BY DAY")
    for key, val in daily_rain.items():
        print(f"{key:<5}{val:>4} mm")
    print(f"{'Wettest day: '}{wettest_day} ({wettest_day_rain} mm)")

    