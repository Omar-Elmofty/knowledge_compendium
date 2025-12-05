# Knowledge Compendium

This repository contains notes about various subjects like robotics, controls, motion planning, etc.

It is split into two main sections:
1. `knowledge_compendium`: A Jupyter book containing all my notes about various topics. The latest version is available at [https://omarelmofty.com/knowledge_compendium/](https://omarelmofty.com/knowledge_compendium/). If you want to run it locally, start the Docker container (see instructions below). It will be accessible at [http://127.0.0.1:8080](http://127.0.0.1:8080).
2. `playground`: Contains random Jupyter notebooks with various examples or experiments. They are less structured than the `knowledge_compendium`. After starting the Docker container (see instructions below), it will be accessible at [http://127.0.0.1:8888/tree](http://127.0.0.1:8888/tree).

Instructions for building the Docker image and running the container:

First, you need to install [Docker](https://www.docker.com/get-started/).

Then build the Docker image by running the following command (the `--network=host` is for working with VPN):
```
docker image build --network=host -t knowledge_compendium .
```

Then run the Docker container:
```
# For launching the Jupyter book (served on http://127.0.0.1:8888)
docker run -it --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --jupyter

# For building the Jupyter book
docker run -it --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --build-compendium

# For building and serving the Jupyter book on http://127.0.0.1:8080
docker run -it --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --serve-compendium
```
