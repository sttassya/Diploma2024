#!/bin/bash

projects_dir="C:/Users/Ана/Desktop/ДИПЛОМ/ITIS_PROJECTS"

for project_dir in "$projects_dir"/*; do
    if [ -d "$project_dir" ]; then
        pushd "$project_dir" > /dev/null
        C:/sonar-scanner-5.0.1.3006-windows/bin/sonar-scanner.bat
        popd > /dev/null
    fi
done