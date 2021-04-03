# Learning_Flask
This is my personal repo to learn web developments.

# Week1 dificulties

### issue

desc="No web processes running"

### Resolution
- ###scale your web dyno

heroku ps:scale web=1

using Heroku CLI

# Week2 dificulties
- ### Connecting with a data base and deploy to Heroku

### issue
Why is SQLAlchemy 1.4.x not connecting to Heroku Postgres?

When using SQLAlchemy 1.4.x to connect to Heroku Postgres, I receive the following error:
sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres

### Resolution
SQLAlchemy 1.4.x has removed support for the postgres:// URI scheme, which is used by Heroku Postgres (https://github.com/sqlalchemy/sqlalchemy/issues/6083). To maintain compatibility, perform the following before setting up connections with SQLAlchemy:

import os
import re

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


- ### how to copy csv data to Heroku
How do I copy a CSV file into a Postgres Table?
### Issue
You want to copy a .csv file from your local machine to a Heroku Postgres table.

### Resolution
Run heroku pg:psql -a <application_name>.

Once the Postgres shell opens, run

DATABASE=> \copy table_name FROM csv_file.csv WITH (FORMAT CSV);