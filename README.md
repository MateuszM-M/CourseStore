# CourseStore

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

## General info

CourseStore is an app in early stage of development, created for learning purposes. My main focus is to acquire knowledge in Docker, CI/CD, pytest, Django Class Based Views.

## Technologies

 - Python
 - Django
 - Docker
 - TravisCI
 - Pytest
 - Factory-boy
 - Postgreql
 - Heroku

## Features

These tasks has been accomplished thus far or I am in the process of doing them:

 - Separate setting for environments
 - Create preliminary DB models
 - Set up initial CI process in CirleCI
 - Set up docker and docker-compose
 - Add first class based view
 - Register and login
 - Add preliminary layout

Currently, I am trying to establish CI/CD process in CircleCI that will include building Django app and postgres DB, run tests with factoryboy fixtures and automatically deploy on Heroku.

## To do

 - CRUD views for courses
 - Cart
 - Ordering courses
 - Search

 ## Setup 

Clone repo `git clone https://github.com/MateuszM-M/CourseStore`,

Rename src/CourseStore/settings/`.env-example` to `.env`

compose app `docker-compose up`,

Browse http://127.0.0.1:8000/

Or

Online demo: https://course-store-x.herokuapp.com/
