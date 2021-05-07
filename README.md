# How to start the server

* Use `bootstrap.sh` to install all requirements and to do all migrations and load fixtures.



# Backend Assignment: Simple Todos and Reminder API

The assignment involves the creation of a TODO and Reminder REST JSON API using Django. Please use the following libraries and versions:

* Python 3.5+
* Django 2.0+
* Django Rest Framework 3.8+
* Celery 4.1+

**Updated @ Nov'18**

## Simple TODO API (1-3h)

Create a CRUD API for a simple TODO Management application. TODOs are organized in boards, on every board there can be multiple TODOs. A TODO contains a title (str), done (bool), a created (datetime) and updated (datetime) timestamp. A board has a name (str). 

Via a REST API it must be possible to:

*   List all boards
*   Add a new board
*   Change a board's title
*   Remove a board
*   List all TODOs on a board
*   List only uncompleted TODOs
*   Add TODOs to a board
*   Change a TODOs title or status
*   Delete a TODO

User management and authentication is are required.

### Constraints

*   When listing all boards the JSON should have a todo_count field, but not the list of all todos
*   In the board's detail view all todos should be serialized and the todo_count should not be visible

## Reminder API (1-2h)

Another endpoint should allow the user to set reminders. A reminder contains an email address, a reminder text and a delay in minutes when it will be triggered. 

Via the REST API it must be possible to:

*   List all reminders
*   Create a new reminder
*   Remove a reminder

After the user provided delay the user should receive an email. If you don't want to work with email it's ok to replace the email address with a callback URL and to POST the serialized reminder to this URL.

### Constraints

Please use celery to implement the delayed execution.

## How to work on the assessment

*   Clone this repository
*   Start working on the assignment
*   Please do periodic commits with meaningful commit messages
*   Once you are done push your final results
*   If you don't want to create a public repository please invite (@phelmig, @erzaehlsalex, @flore2003) to your working repository
*   Please include a brief description how to run your solution
*   If you have any questions contact us (jobs@rocketloop.de)

Please note that we don't accept solutions without periodic commits or if we are unable to execute the solution.

