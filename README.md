Installation method 1 (Run application locally)
Clone this Repo

git clone "git@github.com:CresitaTech/ml-admin-api.git"

Cd into the Fast-Api folder

cd Fast-Api-example

Create a virtual environment

python3 -m venv venv

Activate virtualenv

source venv/bin/activate

For zsh users

source venv/bin/activate.zsh

For bash users

source venv/bin/activate.bash

For fish users

source venv/bin/activate.fish

Cd into the src folder

cd src

Install the required packages

python -m pip install -r requirements.txt

Start the app

python main.py
7b. Start the app using Uvicorn

uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
