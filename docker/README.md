# Steps to set up Demo locally

## 1. Prerequisites

1. Make sure you have logged into your AWS porfile both in the browser and through the CLI in your local terminal of choice

    `aws sso login --profile [PROFILE_NAME]`

2. export your current AWS profile in your terminal. This will prevent you from having to login in every terminal you open.

    `export AWS_PROFILE=[PROFILE_NAME]`

3. Login into AWS ECS using the following command. For future preperations bare in-mind the region and account ID

    `aws ecr get-login-password --region af-south-1 | docker login --username AWS --password-stdin 761183306127.dkr.ecr.af-south-1.amazonaws.com`

4. Should you have an error with the above command (It is probably because you installed Docker Desktop on Windows... ). 

    `Error saving credentials: error storing credentials - err: exit status 1, out: error storing credentials - err: exit status 1, out: The stub received bad data.`

    Then you will have to navigate to your .docker/config file and remove 
    
    `"credsStore": "desktop.exe"`

    or

    `An error occurred (ExpiredTokenException) when calling the GetAuthorizationToken operation: The security token included in the request is expired`

    Then your AWS session has expired and repeat the prerequisites mentioned above.

## 2. Running The Environment

1. Make sure you are in the root folder of the front-end solution and run the following command.

    Start Containers: `docker compose -f docker/docker-compose.yml up`

    Stop Containers: `docker compose -f docker/docker-compose.yml stop`

2. Once the docker containers have been set up. Run the following commands in your terminal

    `npm i && npm run start`


## 3. Connecting to your local postgres

1. Run the following command in the root directory.

    `./docker/postgres/docker_inspect.sh`

    It should then produce a `ipadress.json` file in the same directory used above. 

    In that file it should generate a json object with a single/multiple entries, using the latest entry (The bottom entry), find the following field `"IPAddress":"[CUSTOM_IP_ADDRESS]"`.
2. Using that IP Address, navigate to `localhost:5050` (PGAdmin).
    
    Preferrably use Chrome Browser, as PGAdmin Docker has issues with other browser platforms
    
    Suggestion: Save the Page as a progressive webapp to your desktop -> [How to save a webpage to your desktop](https://www.laptopmag.com/articles/how-to-create-desktop-shortcuts-for-web-pages-using-chrome).
3. The Login in credentials for PGAdmin are in `docker/postgres/.env`.
4. Login and create a server as normal. When asked for a HOST us the IP Address obtained above.

# Important 🔥🔥🔥
Make sure you do not have any other services running on the same ports.
