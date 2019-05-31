from datetime import datetime

def unixtimetotime(time):
    ts = int(time)
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def valid_date(time):
    try:
        return datetime.strptime(time, "%Y-%m-%d %H:%M")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(time)
        raise argparse.ArgumentTypeError(msg)

def fahrtocels(fahr):
    return (fahr - 32) / 1.8

def checkjsonkey(data,loc,key):
    if key in data[loc]:
        return data[loc][key]
    else:
        return 0
       
def get_values(data):
    latitude = data['latitude']
    longitude = data['longitude']
    timezone = data['timezone'] 

    #currently
    currently_time = data['currently']['time']
    currently_time = unixtimetotime(currently_time)
    currently_summary = data['currently']['summary']
    #preciptype = data['currently']['precipType']
    currently_temperature = fahrtocels(data['currently']['temperature'])
    currently_apparentTemperature = fahrtocels(data['currently']['apparentTemperature'])
    currently_humidity = data['currently']['humidity'] 
   # currently_pressure = data['currently']['pressure']
    currently_pressure = 5
    currently_windSpeed = data['currently']['windSpeed']
    currently_cloudCover = data['currently']['cloudCover']
    currently_visibility = checkjsonkey(data,'currently','visibility')
  

    values = [latitude,longitude,timezone,
    currently_summary,currently_temperature,currently_time,currently_apparentTemperature,currently_humidity,currently_pressure,currently_windSpeed,currently_cloudCover,currently_visibility
    
    

    ]
    return values 
