from clean_values import clean
from average_values import average
from day_type_calculate import day_type
from city_averages_calculate import city_averages, extremes
from daily_rain_calculate import totaL_daily_rain
from heavy_rain_calculate import heavy_rain, day_city_heavy_rain_print

days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
weather = {
    "Kochi":{
        "temp":[31,32,30,29,31,33,32],
        "rain":[0,5,12,20,0,0,3]
    },
    "Munnar":{
        "temp":[18,19,17,16,18,20,19],
        "rain":[2,8,15,25,5,0,4]
    },
    "Palakkad":{
        "temp":[36,37,38,-999,37,39,38],
        "rain":[0,0,0,0,0,0,0]
    },
    "Kozhikode":{
        "temp":[30,31,30,29,30,32,31],
        "rain":[0,10,8,18,2,0,1]
    }
}
clean_list = clean(weather) # 'clean_list' dict has 'temp' list with no error values
average(clean_list)
day_type(clean_list)
average_cleaned_dict = city_averages(clean_list) # 'average_cleaned_dict' has cities and its average temperatures
extremes(average_cleaned_dict)
totaL_daily_rain(days, clean_list)

# Heavy Rain functionality
for limit in (20,10): # 2 limits checked 20 and 10
    print("")
    print(f"RAIN ALERTS ({limit} mm or more)")

    for index, day in enumerate(days):
        day_city_heavy_rain = heavy_rain(index, clean_list, limit) # Returns list of tuples having 'city' and 'rain' values
        if day_city_heavy_rain:
            day_city_heavy_rain_print(days[index],day_city_heavy_rain,limit) # Prints the values of above list


            

