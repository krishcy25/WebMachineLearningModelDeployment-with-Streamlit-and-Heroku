# WebModelDeployment-with-Streamlit-and-Heroku

This repository focuses on deploying Machine Learning model on Web that takes the user inputs for the variables and predicts the output

ML Model is deployed on Web using Heroku. You can access the web based model deployed using the link below
https://pycarethp-streamlit-yvk.herokuapp.com/

The screenshot of one of the prediction is provided below:

![webdep](https://user-images.githubusercontent.com/65406908/88798579-1a3ef800-d173-11ea-85d5-8ed43a181de8.PNG)


Step 1: Data files used for training and testing are placed in the directory (train_hp.csv, test_hp.csv)

Step 2: Code to train the model and save/load the model for deployment is included in the notebook "ML_Deployment-House Prices.ipynb" and saved/loaded model is stored in the form of pickle file as "hp_pyc_deployment_07122020.pkl"

Step 3: Images used for web deployment is included in the form of JPEG or PNG files

Step 4: Inclusion of other files.

## requirements.txt
requirements.txt file is a text file containing the names of the python packages required to execute the application. If these packages are not installed in the environment where the application is running, it will fail.

## setup.sh
setup.sh is a script programmed for bash. It contains instructions written in the Bash language and like requirements.txt, it is used for creating the necessary environment for our streamlit app to run on the cloud.


## Procfile
Procfile is simply one line of code that provides startup instructions to the web server that indicate which file should be executed when an application is triggered. In this example, ‘Procfile’ is used for executing setup.sh which will create the necessary environment for the streamlit app and the second part “streamlit run app.py” is to execute the application (this is similar to how you would execute a streamlit application on your local computer).

## app.py
This file contains the HTML web page developed as part of web based deployment that takes in user input and predicts the output in two ways: Online Predictions and Batch Predictions



# Execution of the Web based deployment in 2 ways

## Method 1: Using Local Host

All the files were placed in the local directory in a folder and followed the below procedures to check the deployed model in our local host

![l1](https://user-images.githubusercontent.com/65406908/88801984-70fb0080-d178-11ea-87b4-784aca71cad5.PNG)

![l2](https://user-images.githubusercontent.com/65406908/88802010-79533b80-d178-11ea-9bc4-9ac4b79a283c.PNG)



## Method 2: Deploying on Web using Heroku

Create a free account with Heroku. Upon successful creation of Heroku account, Create an new app with in Heorku, Place the entire local directory in GitHub repository with all the files and connect to GitHub repository and deploy it.

I have deployed the Wed Based ML model on Web using Heorku and it can be accessed using the below link

https://pycarethp-streamlit-yvk.herokuapp.com/

(Please note that the link usually loads with slight delay of 30 sec-1 min)




