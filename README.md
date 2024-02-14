# To Do List

## Description
REST API for task management (To-Do List). Simple REST API to add, update, and delete tasks in your to-do list.

Tools:
- Django +DRF
- PostgreSQL

Functionality:
- Adding a new task
- Getting a list of all tasks
- Update task status (completed/not completed)
- Deleting a task


## Set Up your personal settings
Create a `.env` configuration file with your personal settings in the root of the project, according to the sample, specified in `.env.sample`. Fill out the file according to your personal data. 

Create a database in postgresql. The name of the database must match the name specified in the file.

## Running
Run migrations using the command `python manage.py migrate`.

To run the project, enter the `python manage.py runserver` command in the terminal.
Now you can start using the project with http://127.0.0.1:8000/tasks/ link!

Detailed documentation can be found here: http://127.0.0.1:8000/docs/
or here: http://127.0.0.1:8000/redoc/