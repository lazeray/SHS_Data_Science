import requests
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


if __name__ == "__main__":
    name = input("Enter jstris username: ") # gets jstris username
    url = "https://jstris.jezevec10.com/u/"+ name + "/stats"  # jstris data url
    contents = download_webpage_as_html(url)
    print(contents)

    
    start_index = contents.find('"unused":[')
    end_index = contents.find("}]", start_index) + 2
    input_data = contents[start_index+10:end_index-1]
    print(input_data)
    


