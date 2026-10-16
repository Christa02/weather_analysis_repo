def clean(values):
    print("SENSOR CHECK")
    print("-"*30)
    count = 0
    for city, val in sorted(values.items()):
        for temp in val["temp"]:
            if (temp<-50): # Checking whether temperature is below -50
                count += 1
                val["temp"].remove(temp) # Error temperature value removed from list
        print(f"{city:<10}{count} invalid reading(s)")
    return values