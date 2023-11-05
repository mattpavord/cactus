#README

#### Overview

Cactushugger is an app that provides notifications on when to water a cactus, based on when it rains in the
cactus' native desert. 

Cactushugger is hosted on heroku, it has an integrated deployment pipeline with GitHub and 
sits on a heroku postgres database (which is actually hosted on AWS RDS)

Disclaimer: I wrote this code in 2020 when I was relatively junior, my coding ability has come on significantly since this time.

#### Updating Requirements

As simple as updating requirements.txt and pushing to master, heroku will handle the rest


#### Running Migrations in production

Once logged into the heroku CLI, simply run

```heroku run python manage.py migrate```
