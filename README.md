# DB_Project
Final project of data base

Assignment report on overleaf [here](https://www.overleaf.com/16613395pjytnbwkjqsg#/63779068/)

# Installation:

[Python3](https://www.python.org/) and [PostgreSQL](https://www.postgresql.org/) are required. For installing the necessary libs, just run:

`pip3 install -r src/requirements.txt`

Create the database named `db_project` on postgres

`sudo psql -u postgres createdb db_project`

Populate the database

`python3 src/queries.py`

# Running:

Initialize the graphical interface with

`python3 src/main.py`
