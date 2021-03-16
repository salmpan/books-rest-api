# books-rest-api
A sample Django REST API application implemented for demonstration purposes.

## Functionality
All requests and responses are in JSON format.

| Method | Endpoint              | Action(s) |
| ------ | --------------------- | --------- |
| GET    | /api/books/           | Retrieves a list of books, ordered by the author's last name and then by the PK of the book. Only visible books having a publisher are shown. |
| GET    | /api/book/:id         | Returns detailed information for a specific book based on its PK. |
| POST   | /api/add-author/      | Adds a new author entry to DB. |
| POST   | /api/add-publisher/   | Adds a new publisher entry to DB. |
| POST   | /api/add-book/        | Adds a new book entry to DB. |
| PATCH  | /api/upd-book/:id     | Updates an existing book entry based on its PK |
| DELETE | /api/del-book/:id     | Deletes an existing book entry based on its PK |

## Installation
book-rest-api can be run via a virtual environment or as a dockerized app.

### Requirements
* Python 3.8
* all dependencies included in requirements.txt
* SQLITE DB is used

### Using containers
Note: Docker and docker-compose should be already installed in the system.

```
git clone https://github.com/salmpan/books-rest-api.git
cd books-rest-api
docker-compose up --build
```

If this is the first time running the app, access docker container shell in order to run migrations and (optionally) run the custom script in order populate DB with some entries:

```
docker exec -it <container id> /bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py runscript populate_db
exit
```

## Tests
In order to run unit tests, simply: ```python manage.py test```
