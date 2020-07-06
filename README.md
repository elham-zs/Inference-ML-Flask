# Serve machine learning model via flask

To run code  with docker, first must be run the command as follows and then can be use [postman](https://github.com/elham-zs/Inference-ML-Flask/blob/master/online-inference-innovaton.postman_collection.json) in the repo to send the post request
```console
foo@bar:~$ docker build -t inference .
foo@bar:~$ docker run -d -p 5000:5000 inference
```
