# streamlit-template
Template for building streamlit apps efficiently

## About

- This is a template for layout and efficient directory structure for a streamlit demo.
- If you want to use, clone the repo, and copy-paste all files in your working directory.

## Files and directory
**app.py** - main script for the streamlit frontend  
**.streamlit/** - config folder for streamlit app configurations (colors, font, themes, etc)  
**frontend/** - directory with all the 'frontend' scripts and rendering functions and constants. The idea is to keep the app.py as simple as possible.    
**backend/** - directory with all the backend scripts and computations.  
**.env & .env.template** - environment variable (AUTH0 secret variables for example). Never push to Git (add .env to .gitignore).      
**requirements.txt** - If you use pip, fill this file with the needed packages.  


## Installation (Using python virtual env and pip)
- *(Only do once for the installation)* Clone this repository
-  Download python 3.9 from [python.org](https://www.python.org/downloads/)
- *(Do every time)* Open the terminal
- *(Only do once for the installation)* Make sure that pip is up-to-date by running:
```console
python3 -m pip install --upgrade pip

python3 -m pip --version
```
- *(Do every time)* Navigate to the project's directory *(example)*:
```console
cd /Users/user_name/Documents/streamlit-template
```
- *(Only do once for the installation)* Create a virtual environment:
```console
python3 -m venv venv
```
- *(Do every time)* Activate the virtual environment:
```console
source venv/bin/activate
```
- *(Only do once for the installation)* Install all the dependencies contained in the requirements.txt file:
```console
python3 -m pip install -r requirements.txt
```
- *(Do every time)* Run the app:
```console
streamlit run app.py
```

- *(Do every time)* Close the app when finished:
```console
CTRL-c
```