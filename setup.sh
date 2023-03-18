#!/bin/sh

function deploy(){

	python manage.py migrate

	python manage.py setup_admin --username ${ADMIN_USERNAME} --email ${ADMIN_EMAIL} --password ${ADMIN_PASSWORD}

}

deploy
