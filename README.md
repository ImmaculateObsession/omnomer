# Omnomer
### All your stuff is belong to you
***
Omnomer is an inventory system built in Django.

Pre-requisites:
* A local postgres install. On a mac [PostgresApp](http://postgresapp.com/) is highly recommended and has pretty good docs.

To get started:

1. Clone this repo.

2. Create a virtualenv around the cloned repo

3. Install requirements using 'pip install -r requirements.txt'

4. Get the secret keys from one of the project maintainers.

5. Start playing around!

Full setup details (Mac):
1. Download [PostgresApp](http://postgresapp.com/) and go through the install.

2. Open the postgres app (an elephant icon should appear in the menubar)

3. Click the postgres menubar icon. Select psql.

4. At the psql prompt, enter "CREATE DATABASE omnomer;". This will create the omnomer db

5. Exit psql

6. Clone the repo to the location of your choice.

7. Create a virtualenv around the repo (virtualenv .)

8. Activate the virtualenv (. bin/activate)

9. Install dependencies (pip install -r requirements/local.txt)

10. Get the secret key from one of the project maintainers or create your own; set that key in an environment variable (export OMNOMER_KEY=...) - not necessary if you are using local settings.

11. Cd into the omnomer directory (omnomer/src/omnomer)

12. Attempt to sync the db (python manage.py syncdb --settings=omnomer.settings.local)
