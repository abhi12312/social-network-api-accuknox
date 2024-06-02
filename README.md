# social-network-api-accuknox
A social network project based on django rest framework


## Prerequisites

- Linux (Preferably Ubuntu 20.04.5)
- Python 3.10+ (Preferably 3.10)
- pip
- virtualenv
- docker

## Installation

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/abhi12312/social-network-api-accuknox.git

2. Navigate to Git Repository
    ```bash
    cd social-network-api-accuknox/

3. Create Virtual Environment
    ```bash
    python3 -m venv env

4. Activate Virtual Environment
    ```bash
    source env/bin/activate/

5. Navigate to Django Project   
    ```bash
    cd social_network

6. Run docker command
    ```bash
    docker compose up --build    

After running the Docker command, you can access the API endpoints at:

- Base URL: http://localhost:8000/
- Endpoints:
  - POST  api/login/  (Login) 
  - POST  api/signup/  (Sign Up) 
  - GET   api/users/  (User Lisiting)  
  - POST  api/friend-requests/send/ (Send a friend request)
  - PUT   api/friend-requests/{id}/accept/ (Accept a friend request)
  - PUT   api/friend-requests/{id}/reject/ (Reject a friend request)
  - GET   api/friends/ (List of friends)
  - GET   api/pending-requests/ (List of pending friend requests)

Please ensure you have the necessary authentication tokens or credentials to access authenticated endpoints.


## Postman Collection
You can import the Postman collection for testing the API endpoints using the `postman_collection.json` file.



