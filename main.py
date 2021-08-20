weather_c = {
    "Monday" : 14,
    "Tuesday" : 15,
    "Wednesday" : 16,
    "Thursday" : 17,
    "Friday" : 18,
    "Saturday":19,
    "Sunday" :20,
}
weather_f = {day:temp_c*9/5 + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

