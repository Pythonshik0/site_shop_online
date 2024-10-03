
# Clothing store \ Магазин одежды


Technologies used:
    Django, PostgreSQL


<hr>


## How to install?

```bash
git clone https://github.com/devvsima/salamis-project.git
cd salamis-project
```
### Virtual environments ".venv"

Linux:
pip3 install -r requirements.txt
```bash
python3 -m venv .venv
source .venv\bin\activate
```
Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
`.venv` you can change it to another name


### Configure environment variables
Copy file `.env.dist` and rename it to `.env`
```
$ cp .env.dist .env
```
Than configure variables
```bash
$ vim .env
# or 
$ nano .env
```
### .env settings:
server_debug=True
server_port=80
server_ip=138.197.184.125
server_domain=devsima.site

`server_debug` - True/False debug mode <br>
`server_port` - port django <br>
`server_ip` - your server ip <br>
`server_domain` - domen example - "salamis.shop" <br>


Dababase postgres <br>
`DB_NAME` - database name <br>
`DB_HOST` - database host <br>
`DB_PORT` - database port <br>
`DB_USER` - user with access to the database <br>
`DB_PASS` - database password <br>

<hr>

### Once you have filled the .env with your config, you can run the project.

Making migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Сreate admin user:
```bash
python manage.py createsuperuser
```

Start Django:
```bash
python manage.py runserver
```
