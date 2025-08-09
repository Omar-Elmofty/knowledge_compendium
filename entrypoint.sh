#!/bin/bash


# Run jupyter notebook on port 8888
jupyter notebook --ip=127.0.0.1 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' & 

# Compile all the draw.io diagrams to SVG

# Check if knowledge_compendium/diagrams/exported directory exists, if not create it
if [ ! -d "knowledge_compendium/diagrams/exported" ]; then
    mkdir -p knowledge_compendium/diagrams/exported
fi

# Cleanup the exported directory
rm -rf knowledge_compendium/diagrams/exported/*

# Export all diagrams from knowledge_compendium/diagrams to SVG format
xvfb-run /opt/drawio/drawio --no-sandbox --export knowledge_compendium/diagrams/  --format png --output knowledge_compendium/diagrams/exported --disable-gpu


# Build the compendium
jupyter-book build knowledge_compendium

# Serve the compendium on port 8080
python3 -m http.server 8080 --directory knowledge_compendium/_build/html --bind 127.0.0.1



# If you want the container to die with no activity, uncomment the following line
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.shutdown_no_activity_timeout=60", "--MappingKernelManager.cull_idle_timeout=60", "--MappingKernelManager.cull_interval=60"]