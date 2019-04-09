# DB Project
Database project

Assignment report on overleaf [here](https://www.overleaf.com/16613395pjytnbwkjqsg#/63779068/) or a local copy [here](https://github.com/martchellop/DB_Project/blob/master/BD_T3.pdf).

# Requirements

- [Python3](https://www.python.org/)

- [PostgreSQL](https://www.postgresql.org/)

# Installation:

Install required python packages:

`pip3 install -r src/requirements.txt`

Create a database named `db_project` on Postgres

`sudo psql -u postgres createdb db_project`

Populate the database

`python3 src/queries.py`

# Running:

Initialize the graphical interface:

`python3 src/main.py`

# Showcase:

![](https://github.com/martchellop/DB_Project/blob/master/imgs/inicializandoGUI.png)
