import json
import requests
n=0
st=""
places =["Mangalore","Chellanam", "Vypeen", "Koyilandy", "Neendakara", "Vilinjam","Tuticorin", "Nagapattinam","Vishakhapatnam"]
tour=["Goa","Agra","Rajasthan","Delhi","Munnar","Coorg","Manali","Ooty","Lonavala","Khandala","Shillong","Varanasi","Kolkata","Amritsar","Sikkim","Shimla"]
history=[]
while(True):
    print("Press 1 if you planning to undertake fishing activities")
    print("Press 2 if you are planning to travel")
    print("Press 3 if you are just curious to know the weather of a location of your choice")
    print("Press 4 if to stop")
    sorry="Sorry. No such option"
    sy=""
    n=int(input())
    if n==4:
        break
    if n<1 or n>4:
        print("No such option. Sorry")
    l=len(places)
    if n==1:
        print("Choose your location from the following:")
        for i in range(l):
            print("Press ",i+1," for - ",places[i])
        print("Press ",l+1," for - Other choices:")
        m=int(input())
        if m<1 or m>l+1:
            sy=sorry
            print(sy)
        if m>0 and m<=l:
            st=places[m-1]
        if m==l+1:
            print("Enter Your Location Nmae:")
            st=input()
            places.append(st)
    if n==2:
        print("Choose your location from the following:")
        for i in range(len(tour)):
            print("Press ",i+1," for - ",tour[i])
        print("Press ",i+2," for - Other choices:")
        m=int(input())
        if m<1 or m>len(tour)+1:
            sy=sorry
            print(sy)
        if m>0 and m<=len(tour):
            st=tour[m-1]
        if m==len(tour)+1:
            print("Enter Your Location Name:")
            st=input()
            tour.append(st)
    if n==3:
        if len(history)>0:
            print("Choose your location from the following:")
        for i in range(0,len(history)):
            print("Press ",i+1," for - ",history[i])
        if len(history)>0:
            print("Press ",i+2," for - Other choices:")
            m=int(input())
            if m<1 or m>len(history)+1:
                sy=sorry
                print(sy)
            if m>0 and m<=len(history):
                st=history[m-1]
            if m==len(history)+1:
                print("Enter Your Location Name:")
                st=input()
                history.append(st)
        if len(history)==0:
            print("Enter Your Location Name:")
            st=input()
            history.append(st)
    #link='https://goweather.herokuapp.com/weather/'Curitiba''
    s="http://api.weatherstack.com/current?access_key=4f6fb7a3c084dd3ce1e6f6a7deebb39d&query="
    if len(st)>0:
        try:
            s2=s+st
            response = requests.get(s2)
            #print(response)
            data=json.loads(response.text)
            #print(data)
            print("Overall Weather:  ",data['current']['weather_descriptions'])
            print("Country:  ",data['location']['country'])
            print("Latitude:  ",data['location']['lat'])
            print("Longitude:  ",data['location']['lon'])
            print("Wind Speed:  ",data['current']['wind_speed'])
            print("Wind Degree:  ",data['current']['wind_degree'])
            print("Wind Direction: ",data['current']['wind_dir'])
            print("Temperature:  ",data['current']['temperature'])
            print("Pressure:  ",data['current']['pressure'])
            print("Precipitation:  ",data['current']['precip'])
            print("Humidity:  ",data['current']['humidity'])
            print("Cloud Cover:  ",data['current']['cloudcover'])
            print("Observation Time:  ",data['current']['observation_time'])
            st=""
        except:
            print("Sorry!! No such data available!! Please try again")