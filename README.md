Animal Name Generator

Do you have a new pet? Can't think of great names like "Naptime Allstar", "Captain Karen", "Grampy", or "Spinach" on your own? Then this is the program for you! C'mon, there are too many cats out there named "Socks" anyway.

This program was created in order to assist staff and volunteers at local animal shelters with naming animals. After working in a shelter environment for a while, it can be difficult to come up with unique names for the animals, and many programs of this kind have a limited subset of names, or names along a specific theme. While this program was developed with shelter staff in mind, it's great for anyone anywhere with an animal in need of a great name.

Installation
    - Open terminal and cd into the folder in which you'd like this project to live
    - `git clone https://github.com/theresaoh/animal-name-generator.git`
    - `cd animal-name-generator`
    - Open another terminal tab
    - *In one tab:*
        - `cd server`
        - `pipenv install`
        - `touch .env`
        - `code .env` Follow instructions for .env file below
        - `pipenv run python main.py`
    -*In the other tab:*
        - `cd client`
        - `npm install`
        - `npm run build`

    Requirements

Running Locally ( what commands used to run locally)

Features (what your app can do)

Environment Variable Configuration (What they need in the .env file)

Deployment Configuration (How can they deploy it if they want to)
   - Setting Up an AWS RDS PostgreSQL Instance (Or SQLite3)

Configuring the Database (if you need to seed a db, or any other db config steps)

Caveats and Good-To-Knows (IMPORTANT [every app has it’s warts, please document them here])

Next Steps (What are the next planned features for the app’s development)
