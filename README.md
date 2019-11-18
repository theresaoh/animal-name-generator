Animal Name Generator
=====================

Do you have a new pet? Can't think of great names like "Naptime Allstar", "Captain Karen", "Grampy", or "Spinach" on your own? Then this is the program for you! C'mon, there are too many cats out there named "Socks" anyway.

This program was created in order to assist staff and volunteers at local animal shelters with naming animals. After working in a shelter environment for a while, it can be difficult to come up with unique names for the animals, and many programs of this kind have a limited subset of names, or names along a specific theme. While this program was developed with shelter staff in mind, it's great for anyone anywhere with an animal in need of a great name.

Features
--------
Access over 95,000 names (Names.csv provided here only has about 2,000 names), sorted by gender (female, male, gender-neutral)
Temporarily set names aside to continue generating new names without losing names you like
Register and log in as a user
As a registered user, favorite names to be viewed at any time on your favorites page
View character names from the top 20 currently trending movies
Add names to the database

Requirements
------------
* Node JS
* Python 3.7+
* Pipenv
* SQLite3

Installation & Running Locally
------------------------------
    * Open terminal and cd into the folder in which you'd like this project to live
    * `git clone https://github.com/theresaoh/animal-name-generator.git`
    * `cd animal-name-generator`
    * Configure Environment variables (instructions below)
    * Open another terminal tab
    * *In one tab:*
        * `cd server`
        * `pipenv install`
        * `touch .env`
        * `code .env` Follow instructions for .env file below
        * `pipenv run python main.py`
    * *In the other tab:*
        * `cd client`
        * `npm install`
        * `npm run build`

Environment Variable Configuration
----------------------------------
Within the `server` folder, create a file called `.env`. In it, fill in the following values:
    - RUN_ENVIRONMENT=local
    - SECRET_KEY =*enter a secret key here*
    - API_ROOT = https://api.themoviedb.org/3
    - API_TOKEN = *register for a api_key with the API above and enter it here*


Environment Variable Configuration
----------------------------------
>Within the `server` folder, create a file called `.env`. In it, fill in the following values:
    ```
    RUN_ENVIRONMENT=local
    SECRET_KEY =*enter a secret key here*
    API_ROOT = https://api.themoviedb.org/3
    API_TOKEN = *register for a api_key with the API above and enter it here*
    ```

Deployment Configuration (How can they deploy it if they want to)
   - Setting Up an AWS RDS PostgreSQL Instance (Or SQLite3)

Configuring the Database (if you need to seed a db, or any other db config steps)

Next Steps
----------
>Here are some features I'd like to add in the future:
    * Advanced search (e.g. names starting with or ending with a letter/letters)
    * Top favorited names viewable by any user
    * Giving users the ability to view a list of any names they've added to the database
    * Giving users the ability to favorite or set aside names from the movies-names page