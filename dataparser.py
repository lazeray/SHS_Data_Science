import requests
import json
import sys
def download_webpage_as_html(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # return HTML contents
            return response.text
            
        else:
            exit()
    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)

def json_getter(contents):
    start_index = contents.find('"unused":[')
    end_index = contents.find("}]", start_index) + 2
    input_data = contents[start_index+10:end_index-1]
    return "[" + input_data + "]"

def time_adjuster(data_array):
    min = sys.maxsize
    for sprint in data_array:
        if sprint['x'] < min:
            min = sprint['x']

    for sprint in data_array:
        sprint['x'] -= min
    
    return data_array


if __name__ == "__main__":
    name = input("Enter jstris username: ") # gets jstris username
    url = "https://jstris.jezevec10.com/u/"+ name + "/stats"  # jstris data url
    contents = download_webpage_as_html(url)
    input_data = json_getter(contents)

    data_array = json.loads(input_data)

    data_array = time_adjuster(data_array)

    print(data_array)

    


