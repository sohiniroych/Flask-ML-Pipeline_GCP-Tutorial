# For this In-Class assignment you will deploy an ML-based Flask app first on local host and then host it on GCP using a continuous pipeline.

## Flask ML Model CD Pipeline Tutorial
The data set in this exercise is from the blog on Flask Tutorial at [Build the first Flask Python web app framework](https://medium.com/analytics-vidhya/https-medium-com-chirag6891-build-the-first-flask-python-e278b52473f3). This codebase is based on the GCP Pipeline tutorial at [ML Deployment on Cloud](https://github.com/jgvaraujo/ml-deployment-on-gcloud)

## ML Model Flask-Deployment
This project demonstrates how a Flask ML app can be deployed on Google Cloud Platform using Docker container and YAML files that are useful to build continuous deployment (CD) pipelines. 

### Prerequisites (requirements.txt)
 - Scikit Learn
 - Pandas 
 - Numpy
 - Flask 

### Steps for the Assignment
All the application files are contained in the folder 'app_files'. The goal is to build an ML model using Decision Tree Classifier. Start by cloning the repo to your local drive.
**Step 1: Inside folder 'app_files' open the code 'model.py'. Add some lines there to train a regression model (ANY regression model). Run 'model.py' so the 'treemodel.pkl' gets created.

**Step 2: Run: python app.py. Check out the localhost app. It should work properly. Take a snapshot of the URL and your app.

*Step 3: Now, fork the Github: https://github.com/sohiniroych/Flask-ML-Pipeline_GCP-Tutorial/tree/main to your Github account. This is important for the CD pipeline that we will build.
*Step 4: Go to the page https://console.cloud.google.com/cloud-build/triggers?project=my-ml-project-303018 and create a PUSH trigger using Dockerfile for your forked github project page (Folow instructions shown in class). RUN the trigger and check logs.
*Step 5: Repeat Step 4 but use YAML as your source. RUN the trigger and check the app. Check the cloud Build on https://console.cloud.google.com/cloud-build/triggers?project=my-ml-project-303018
*Step 6: Take a picture of your app with the sample URL. SUBMIT THIS PICTURE FOR YOUR ASSIGNMENT.
Now you have uploaded your OWN ML app on GCP with a CD Pipeline! Congratulations..
*Step 7: Clean up. Please delete ypur Triggers and your ML app before you go.

### Things to notice
The local flask app will run on http://0.0.0.0:8080/ (localhost). This is because the GCP app is detected on this port only. This step is native to GCP deployment only.




