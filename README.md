# Foreshift Web Application

Foreshift is a Django Web Application that integrates a Machine Learning specifically MARS Algorithm. It predicts if the student who answers the 
survey has a risk to shift or not base from the features or factors on the survey questionnaire from the Web Application. It also includes machine learning
training code for training and testing our dataset.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Visual Studio Code
- Python
- xampp

### Installing

A step by step series of examples that tell you how to get a development
environment running

After you have downloaded the repository. Create an environment using:

    python  -m venv env (and then activate the environment by: )
    .//env/scripts/activate

Install all the requirements from the requirements.txt

    pip  -r install requirements.txt

Install the pyearth in the file: Go to the py-earth directory

    cd py-earth
    py setup.py install

Setup the database on the Xampp localhost by naming it foreshiftdb (give access) and migrate all the needed tables for it:

    py manage.py makemigrations
    py manage.py migrate

the run it.

    py manaage.py runserver

## Deployment

The Web Applicatioon is deployed using AWS EC2 cloud service.
You can check it out here: [Foreshift Web Application](http://13.212.229.116:8000/)

## Built With

  - Django Web Application
  - Python
  - JavaScript, HTML, CSS
  - VSCode

## Authors

  - **Christian John Bañez**
  - **Vea Therese Cruz** 
  - **Princess Nicole Salvador** 
  - **Ibanica Dionisio** 

## Acknowledgments

  - Mr. Jay Ryan Mapanao as our adviser for our thesis
  - Pamantasan ng Lungsod ng Maynila for letting us get the data needed for the thesis

