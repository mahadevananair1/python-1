is_hungry = False
good_weather = True

if is_hungry and good_weather:
    print("Jan go to eat, and go play out")
elif not(is_hungry) and good_weather:
    print("Jan go out for 5min")
elif not(good_weather) and is_hungry:
    print("Jan eat")
else:
    print("is a bad day")

