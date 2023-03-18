![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

[![CI Django & Postgres Tests](https://github.com/SpaceyaTech/blog/actions/workflows/django-postgres-ci.yml/badge.svg)](https://github.com/SpaceyaTech/blog/actions/workflows/django-postgres-ci.yml)

# Mastori: A SpaceYaTech Blog App made in Django
Mastori is a community-driven open-source project that aims to provide a simple and efficient blogging platform built with the Django Rest Framework. 

# Overview

The SpaceYaTech Content Management system is an open-application that lets users to quickly publish content and share it with ease to their audience. Inspired by existing CMSes like Hashnode, Wordpress, DEV and Joomla, we felt the need to create an African CMS created by young Africans looking to learn by contributing to Open Source. SpaceYaTech opted for a CMS as the debut open source project because of the technicalities involved in creating, maintaining and scaling a CMS. A CMS poses great technical challenges and a great learning opportunity for those looking to grow their tech skills.
For a more detailed overview of the project, read through the [CMS Backend wiki](https://github.com/SpaceyaTech/CMS-Backend-Repository/wiki) 

The project is designed to help developers build their own blogging website or add blogging functionality to an the SpaceYaTech website with ease.

# Endpoints 
```sql
/mastori/
 ```
 The `/mastori/` endpoint allows retrieving all blog posts. GET requests to this endpoint retrieve a list of all blog posts 
> For complete documentation. [Mastori Api Documentation](https://github.com/SpaceyaTech/mastori-backend/wiki/Endpoints)
## Authentication
```sql
/mastori/token/
```
## Users
```sql
    /register/
    /login/
```
## User Accounts
```sql
    /accounts/
    /accounts/id/
```
## Blog Posts
```sql 
    /mastori/
    /stori/id/
    /account/id/stori/
    /account/id/stori/id/
```
## Comments
```sql
    /stori/id/comments/
    /stori/id/comment/id
    /account/id/stori/id/comment/
    /account/id/stori/id/comment/id/
```
## Reactions
```sql
    /stori/id/reactions/
    /stori/id/reaction/id
    /account/id/stori/id/reaction/
    /account/id/stori/id/reaction/id/
```
# Features
Mastori provides the following features:

* Create, edit and delete blog posts
* Publish, unpublish or delete blog posts
* Tagging and categorizing posts
* Searching for posts by title, content, tags or categories
* User authentication and authorization
* User profile management
* Installation
> To install Mastori, follow these steps:

- Clone the repository:
            ```bash

            git clone https://github.com/yourusername/mastori.git
            ```
- Create a virtual environment and activate it:

    ```bash

            python -m venv env
            source env/bin/activate
     ```
- Install the required packages:
    ```bash
            pip install -r requirements.txt 
    ```
- Set up the database:
    ```bash
            python manage.py migrate
    ```
- Create a superuser:
    ```bash
            python manage.py createsuperuser
    ```
- Run the server:
    ```bash
            python manage.py runserver
    ```
# Usage
Once the server is running, you can access the API at `http://localhost:8000/api/`. You can use any HTTP client to interact with the API, such as curl or httpie. Alternatively, you can use the built-in API explorer by navigating to `http://localhost:8000/api/docs/` in your web browser.

To access the admin panel, navigate to `http://localhost:8000/admin/` and log in using the credentials of the superuser you created earlier.

## The blog Api

The blog api **{{baseurl}}/blog/**
shows a list of all available blog posts (Stori/Mastori)
The model naming is abitrary and can be subject to change if need be
Ther is also need to filter out the various blogposts in relation ti their tittle or date posted hence the filter

![Screenshot from 2023-01-03 00-59-16](https://user-images.githubusercontent.com/23496280/210282497-96bb8b6f-544d-4454-8b01-e3aea9b8745d.png)


# Contributing
We welcome contributions from the community. To contribute, follow these steps:

* Fork the repository
* Create a new branch
* Make your changes and commit them
* Push your changes to your forked repository
* Create a pull request

Please make sure to follow the coding style and conventions used in the project.

Get to read the [Contributions guide](https://github.com/SpaceyaTech/Team-Rio-Django/blob/main/contributions.md) here.

## Commit message template

Just so that we have all our commit messages to be more readable and sensible it is recomended we use a template for the commit messages. Here is a [commit message template](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/Commit-Messages) that one should follow when making your Contributions

# License
Mastori is licensed under the MIT License. See LICENSE for more information.

# Contributor Features
> Enviroment setup By @wanjirumurira [82d55a4](https://github.com/SpaceyaTech/blog/commit/82d55a45ea0421c3918a7b2ae2b5808486f879a3)

> Project Setup By @sangkips         [82bc556](https://github.com/SpaceyaTech/blog/commit/82bc556935ac134024b659233e012bb5c5da4fda)

> User & Accounts By @hellen-22      [1818b63](https://github.com/SpaceyaTech/blog/commit/1818b6304d203d0077bf54ff67151756db5d324a)

> PhoneNumberField By @sangkips      [615c011](https://github.com/SpaceyaTech/blog/commit/615c01194cebc205a743451bea9c5164e74bdf75)

> Authentication (JWT) By @hellen-22 [c2d7a90](https://github.com/SpaceyaTech/blog/commit/c2d7a90c9e644ba1c49ab02eb43d6e08da7022a3)

> Throttling policy By @Collins-Omariba [9159a8e](https://github.com/SpaceyaTech/blog/commit/9159a8ed389b3c7482c4b60c5fdc5576013bafd3)

> Verification richtext editor By @aibunny [25f991b](https://github.com/SpaceyaTech/blog/commit/25f991bed6aa163fe464a6bf2b28ccb6bbd82630)

> Fixed Workflow Build Error (commit #100) By @mosesmbadi [b40a5b4](https://github.com/SpaceyaTech/blog/commit/b40a5b4e0bdadb22bf099c8829d6d6e4dcc91fe7)

> Nested Comments By @aibunny [bbab06c](https://github.com/SpaceyaTech/blog/commit/bbab06c95da6ec1506469aa1d3652b7b52c17a6f)


## Authentication
[JWT Authentication by:](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/Authentication) [Hellen](@hellen-22)

## Phone Numbers
## Api Throttling
[Api Throttling by:](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/API-THROTTLING)[Collins](@Collins-Omariba)
## Nested Comments 
[Nested Comments by:](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/Nested-Comments) [Fredrick](@aibunny)

# Contributors 
[![Contributors](https://contrib.rocks/image?repo=SpaceyaTech/blog)](https://github.com/SpaceyaTech/blog/graphs/contributors)
