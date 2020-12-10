#README

#### Overview

cactushugger is hosted on heroku, it has an integrated deployment pipeline with GitHub and 
sits on a heroku postgres database (which is actually hosted on AWS RDS)


#### Updating Requirements

As simple as updating requirements.txt and pushing to master, heroku will handle the rest


#### Running Migrations in production

Once logged into the heroku CLI, simply run

```heroku run python manage.py migrate```
