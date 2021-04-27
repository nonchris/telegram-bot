# telegram-bot
A functional, generic telegram bot template that includes a sqlite database and the general bot setup

## setup
`pip install -r requirements.txt`  
`export API_KEY="your-key"`  
`python3 main.py`  
_Remember using a virtual environment!_

## features
This bot does 'nothing' but is completely functional!  
_What is does:_  
* setup logging
* setup database (SQLite) for users
* register default start and help command
* register functional callback handler
* register message listener

### also included
* default inline keyboards
* util wrapper `send_message`
* `get_user_by_chat_id` for quick db access
* converter of 'normal' text to escaped markdown text
* simple examples for normal and inline commands for better understanding
* *TODO* Marks on all the main points to fill this project with functionality

*The only thing you need is to fill this structure with life!*

## about
This repository contains code that was written by me across various bot-projects, like:
* https://github.com/nonchris/covid-data-bot
* https://github.com/the-rising-tide/certificate-bot

I collected the most useful and generic functions to save me some time when starting the next bot-project.  

### dependencies 
This project is based on `python-telegram-bot` and `SQLAlchemy`
