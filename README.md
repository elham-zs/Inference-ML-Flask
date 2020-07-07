# Serve machine learning model via flask

## Run with docker
To run code  with docker, first must be run the command as follows and then can be use [postman](https://github.com/elham-zs/Inference-ML-Flask/blob/master/online-inference-innovaton.postman_collection.json) in the repo to send the post request
```console
foo@bar:~$ docker build -t inference .
foo@bar:~$ docker run -d -p 5000:5000 inference
```
if there is no postman, you can use curl to get the response.
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
```bash
docker ps
docker kill CONTAINER
```

## Run locally
In order to run the code locally, need first to install required library inside requirements.txt. Then, you need to create the model(classifier) and then run the flask server. 
```bash
pip install -r requirements.txt
python3 train.py
python3 inference.py
```
after running the inference.py, the flask serve runs and just to send the request by postman or by curl command as mentioned above.
