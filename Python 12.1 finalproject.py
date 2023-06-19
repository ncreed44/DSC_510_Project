# DSC 510
# Week 12
# Programming Assignment Week 12
# Nathan Reed
# 03/04/2023
# ------------------------------

import requests


def city():  # does the search by city
    city_name = input('Please input the name of the city you would like the weather from: ')  # lets user choose city
    state_name = input('Please input the name of the state for the city you entered: ')  # lets user enter the state for the chosen city
    temperature = input('Please indicate F for Fahrenheit or C for Celsius: ')  # lets user choose Fahrenheit or Celsius
    try:  # stops the more common exceptions
        url1 = ('http://api.openweathermap.org/geo/1.0/direct?q=' + city_name + ',' + state_name + ',US&appid=f3cfb27e258625a4663cd732193b0f5c')
        lat = requests.get(url1).json()[0]['lat']
        lon = requests.get(url1).json()[0]['lon']
        if temperature == 'F' or temperature == 'f':  # finds option for Fahrenheit
            url2 = ('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=f3cfb27e258625a4663cd732193b0f5c&units=imperial')
            data = requests.get(url2).json()
            imperial_data(data)
            another_one = input('Would you like to look at the weather somewhere else? Type Yes or No: ')  # lets user decide if they want to do another weather lookup
            if another_one == 'Yes' or another_one == 'yes':
                main()
            elif another_one == 'No' or another_one == 'no':
                print("Thank you for trying my weather program!")
                exit()
        elif temperature == 'C' or temperature == 'c':  # finds option for Celsius
            url2 = ('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=f3cfb27e258625a4663cd732193b0f5c&units=metric')
            data = requests.get(url2).json()
            metric_data(data)
            another_one = input('Would you like to look at the weather somewhere else? Type Yes or No: ')  # lets user decide if they want to run another weather lookup
            if another_one == 'Yes' or another_one == 'yes':
                main()
            elif another_one == 'No' or another_one == 'no':
                print("Thank you for trying my weather program!")
                exit()
        else:
            print('Please try again!')
            city()
    except Exception as e:  # lets code error and restarts the lookup
        print(e)
        print('Please try again!')
        city()


def zipCode():  # does the search by zip code
    zipcode_number = input('Please enter the zipcode you would like the weather from: ')  # lets user choose what zip code they want
    temperature = input('Please indicate F for Fahrenheit or C for Celsius: ')  # lets user choose between Fahrenheit and Celsius
    try:  # prevents errors
        url1 = ('http://api.openweathermap.org/geo/1.0/zip?zip=' + zipcode_number + ',US&appid=f3cfb27e258625a4663cd732193b0f5c')
        data = requests.get(url1).json()
        lat = data['lat']
        lon = data['lon']
        if temperature == 'F' or temperature == 'f':  # finds option for Fahrenheit
            url2 = ('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=f3cfb27e258625a4663cd732193b0f5c&units=imperial')
            data = requests.get(url2).json()
            imperial_data(data)
            another_one = input('Would you like to look at the weather somewhere else? Type Yes or No: ')
            if another_one == 'Yes' or another_one == 'yes':
                main()
            elif another_one == 'No' or another_one == 'no':
                print("Thank you for trying my weather program!")
                exit()
        elif temperature == 'C' or temperature == 'c':  # finds option for Celsius
            url2 = ('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=f3cfb27e258625a4663cd732193b0f5c&units=metric')
            data = requests.get(url2).json()
            metric_data(data)
            another_one = input('Would you like to look at the weather somewhere else? Type Yes or No: ')
            if another_one == 'Yes' or another_one == 'yes':
                main()
            elif another_one == 'No' or another_one == 'no':
                print("Thank you for trying my weather program!")
                exit()
        else:
            print('Please try again!')
            zipCode()
    except Exception as e:  # lets code error and restarts the lookup
        print(e)
        print('Please try again!')
        zipCode()


def imperial_data(data):  # prints the data in imperial units
    temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    cloud_cover = data['clouds']['all']
    print('Current Temperature : {} degrees Fahrenheit'.format(temp))
    print('High Temperature : {} degrees Fahrenheit'.format(high_temp))
    print('Low Temperature : {} degrees Fahrenheit'.format(low_temp))
    print('Feels Like : {} degrees Fahrenheit'.format(feels_like))
    print('Wind Speed : {} miles/hour'.format(wind_speed))
    print('Pressure : {} hPa'.format(pressure))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humidity))
    print('Description : {}'.format(description))
    print('Cloud Cover : {} %'.format(cloud_cover))


def metric_data(data):  # prints the data in metric units
    temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']
    pressure = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    cloud_cover = data['clouds']['all']
    print('Current Temperature : {} degrees Celsius'.format(temp))
    print('High Temperature : {} degrees Celsius'.format(high_temp))
    print('Low Temperature : {} degrees Celsius'.format(low_temp))
    print('Feels Like : {} degrees Celsius'.format(feels_like))
    print('Wind Speed : {} meter/sec'.format(wind_speed))
    print('Pressure : {} hPa'.format(pressure))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humidity))
    print('Description : {}'.format(description))
    print('Cloud Cover : {} %'.format(cloud_cover))


def main():
    print('Welcome to my weather program!')  # welcomes the user
    while True:  # runs the program until the user is done
        determination = input('Please enter whether you would like to search the weather by zip code or city: ')  # lets the user decide city or zip code
        if determination == 'zip code' or determination == 'Zip Code':
            try:
                zipCode()
            except Exception as e:
                print(e)
                print('Please try again!')
                zipCode()
        elif determination == 'city' or determination == 'City':
            try:
                city()
            except Exception as e:
                print(e)
                print('Please try again!')
                city()
        elif determination == 'done':
            break
        else:
            print('Invalid input! Please either enter zip code, city, or done. Thank you!: ')


if __name__ == "__main__":
    # execute only if run as a script
    main()
