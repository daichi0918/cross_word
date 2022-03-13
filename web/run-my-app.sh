#!/bin/sh

while :
do
  if python manage.py migrate; then
    break
  else
    sleep 1
  fi
done

python manage.py runserver 0.0.0.0:8004

exit 0