import pyowm

owm = pyowm.OWM('e2ef41348ab4f86bf88ed303bc16b2dc')
mgr = owm.weather_manager()

where = input('Где искать погоду?: ')

observation = mgr.weather_at_place(where)
w = observation.weather
print(w)
