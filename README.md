# My Machine Learning Notes


Building the container (the `--network=host` is for working with vpn):
```
docker image build --network=host -t jupyter_notebooks .
```

Running the container:
```
docker container run --rm --network=host -p 8888:8888  -v $(pwd):/app:rw  jupyter_notebooks
```

Open [http://127.0.0.1:8888/tree](http://127.0.0.1:8888/tree) on your browser to interact with the notebook.

