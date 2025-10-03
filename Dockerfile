# Use an official Python runtime as a parent image
FROM python:3.11


# Have to install swig for gymnasium box2D environment
RUN apt-get update && apt-get install -y \
    swig \
    nano \
    curl \
    libasound2 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN curl -s https://api.github.com/repos/jgraph/drawio-desktop/releases/latest | grep browser_download_url | grep 'drawio-amd64.*\.deb' | cut -d '"' -f 4 | wget -i -

RUN apt-get update && apt-get install -y -f \
    ./drawio-amd64-*.deb \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Installing pytorch (TODO: add it in requirements.txt)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


# Install Jupyter Notebook
COPY ./datasets ./datasets
COPY ./pyproject.toml ./pyproject.toml
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt


# Clone the pypibt repository
RUN git clone https://github.com/Kei18/pypibt.git

# Build and install pypibt
WORKDIR /app/pypibt
RUN pip install -e .

WORKDIR /app

# Set default working directory

EXPOSE 8888
EXPOSE 8080

COPY ./playground ./playground
COPY ./knowledge_compendium ./knowledge_compendium
COPY ./entrypoint.sh ./entrypoint.sh


CMD ["./entrypoint.sh" ]
