# Python Quiz Game
A simple quiz game built with python

## Table Of Contents
- [Python Quiz Game](#python-quiz-game)
  - [Table Of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
    - [File Description](#file-description)
  - [Requirments](#requirments)
  - [Installation](#installation)
  - [Envoriment Setup](#envoriment-setup)
  - [Usage](#usage)
  - [Example Output](#example-output)
  - [Road Map](#road-map)
  - [Contributing](#contributing)
  - [Licence](#licence)
  - [Author](#author)

## Features
- Quiz system
  - Ask the player multiple questions 
  - Check the answers automatically
  - Calculates the final score
- Result Storage
  - saves quiz results in `result.txt`
- Admin mode
  - asks for the admin password
  - checks if the password is correct
  - keeps the password outside the main python file
- Loads the password from `.env`


## Project Structure

```text
python_quiz_game/
│   main.py
│   question.py
│   requirments.txt
│   .env.example
│   .gitignore
│   README.md
```

### File Description
- `main.py ` - main file used to run quiz game
- `question.py` - stores questions and answers
- `requirments.txt` - lists the python packages needed for the project
- `.env.example` - shows the envoriment variables needed by the project
- `gitignore` - tells git wich files and folders should not be tracked
- `README.md` - contains the project documantion

## Requirments
Before running the project make sure you have :
- python 3
- `python-dotenv`

## Installation
1. open a terminal in the project folder
2. check that python is installed
```bash
python --version
```
3. install the python packages :
```bash 
pip install -r requirments.txt
```

## Envoriment Setup
1. create a `.env` file from `.env.example`
```bash
cp .env.example .env
```
2. open the new `.env` file
3. replace the example value with your own password 
```text
QUIZ_ADMN_PASSWORD = your_password_here
```
4. save the file

> Do not commit your `.env` file because it may contain private 
## Usage
1. open a terminal in the project folder
2. run the quiz game 
```bash
python main.py
```
3. choose `yes` or `no` for admin mode 
4. if you choose `yes`, enter the password from your `.env` file 
5. enter your name
6. answer the questions 
7. see your final score and meesage
8. your results is saved in `result.txt`

## Example Output
```text
do you want to open admin mode? yes/no: no
whats your name: Alex
welcome
what language are we using: c++
wrong
what command starts a git: git init
correct
what command shows git status: git --oneline
wrong
your score is:  1 out of  3
keep praticing Alex   
```
## Road Map
- [x] add multiple quiz questions
- [x] calculate the final score
- [x] save results to a file
- [x] add admin mode
- [ ] add more quiz questions
- [ ] add difficultly levels
- [ ] add a timer
## Contributing

## Licence

## Author

create by [Hamidreza]((https://github.com/hamidrezaesfandiary))  