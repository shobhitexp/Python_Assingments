import random#by using random function
import datetime#by using random function

def rainfall():
    print( "Collecting Data \n" )

    months = []  
    for monthinteger in range(1, 13):
        retrieved_month = datetime.date(1900, monthinteger, 1).strftime('%B')  
        months.append(retrieved_month)

    rainfall = dict()
    for rain in months:
        rainfall[rain]= random.randint(0,4)

    return rainfall

sort_rain = sorted(rainfall().items(), key=lambda item:item[1], reverse=True)

max = sort_rain[0][1]
max_month = sort_rain[0][0]
min = sort_rain[-1][1]
min_month = sort_rain[-1][0]
print("Data of :- ",max,"Maximum rain in ",max_month)
print("Data of :- ",min,"Minimum rain in ",min_month,"\n")

rain_sum = sum( d for d in rainfall().values())
average = sum( d for d in rainfall().values()) / len(rainfall())

print("sum of day's for getting rain :- ",rain_sum,"Day's")
print("Average chance of getting rain :- ",average,"Percent")
