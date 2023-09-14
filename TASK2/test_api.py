import requests
import json

# base url of FLASK API
# base_url = 'http://127.0.0.1:5000/api'  
base_url = 'https://task2-api.onrender.com/api'

# Function to print response nicely
def pretty_print_response(response):
    print(f"Response Status Code: {response.status_code}")
    try:
        data = response.json()
        print(json.dumps(data, indent=4))
    except ValueError:
        print(response.text)

# Function to create a person
def create_person(name):
    data = {"name": name}
    response = requests.post(f"{base_url}", json=data)
    return response

# Function to retrieve a person
def get_person(user_id):
    response = requests.get(f"{base_url}/{user_id}")
    return response

# Function to update a person
def update_person(user_id, name):
    data = {"name": name}
    response = requests.put(f"{base_url}/{user_id}", json=data)
    return response

# Function to delete a person
def delete_person(user_id):
    response = requests.delete(f"{base_url}/{user_id}")
    return response

if __name__ == '__main__':
    # Testing the API operations
    # Create a new person with a valid name
    create_response = create_person("John Doe")
    print("Create Person Response:")
    pretty_print_response(create_response)

    # Create a new person with an invalid name (non-string)
    create_response = create_person(123)
    print("Create Person Response (Invalid Name):")
    pretty_print_response(create_response)

    # Fetch details of the created person (assuming the ID is 1)
    get_response = get_person(1)
    print("Get Person Response:")
    pretty_print_response(get_response)

    # Fetch details of a person that does not exist (assuming the ID is 100)
    get_response = get_person(100)
    print("Get Person Response (Non-Existent ID):")
    pretty_print_response(get_response)

    # Update the person's details with a valid name
    update_response = update_person(1, "Jane Doe")
    print("Update Person Response:")
    pretty_print_response(update_response)

    # Update the person's details with an invalid name (non-string)
    update_response = update_person(1, 123)
    print("Update Person Response (Invalid Name):")
    pretty_print_response(update_response)

    # Delete the person
    delete_response = delete_person(1)
    print("Delete Person Response:")
    pretty_print_response(delete_response)
