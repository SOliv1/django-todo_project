<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

View the live site [HERE](https://sjo-django-todo.herokuapp.com/)

Welcome Sara Oliver,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.


# Django Fullstack Frameworks - Heavy Duty

The Django framework comes with much more features and functionality out of the box than a
framework like flask which is why we usually refer to *Django as a framework that
comes with batteries included*. Django follows a strict pattern called **Model
View Template. Template** being the HTML or the presentation layer. The *View* layer
being the logic that provides the templates with the context users will be
viewing. Models are the data *models* that we use to *model* our data.
We will be using Django to look at the MVC style pattern, which is where MVT (Model View Template) pattern comes from.
MVT is a child of MVC. We will be connecting all the different aspects of the MVC pattern
together so we start with the models - we'll be getting data from the models
and doing some form of manipulation with it in the view and then
presenting it to a user. And then getting information from a template to a view to
a database. We'll be looking at ranked using Django's built in *admin* panel.


To run django command in fullstack 
`python3 manage.py runserver`

## django
1.  What command do we need to 
run to create a new Django project?
django-admin startproject .

1.  What does the . signify in the startproject command?
Create the project in this directory  

1.  What class did we extend in order to create the form?
forms.ModelFormcorrect

1.  python3 manage.py migrate command will
use the migration files to apply changes to a database

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

## tests
go to tests.py

*picks up on file*
    names that start with the test (or test_) and
    it will run all of the tests that they contain.
    To do this
    it will check all of those files for any methods that begin with
    test_. 

To run tests with command in django:
`python3 manage.py test`

Install and use coverage command:
`pip3 install coverage` 
run coverage command:
`coverage run --source=todo manage.py test`
runa coverage report:
`coverage report`
`coverage html`
Create folder for coverage html-creates a folder 
rage HTML command actually generates a new folder
called htmlcov and inside of that, a file called
index.html and run this file then and open it in the browser and it
will actually give an HTML output of our coverage and we can see then
we click on these files and we can see any lines here that actually haven't been
covered by our tests will be highlight.

## Heroku platform and installing project requirements. 
`pip3 install gunicorn` -the server that will run our project
 
`pip3 install psycopg2`  - allows us to connect PostgreSQL database so instead of using MySQL or SQLite for this we'll be
using a Postgres database and the reason for this is that Postgres is very
easy to setup on Heroku to really encourage it we can get it up.

`heroku create`

`heroku login`

`heroku apps`

`git remote -v`

`heroku help` view help info

`git push origin master`  push to github && heroku
`git push heroku master`

`heroku addons` Allows us to create and manage addons for applications using this command.
`heroku addons:create heroku-postgresql:hobby-dev`

`pip3 install dj_database_url`connects to out database A package that parses database URIs
by installing it and referencing it in the settings.py file

`pip3 freeze --local > requirements.txt`


`config vars`to view dashboard url

settings.py then copy and paste configs string from heroku config vars reveal, and import dj_database_url
return to terminal and command:
`python3 manage.py migrate`

my migration should now be applied and there we go we've successfully connected
to a Postgres database hosted on heroku
through Django

Debugging
`heroku config:set DEBUG_COLLECTSTATIC=1`

Disabling Collectstatic
`heroku config:set DISABLE_COLLECTSTATIC=1`

fully disables the collectstatic step of the build.

run development server
`python3 manage.py runserver $IP:$PORT`
Export development
`export DEVELOPMENT=1`
run development server again
echo "env.py" >> .gitignore

#Then git status then git add then git commit -m ""
`git status`
`git add django_todo/settings.py` 
`git commit` -m "git
commit -m I would say implement environments specific values for the
debug and database"

https://miniwebtool.com/django-secret-key-generator/  SECRET_KEY generator

#assign one to env.py and the other to Heroku:

*export "SECRET_KEY" = ''
*secret key has been et on both our development department and our production environment on Heroku

`heroku config:set SECRET_KEY=`
echo "env.py" >> .gitignore

ls -a 
nano .gitignore
git status
----

tpod Reminders
Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
