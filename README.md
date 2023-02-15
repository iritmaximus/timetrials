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
* authenticated user can add times and edit old ones
* other boring user/account things, can login
* can sort times by game, track, time and other things

## Deployment

The site is being deployed at https://tsoha-flask.fly.dev/

## Routes (Mostly TODO)

### GET https://tsoha-flask.fly.dev/
Just to test if the site works

### GET [db](https://tsoha-flask.fly.dev/db)
Just to test if the db works (at the moment)

### GET [games](https://tsoha-flask.fly.dev/games)
TODO will be list of all games and other relevant information

### GET [cups](https://tsoha-flask.fly.dev/cups) (TODO, not yet a route)
TODO will be list of all cups and other relevant information

### GET [courses](https://tsoha-flask.fly.dev/courses)
TODO will be list of all courses and other relevant information

### GET [login](https://tsoha-flask.fly.dev/login)
TODO will be used to login to the site, html template already in use, doesn't do anything meaninful yet.


## Note
If you get an error ´sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres´,
change your url from ´postgres://´ to ´postgresql://´.
