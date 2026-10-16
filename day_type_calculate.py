def day_type(values,hot=35, warm=29):
    city_day_type_dict = {}

    for city, val in sorted(values.items()):
        hot_count = warm_count = cold_count = 0 # Sets no of hot/ cold / warm days of a city initially as zero

        if (len(val["temp"]) != 0): # Checks whether any 'temp' list of weather dict is empty
            for temp in val["temp"]:
                if (temp>=hot):
                    hot_count += 1
                elif (temp<35 and temp>=warm):
                    warm_count += 1
                else:
                    cold_count += 1
            # Dict to store no of hot / cold/ warm days of each city
            city_day_type_dict[city] = {
                "Hot": hot_count, 
                "Warm" : warm_count, 
                "Cold" :cold_count
            }

    print("")
    print("DAY TYPES")
    print(f"{'City':<10}{'Hot':<5}{'Warm':<6}{'Cold'}")
    for key,val in city_day_type_dict.items():
        print(f"{key:<10}{val.get("Hot",0):<5}{val.get("Warm",0):<6}{val.get("Cold",0):<5}")
