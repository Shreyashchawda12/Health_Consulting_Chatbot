---
title: Health Consulting Chatbot
emoji: 👀
colorFrom: green
colorTo: red
sdk: streamlit
sdk_version: 1.31.1
app_file: app.py
pinned: false
license: mit
---

## For Local Machine
### Create API KEY
``
Create .env file and add GOOGLE_API_KEY \n
visit https://makersuite.google.com/app/apikey website and create API Key and store in .env file
``

### created a environment using Annaconda
```Bash
conda create -p "gen_venv" python==3.10 -y
```
### activate environment
```Bash
conda activate gen_venv/
```
### Install all necessary libraries
```Bash
pip install -r requirements.txt
```
## To run the application
```bash
python -m streamlit run app.py
```

