#!/bin/bash

# Check if project name is provided
if [ -z "$1" ]; then
    echo "Usage: ./create_project.sh <project_name>"
    exit 1
fi

PROJECT_NAME=$1

# Create main project directory
mkdir -p $PROJECT_NAME

# Create the directory structure
directories=(
    "1_Journey/timeline"
    "2_Real/implementation"
    "3_Environment/configs"
    "4_UI/screenshots"
    "5_Formula/docs"
    "6_Symbols/code"
    "7_Semblance/issues"
)

# Create directories
for dir in "${directories[@]}"; do
    mkdir -p "$PROJECT_NAME/$dir"
done

# Create basic README files with descriptions
files=(
    "1_Journey/README.md:# Journey\nObjectives and timeline tracking"
    "2_Real/README.md:# Real Implementation\nActual implementation and code"
    "3_Environment/README.md:# Environment\nSetup and configuration details"
    "4_UI/README.md:# UI\nUser interface and visual elements"
    "5_Formula/README.md:# Formula\nTechnical procedures and documentation"
    "6_Symbols/README.md:# Symbols\nCode implementation"
    "7_Semblance/README.md:# Semblance\nIssue tracking and solutions"
)

# Create files with initial content
for file in "${files[@]}"; do
    IFS=':' read -r filename content <<< "$file"
    echo -e "$content" > "$PROJECT_NAME/$filename"
done

echo "Project structure created successfully!"

# Display tree if available
if command -v tree &> /dev/null; then
    cd $PROJECT_NAME && tree
else
    echo "Install 'tree' command to view directory structure"
fi