# Serve machine learning model via flask

## Run with docker
To run code  with docker, first must be run the command as follows and then can be use [postman](https://github.com/elham-zs/Inference-ML-Flask/blob/master/online-inference-innovaton.postman_collection.json) in the repo to send the post request
```console
foo@bar:~$ docker build -t inference .
foo@bar:~$ docker run -d -p 5000:5000 inference
```
if there is no postman in your local machine, you can use curl to send your POST request.
here is the curl command:
```
curl --location --request POST 'http://127.0.0.1:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '[
  	{ 
	  	"sepal length (cm)": 5.5,
	    "sepal width (cm)": 2.5,
	    "petal length (cm)": 4.0,
	    "petal width (cm)": 1.3 
  	
    },
    {
		"sepal length (cm)": 5.1,
	    "sepal width (cm)": 1.2,
	    "petal length (cm)": 2.0,
	    "petal width (cm)": 4.4
    }
]
'
```
to kill your docker that not run anymore on your system
```console
foo@bar:~$ docker ps
foo@bar:~$ docker kill CONTAINER
```

## Run locally
In order to run the code locally, need first to install required library inside requirements.txt. Then, you need to create the model(classifier) and then run the flask server. 
```console
foo@bar:~$ pip install -r requirements.txt
foo@bar:~$ python3 train.py
foo@bar:~$ python3 inference.py
```
after running the inference.py, the flask serve runs and just to send the request by postman or by curl command as mentioned above.

## Run in Cloud Foundry
To run the code on cloud foundry, just need to run the following command:

```console
foo@bar:~$ cf login
foo@bar:~$ cf push
```
Just be sure that the name that you used is unique, just change the name of ml-flask to your desired name in [manifest.yml](https://github.com/elham-zs/Inference-ML-Flask/blob/master/manifest.yml) if you used the shared space.

and in order to use it, just in curl or postman must change the url to https://<YOUR-CF-URL>/predict
