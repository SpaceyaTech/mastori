# Team-Rio-Django

Backend for Team Rio Written in Django for the Space Ya Tech Project

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

[![Django CI](https://github.com/SpaceyaTech/Team-Rio-Django/actions/workflows/django.yml/badge.svg?event=push)](https://github.com/SpaceyaTech/Team-Rio-Django/actions/workflows/django.yml)
## Table of contents

- [Overview](#overview)
- [Product vision](#product-vision)
  - [Vision Abstract](#vision-abstract)
- [Contributing](#contribution-guide)
- [Commit message](#commit-message-template)

## Overview

The SpaceYaTech Content Management system is an open-application that lets users to quickly publish content and share it with ease to their audience. Inspired by existing CMSes like Hashnode, Wordpress, DEV and Joomla, we felt the need to create an African CMS created by young Africans looking to learn by contributing to Open Source. SpaceYaTech opted for a CMS as the debut open source project because of the technicalities involved in creating, maintaining and scaling a CMS. A CMS poses great technical challenges and a great learning opportunity for those looking to grow their tech skills.
For a more detailed overview of the project, read through the [CMS Backend wiki](https://github.com/SpaceyaTech/CMS-Backend-Repository/wiki)

## Product Vision

## Vision Abstract

As a user interested in technology space in Kenya, I should be able to use the application to find meaningful discussions on the tech ecosystem in Africa. The SpaceYaTech Forum should provide users with the opportunity to join communities, make posts, up-vote other people's posts, comment on posts, down-vote posts they don't like and report posts which don't abide by the community standards.

## Target Group

Young people interested in keeping in touch with what's happening in the tech space within Africa and other relevant topics which will boost their careers.

## Concrete Product Vision

**FOR**: young Africans interested in technology discussions in Africa
**WHO**: want to find opinions and news about various topics in Africa
**THE**: Space Ya Tech IS A web application
**THAT**: gives a platform to young people to interact on different technology matters
**UNLIKE**: other existing products which already exist in the market
**OUR PRODUCT**: is open source and developed by the community for the community addressing the pain points of the African tech ecosystem.

## Contribution guide

Get to read the [Contributions guide](https://github.com/SpaceyaTech/Team-Rio-Django/blob/main/contributions.md) here.

## Commit message template

Just so that we have all our commit messages to be more readable and sensible it is recomended we use a template for the commit messages. Here is a [commit message template](https://github.com/SpaceyaTech/Team-Rio-Django/wiki/Commit-Messages) that one should follow when making your Contributions

## To use PhoneNumberField

In order to use PhoneNumber_field for localization option, perform the following:

- Install phonenumber minimal metadata

```python
pip install "django-phonenumber-field[phonenumberslite]"
```

or

- Install phonenumber extended features (e.g. geocoding)

```python
pip install "django-phonenumber-field[phonenumbers]"
```

- Add `phonenumber_field` to the list of the installed apps in your `settings.py` file INSTALLED_APPS:

```python
INSTALLED_APPS = [
    # Other apps…
    "phonenumber_field",
]
```

- Model field section add the following:

```python
from phonenumber_field.modelfields import PhoneNumberField

phone_number = PhoneNumberField(blank=True)
```

## To Run and Create unittests

Add your tests in the test file in the test folder which is located in the app you want to test.  
To run all tests  
```python
python3 manage.py test
```
To run tests in a particular app
```
python3 manage.py test [appname]
```
## Changing the site titles
![image](https://user-images.githubusercontent.com/23496280/204856386-3105fb57-a020-47c7-a789-8943099f3e44.png)
