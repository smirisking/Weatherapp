import requests

Api_key = "3f757074bdaf922ace706f56211608f0"

def get_data(place, days, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={Api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value= 8 * days
    filtered_data = filtered_data[:nr_value]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Tokyo", days=3, kind="Temperature"))
