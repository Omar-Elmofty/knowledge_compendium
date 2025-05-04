# My Machine Learning Notes


Building the container:
```
docker image build -t machine_learning_notes .
```

Running the container:
```
docker container run -p 8888:8888  -v $(pwd)/notebooks:/app/notebooks  machine_learning_notes
```

Copy the jupyter link with the token from the terminal and run on the browser.