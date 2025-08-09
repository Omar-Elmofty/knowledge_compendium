# Jupyter Notebooks

This repo contains a bunch of Jupyter Notebooks with mainly my notes about various subjects like Reinforcement Learning / Controls ... etc.

Check my corresponding blog [https://medium.com/@oelmofty](https://medium.com/@oelmofty) where I also write about the same topics an link these jupyter notebooks.

To run the jupyter notebooks, first you need to install [docker](https://www.docker.com/get-started/)


Then build the docker image by running the following command (the `--network=host` is for working with vpn):
```
docker image build --network=host -t jupyter_notebooks .
```

Then running the docker container:
```
docker container run --rm --network=host -p 8888:8888  -v $(pwd):/app:rw  jupyter_notebooks
```

After running the container, you should be able to reach the jupyter environment on [http://127.0.0.1:8888/tree](http://127.0.0.1:8888/tree).
