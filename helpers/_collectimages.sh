#!/bin/bash

# Directory to hold the used figures
mkdir -p graphics

# Extract paths and copy figures
for path in $(find . -name "*.tex" | xargs grep -hoP '\\includegraphics.*?\{.*?\}' | grep -oP '\{.*?\}' | sed 's/[{}]//g'); do
    # Create the destination path inside the graphics directory
    dest_path="graphics/$path"
    
    # Create directories if they don't exist yet
    mkdir -p "$(dirname "$dest_path")"
    
    # Copy the figure to the new location in graphics directory
    cp "../results/paper/$path" "$dest_path"

    # Print the copied file
    echo "Copied: $path -> $dest_path"
done