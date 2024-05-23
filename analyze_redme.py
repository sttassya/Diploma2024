import os

projects_folder = "C:/Users/Ана/Desktop/ДИПЛОМ/ITIS_PROJECTS"

projects_without_readme = 0

root_directories = [d for d in os.listdir(projects_folder) if os.path.isdir(os.path.join(projects_folder, d))]

for directory in root_directories:
    if 'README.md' not in os.listdir(os.path.join(projects_folder, directory)) and 'README.txt' not in os.listdir(os.path.join(projects_folder, directory)):
        projects_without_readme += 1

print(f"Количество проектов без README файлов: {projects_without_readme}")