import requests

# Define the base URL of your Flask API
base_url = 'http://127.0.0.1:5000/api'  # Update with your API URL

# Function to send a POST request to create a new person
def create_person(name):
    data = {"name": name}
    response = requests.post(f"{base_url}", json=data)
    return response

# Function to send a GET request to fetch details of a person
def get_person(user_id):
    response = requests.get(f"{base_url}/{user_id}")
    return response

# Function to send a PUT request to update a person's details
def update_person(user_id, name):
    data = {"name": name}
    response = requests.put(f"{base_url}/{user_id}", json=data)
    return response

# Function to send a DELETE request to remove a person
def delete_person(user_id):
    response = requests.delete(f"{base_url}/{user_id}")
    return response

if __name__ == '__main__':
    # Test the API operations
    # Create a new person
    create_response = create_person("John Doe")
    print("Create Person Response:", create_response.json())

    # Fetch details of the created person (assuming the ID is 1)
    get_response = get_person(1)
    print("Get Person Response:", get_response.json())

    # Update the person's details
    update_response = update_person(1, "Jane Doe")
    print("Update Person Response:", update_response.json())

    # Delete the person
    delete_response = delete_person(1)
    print("Delete Person Response:", delete_response.json())
