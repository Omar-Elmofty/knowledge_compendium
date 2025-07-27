# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Have to install swig for gymnasium box2D environment
RUN apt-get update && apt-get install -y \
    swig \
    nano \
    && rm -rf /var/lib/apt/lists/*


# Installing pytorch (TODO: add it in requirements.txt)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


# Install Jupyter Notebook
COPY ./datasets ./datasets
COPY ./notebooks ./notebooks
COPY ./pyproject.toml ./pyproject.toml
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt


RUN pip install -e .

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.shutdown_no_activity_timeout=60", "--MappingKernelManager.cull_idle_timeout=60", "--MappingKernelManager.cull_interval=60"]
