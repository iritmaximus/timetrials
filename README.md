# Tsoha-project

## Forum

The subject of the project is a forum. Just a simple forum that one can log into and make/view posts and commend etc.
Sike, we are doing a database for time trial-times in video games. (Mostly Nintendo racing games = Mario Kart)
The main functionality is that one can add times to specific games and/or tracks and get a rank based on those
times (see https://www.mariokart64.com/mkdd/standardc.php)

## Database

The database will be PostgreSQL-based database hosted on fly.io.

### Tables (at least)
* users
* games
* cups
* courses
* standards
* times

### Fancier db things
* authenticated user can add times and edit old ones TODO
* other boring user/account things, can login
* can sort times by game, track, time and other things TODO

### Välipalautus 3
Most of the fancier db things are todo. This is sort of the MVP (minimun viable product).


## Deployment

The site is being deployed at https://tsoha-flask.fly.dev/

## Routes

### GET https://tsoha-flask.fly.dev/
Works as the main page, can navigate to other sites.

### GET [games](https://tsoha-flask.fly.dev/games)
List of games.

### GET [cups](https://tsoha-flask.fly.dev/cups)
List of cups

### GET [courses](https://tsoha-flask.fly.dev/courses)
List of all courses.

### GET [login](https://tsoha-flask.fly.dev/login)
Login page to the site. You will be redirected here, if you try to access other pages without a session (login in).

### GET [times](https://tsoha-flask.fly.dev/times)
List of all times submitted by the players. There is also a button to add new times.

### GET [create/time](https://tsoha-flask.fly.dev/create/time)
A page where you can submit new times, you have to be logged in for the submission to go through.

### GET [api/(game/cup/course)/id](https://tsoha-flask.fly.dev/api/)
You will be redirected to some of these from clicking any of the corresponding fields in the times.

## Note
If you get an error ´sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres´,
change your url from ´postgres://´ to ´postgresql://´.

## Local dev
### Requirements
If you want to run this locally, you need
* Virtual environment
* Proper .env file
* Docker and docker-compose installed (optional)

### Setting up
* Venv (virtual environment) can be achieved through running `python -m venv .venv` in the `timetrials` directory.
This will create the venv file to `timetrials/.venv` (a hidden file).
* `.env` needs to contain `POSTGRES_URL` and `SECRET_KEY`
- The `POSTGRES_URL` needs to be the full url to your postgres database, containing user, password and database
- `SECRET_KEY` is some random string that you need to create. One simple way is to launch the python interactive prompt with 
```bash
python
```
and then run the commands
```python
>>> import secrets
>>> secrets.token_hex(16)
```
and copy the result to the `SECRET_KEY` variable.

After that you can either build the app by running
```bash
docker-compose up -d
```

If you don't have or don't want to use docker, you can activate the venv by calling
```bash
source .venv/bin/activate
```
(google the proper way to do it if you are on Windows).
Then install the requirements with pip
```bash
pip install -r requirements.txt
```
and then you can just run the command
```bash
python run.py
```
