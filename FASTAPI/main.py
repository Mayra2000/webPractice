from fastapi import FastAPI  # Import the FastAPI class used to create the web application

app = FastAPI()  # Create an instance of the FastAPI application

# @app.get("/")  # Register this function as the handler for GET (read) requests to the root URL
# def read_root():  # Define the function that runs when the root URL is requested
#     return {"Hello": "World"}  # Return a JSON response containing a greeting

# @app.post("/items/")  # Register this function as the handler for POST (create) requests to the /items/ URL
# def create_item(name:str, price: float):  # Define the function that runs when a POST request is and the request body contains 'name' and 'price' parameters
#     return {"name": name, "price": price} # Return a JSON response containing the name and price of the item that was created

# @app.put("/items/{item_id}")  # Register this function as the handler for PUT (update) requests to the /items/{item_id} URL
# def update_item(item_id: int, name: str, price: float):  # Define the function that runs when a PUT request is made to update an item with a specific ID
#     return {"item_id": item_id, "name": name, "price": price}  # Return a JSON response containing the updated item information

# @app.delete("/items/{item_id}")  # Register this function as the handler for DELETE (delete) requests to the /items/{item_id} URL
# def delete_item(item_id: int):  # Define the function that runs when a DELETE request is made to delete an item with a specific ID
#     return {"item_id": item_id, "message": "Item deleted"}  # Return a JSON response confirming the deletion of the item

##Path Parameters: Path parameters are used to capture values from the URL path. In this code, the `item_id` 
# parameter is a path parameter that allows the user to specify which item they want to update or delete. 
# The value of `item_id` is extracted from the URL and passed to the corresponding function as an argument.

# @app.get("/users/{user_id}")  # Register this function as the handler for GET (read) requests to the /users/{user_id} URL
# def read_user(user_id:int):  # Define the function that runs when a GET request is made to retrieve information about a user with a specific ID
#     return {"user_id": user_id}  # Return a JSON response containing the user ID 

##Query Parameters: Query parameters are used to pass additional information in the URL. 
# In this code, the `name` and `age` parameters are query parameters that allow the user 
# to filter the results of the request. The values of `name` and `age` are extracted from 
# the URL and passed to the corresponding function as arguments.

# @app.get("/users/")  # Register this function as the handler for GET (read) requests to the /users/ URL
# def read_users(user_id: int, name: str, age: int = None):  # Define the function that runs when a GET request is made to retrieve information about users, with optional query parameters for name and age
#     return {"user_id": user_id, "name": name, "age": age}  # Return a JSON response containing the user ID, name, and age of the user(s) requested

##Use both parameters

@app.get("/users/{user_id}/details")
def read_user_details(user_id:int, include_mail:bool = False):
    if include_mail:
        return {"user_id": user_id, "email": "user@example.com"}
    else:
        return {"user_id": user_id}

#Example of url: http://127.0.0.1:8000/users/10/details?include_mail=true
#in this example, the user_id is a path parameter and include_mail is a query parameter. 
# The function will return the user ID and email if include_mail is set to true, otherwise it will only return the user ID.