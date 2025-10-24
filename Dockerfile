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

RUN  wget  https://github.com/jgraph/drawio-desktop/releases/download/v28.2.5/drawio-amd64-28.2.5.deb

RUN apt-get update && apt-get install -y -f \
    ./drawio-amd64-28.2.5.deb \
    && rm -rf /var/lib/apt/lists/*


# Install RUST
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

#
# Set the working directory to /app
WORKDIR /app

# Installing pytorch (TODO: add it in requirements.txt)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


# Install Jupyter Notebook
COPY ./datasets ./datasets
COPY ./pyproject.toml ./pyproject.toml
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

# Install evcxr_jupyter
RUN . $HOME/.cargo/env && cargo install evcxr_jupyter
RUN . $HOME/.cargo/env && evcxr_jupyter --install

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
