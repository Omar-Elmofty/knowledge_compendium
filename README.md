# Knowledge Compendium

This repo that contains notes about various subjects like robotics / controls / motion planning ... etc.

It's split into 2 main sections:
1. `knowledge_compendium`: A jupyter book containing all my notes about various topics. Latest version is running on [https://omarelmofty.com/knowledge_compendium/](https://omarelmofty.com/knowledge_compendium/). If you want to locally run, run the docker container (see instructions below), it will be servable on [http://127.0.0.1:8080](http://127.0.0.1:8080)
2. `playground`: Contains random jupyter notebooks with various examples or experiments. They are less structured than the `knowledge_compendium`. After running the docker container (see instructions below) it is servable on [http://127.0.0.1:8888/tree](http://127.0.0.1:8888/tree).


Instructions for building the docker image and running the container:

First you need to install [docker](https://www.docker.com/get-started/)


Then build the docker image by running the following command (the `--network=host` is for working with vpn):
```
docker image build --network=host -t knowledge_compendium .
```

Then running the docker container:
```
# For launching the jupyter book (served on http://127.0.0.1:8888)
docker container run --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --jupyter

# For building the jupyter book 
docker container run --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --build-compendium

# For building and serving the jupyter book on http://127.0.0.1:8080
docker container run --rm --network=host -v $(pwd):/app:rw --name kc_container knowledge_compendium --serve-compendium
```
