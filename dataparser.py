import requests
import json
import sys
import matplotlib.pyplot as plt 
import statistics
import math

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

def graph(data_array, color):
    
    x_values = [sprint['x'] for sprint in data_array]
    y_values = [sprint['y'] for sprint in data_array]


    plt.plot(x_values, y_values, color)

    ##print(f"{name} has played {len(data_array)} games of tetris")

def medianBin(data_array, binsize):
    binned_array = []
    index = 0
    for x in range(0,math.floor(len(data_array)/binsize)): ## that's the number of bins total
        temp_array = []
        index = x * binsize
        for i in range(index,binsize+index):
            temp_array.append(data_array[i]) 
        binned_array.append(temp_array[median(temp_array)])
    return binned_array

def median(arr): ## finds the median, then returns the index in the given array
    values = [item['y'] for item in arr]
    median = statistics.median(values)
    return values.index(median)

if __name__ == "__main__":
    name = input("Enter jstris username: ") # gets jstris username
    url = "https://jstris.jezevec10.com/u/"+ name + "/stats"  # jstris data url
    contents = download_webpage_as_html(url) # self explanator
    input_data = json_getter(contents) # gets the data from html

  

    data_array = json.loads(input_data)

    data_array = time_adjuster(data_array)

    data_array = sorted(data_array, key=lambda k: k['x'], reverse=False) # sorts tetris times chronologically

    ##print(data_array)
    ##print(medianBin(data_array, 3))
    ##graph(data_array, "black")
    graph(medianBin(data_array, 3), "red")
    plt.show()