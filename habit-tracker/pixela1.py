import requests 

import datetime

import os

# Get token from environment variable or prompt if missing
token = os.environ.get('token') or input("Enter your Pixela Token: ")

today = datetime.datetime.now()

username = os.environ.get('username')






pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'X-User-Token' : token , 
    'username' : username , 
    'agreeTermsOfService' : 'yes' ,
    'notMinor' : 'yes'
}

graph_config = {
    'id' : 'graph1' ,
    'name' : 'Habit Graph' , 
    'unit' : 'times' , 
    'type' : 'int' , 
    'color' : 'sora'
}

# new_endpoint = 'https://pixe.la/v1/users/omarayman/graphs'

# response = requests.post(url=new_endpoint , json=graph_config , headers=user_params)

# print(response.text)

today = today.strftime('%Y%m%d') 

new_new_endpoint = f'https://pixe.la/v1/users/omarayman/graphs/graph1/{today}'


pixel_config = {
 
    'quantity' : '3' 

}

# response = requests.post(url=new_new_endpoint , json=pixel_config , headers=user_params)

# print(response.text)

def print_status(response):

    # ANSI color codes for terminal text styling
    
    GREEN = "\033[92m"

    RED = "\033[91m"

    RESET = "\033[0m"

    try:

        data = response.json()

        is_success = data.get("isSuccess", False)

        message = data.get("message", "No message provided.")

        if response.ok and is_success:

            print(f"\n{GREEN}✅ Success ({response.status_code}): {message}{RESET}\n")

        else:

            print(f"\n{RED}❌ Error ({response.status_code}): {message}{RESET}\n")

    except ValueError:

        # Fallback if response isn't JSON
        
        print(f"\nStatus Code {response.status_code}: {response.text}\n")



def main():

    while True:

        input1 = input('\nWhat would you like to do with pixela today 1 Update / Create a pixel or 2 Delete a pixel or perhaps quit 3 ')

        if input1 == '1':

            input2 = input('\nHow many times ')

            pixel_config["quantity"] = input2

            response = requests.put(url=new_new_endpoint , json=pixel_config , headers=user_params)

            print_status(response)
        elif input1 == '2':

            response = requests.delete(url=new_new_endpoint , headers=user_params)

            print(response.text)
        elif input1 == '3':

            break
        else:

            print('\ninvalid input please provide a valid input\n')    

    
main()