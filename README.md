# Flask ML Model CD Pipeline Tutorial
The data set in this exercise is from the blog on Flask Tutorial at [Build the first Flask Python web app framework](https://medium.com/analytics-vidhya/https-medium-com-chirag6891-build-the-first-flask-python-e278b52473f3). This codebase is based on the GCP Pipeline tutorial at [ML Deployment on Cloud](https://github.com/jgvaraujo/ml-deployment-on-gcloud)

## ML Model Flask-Deployment
This project demonstrates how a Flask ML app can be deployed on Google Cloud Platform using Docker container and YAML files that are useful to build continuous deployment (CD) pipelines. 

### Prerequisites (requirements.txt)
 - Scikit Learn
 - Pandas 
 - Numpy
 - Flask 

### Project Structure
All the application files are contained in the folder 'app_files'. The goal is to build an ML model using Decision Tree Classifier
1. model.py - This contains code fot our Machine Learning model (Decision Tree model) to predict employee salaries absed on trainign data in '50_Startup.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
The flask app will run on http://0.0.0.0:8080/ (localhost)


### Deploying on Google Cloud
3. Create a Google Cloud Run trigger at: https://console.cloud.google.com/cloud-build/triggers

4. Check the deployed app at: https://console.cloud.google.com/run

You now have a deployed app

### Clean up

5. Delete the triggers on the page https://console.cloud.google.com/cloud-build/triggers
6. Delete the app at:  https://console.cloud.google.com/run



