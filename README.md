# A4_CC_Project

This repository is dedicated to the end of semester project for the Cloud Computing course at ESILV Paris, in A4 CCC.

This project consits in creating a dockerized application that will get the weather of a city and store it in a database.

## Prerequisites

1. Fork this repository then clone it on your computer
2. Install docker and docker-compose on your computer
3. create a `secrets` folder at the root of the project:
   1. in this folder you must create a `db_root_password.txt` file containing the password for the root user of the database
   2. in this folder you must create a `db_user_password.txt` file containing the password for the user of the database
4. Create a `.env` file containing (replace with your data):
    > API_KEY=your-api-key (for the service openweathermap.org)<br>
    > DB_NAME=your-db-name (defined in [sql/init.sql](sql/init.sql))<br>
    > DB_TABLE=your-db-table (defined in [sql/init.sql](sql/init.sql))<br>
    > DB_USER=your-db-user (defined in [docker-compose.yml](docker-compose.yml) line 14)<br>
    > DB_PASSWORD=your-db-password (defined in [db_user_password.txt](secrets/db_user_password.txt))<br>
5. create a `city.txt` file at the root of the project containing the name of the city you want to get the weather for
6. Run the containers with `docker-compose up -d`

## Quick information

