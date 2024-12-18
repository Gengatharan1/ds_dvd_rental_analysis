## Predicting Customer Behavior in DVD Rental Using Deep Learning with AWS deployment

Predict customer behavior in a DVD rental business, specifically focusing on customer churn, movie genre preferences, and rental demand forecasting. The objective is to use deep learning techniques to create models that can assist in decision-making, marketing strategies, and personalized customer recommendations.


## Table of Contents
- [Predicting Customer Behavior in DVD Rental Using Deep Learning with AWS deployment](#predicting-customer-behavior-in-dvd-rental-using-deep-learning-with-aws-deployment)
- [Table of Contents](#table-of-contents)
- [Setup](#setup)
  - [Softwares needed](#softwares-needed)
  - [Code](#code)
  - [Python packages](#python-packages)
  - [Environment\_variables](#environment_variables)
  - [Database Setup](#database-setup)
  - [Run App](#run-app)
- [Workflow](#workflow)
- [Contact](#contact)

## Setup
### Softwares needed
1. Jupyter Notebook     / Any Notebook IDE
2. Python 3.12          / venv with python=3.12
3. Git (with git bash)  / Download repo
4. AWS CLI
5. Docker

### Code

<!-- Clone this repository and ```cd``` into that directory
``` 
git clone https://github.com/Gengatharan1/ds_dvd_rental_analysis.git

cd ds_dvd_rental_analysis
``` -->

- Download project folder or full repo
- cd into the folder
```
cd ds_dvd_rental_analysis
```

### Python packages

Install all necessary packages
``` 
pip install -r requirements.txt
```

### Environment_variables
Creating ```.env``` file using template
``` 
cp .env_template .env
```

### Database Setup

Create database and table in PostgreSQL and add copy its credentials in ```.env``` file.

### Run App
``` 
streamlit run app.py
```

## Workflow
[Slides](https://docs.google.com/presentation/d/1YfRFRF8DH7qTqKNyuwGSCgqFzS-VdeMH3yqC8VlXMyk)

## Contact
[LinkedIn](https://www.linkedin.com/in/gengatharan007/)

---
^ [Back to table of contents](#table-of-contents)