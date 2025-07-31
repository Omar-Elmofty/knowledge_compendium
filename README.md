# My Machine Learning Notes


Building the container (the `--network=host` is for working with vpn):
```
docker image build --network=host -t machine_learning_notes .
```

Running the container:
```
docker container run --rm --network=host -p 8888:8888  -v $(pwd):/app:rw  machine_learning_notes
```

Copy the jupyter link with the token from the terminal and run on the browser.


Try spinning a new container by via this link [https://sharpe-investor.com:8080/start](https://sharpe-investor.com:8080/start)