def totaL_daily_rain(val_days,val_weather):
    daily_rain = {}
    wettest_day_rain = 0
    for index, day in enumerate(val_days):
        total_day_rain = 0
        for city in val_weather.values():
            total_day_rain += city["rain"][index]
        daily_rain[day] = total_day_rain
        if (total_day_rain > wettest_day_rain):
            wettest_day_rain = total_day_rain
            wettest_day = day

    print("")
    print("RAINFALL BY DAY")
    for key, val in daily_rain.items():
        print(f"{key:<5}{val:>4} mm")
    print(f"{'Wettest day: '}{wettest_day} ({wettest_day_rain} mm)")

    