#!/bin/bash

usage() {
    echo "Usage: $0 [--jupyter --build-compendium --serve-compendium --export-diagrams]"
    exit 1
}

# Check if at least one argument was provided
if [ -z "$1" ]; then
  usage
fi

if [ "$1" != "--jupyter" ] && [ "$1" != "--build-compendium" ] && [ "$1" != "--serve-compendium" ] && [ "$1" != "--export-diagrams" ]; then
    usage
fi

if [ "$1" == "--jupyter" ]; then
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
    exit 0
fi

python3 -m nodeenv -v --node=22.17.0 --prebuilt --clean-src


# Compile all the draw.io diagrams to SVG
# Check if knowledge_compendium/diagrams/exported directory exists, if not create it
if [ ! -d "knowledge_compendium/diagrams/exported" ]; then
    mkdir -p knowledge_compendium/diagrams/exported
fi

# Cleanup the exported directory
rm -rf knowledge_compendium/diagrams/exported/*

# Export all diagrams from knowledge_compendium/diagrams to SVG format
xvfb-run /opt/drawio/drawio --no-sandbox --export knowledge_compendium/diagrams/  --format png --output knowledge_compendium/diagrams/exported --disable-gpu --scale 2

if [ "$1" == "--export-diagrams" ]; then
    exit 0
fi

# clean build
rm -rf  knowledge_compendium/_build/
rm -rf  knowledge_compendium/.ipynb_checkpoints/

# Build the compendium
jupyter-book build knowledge_compendium

if [ "$1" == "--serve-compendium" ]; then
    # Serve the compendium on port 8080
    python3 -m http.server 8888 --directory knowledge_compendium/_build/html --bind 0.0.0.0
fi
