#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color


echo -n "- Cleaning up and recreating any databases:      "
filename='db.sqlite3'
if [ -f $filename ]; then
   rm db.sqlite3
   echo -e "[${GREEN}Done${NC}]"
fi

echo -n "- Cleaning up any migrations that already exist: "
find . -type f -name '[0-9][0-9][0-9][0-9]*.py' -delete > /dev/null 2>&1
sudo py3clean .
echo -e "[${GREEN}Done${NC}]"

echo -n "- Installing requirements:                       "
sudo pip3 install -r requirements.txt --upgrade > /dev/null 2>&1
echo -e "[${GREEN}Done${NC}]"

echo -n "- Creating the database:                         "
./manage.py makemigrations > /dev/null
./manage.py migrate > /dev/null
echo -e "[${GREEN}Done${NC}]"

echo "- Loading component data:                        "
#components=(`ls -d component/*/ | cut -f2 -d'/' | grep -v __pycache__`)
components=("personal" `ls -d component/*/ | cut -f2 -d'/' | grep -v __pycache__`)
for component in "${components[@]}"
do
    printf "%-49s" "  + Generating ${component}: "
    if ./manage.py loaddata component/$component/fixtures/*.json > /dev/null; then
        echo -e "[${GREEN}Done${NC}]"
    else
        echo -e "[${RED}Failed${NC}]"
    fi
done
echo
