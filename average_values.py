def average(values):
    print("")
    print("WEEKLY SUMMARY")
    print(f"{'City':<10}{'Avg':<7}{'Max':<6}{'Min':<6}{'Rain':<7}{'Rainy'}")
    for city, val in sorted(values.items()):
        avg_temp = sum(val["temp"])/len(val["temp"])
        max_temp = max(val["temp"])
        min_temp = min(val["temp"])
        total_rain = sum(val["rain"])
        no_rainy_days = 0
        for rain in val["rain"]:
            if rain != 0: # Checks whether the value of rain in a day is zero
                no_rainy_days += 1 # Counts the days where there was rain
        print(f"{city:<10}{avg_temp:<7.1f}{max_temp:<6}{min_temp:<6}{total_rain:<7}{no_rainy_days}")
