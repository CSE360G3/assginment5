### README
This is the skeleton for image hosting and editing app called ImageSpace in Django Python.

## To setup project

* Install virtualenv with `easy_install virtualenv`

* Go to a directory workspace and create new virtual environment by `virtualenv <ENV-NAME>`

* activate environment with `source <ENV-DIRECTORY>/bin/activate`

* do `easy_install pip`

* Install dependencies with `pip install -r image_space/requirements.pip`

* Run server with `python manage.py runserver`

* Go to your web browser and open "http://localhost:8000"


*The UI is built with twitter bootstrap, less and jquery*


The home page does nothing other than taking email and password. If you click on the 'sign in' you will be taken to the same home page.


## To run sample unit test

* run `python manage.py test image_space_app/tests`

The source file for test is at image_space/image_space_app

## To run sample functional test

*run `python manage.py harvest`

*The functional test is written on Lettuce steps. You can see the tests at image_space/image_space_app/features folder*
