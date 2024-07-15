import os

def create_cv_repo_structure(base_path, repo_name):
    main_folders = [
        'data/raw', 'data/processed', 'data/external', 'data/interim',
        'notebooks',
        'scripts',
        'models',
        'reports/figures',
        'src/data', 'src/features', 'src/models', 'src/visualization',
        'tests'
    ]

    projects = ['ImageClassification', 'ObjectDetection', 'OtherProjects']

    for project in projects:
        for folder in main_folders:
            os.makedirs(os.path.join(base_path, repo_name, project, folder), exist_ok=True)
        
        with open(os.path.join(base_path, repo_name, project, 'README.md'), 'w') as f:
            f.write(f"# {project.replace('_', ' ')} Project\n\n")
            f.write("## Project Overview\n\n")
            f.write("Provide a brief description of the project here.\n\n")
            f.write("## Directory Structure\n\n")
            f.write("```\n")
            f.write(f"{project}/\n")
            for folder in main_folders:
                f.write(f"{folder}/\n")
            f.write("README.md\n")
            f.write("```\n")
            f.write("\n## How to Use This Repository\n\n")
            f.write("Instructions on how to use the repository.\n\n")
            f.write("## Requirements\n\n")
            f.write("List the project requirements here.\n\n")
            f.write("## Installation\n\n")
            f.write("Steps to install the necessary dependencies.\n\n")
            f.write("## Usage\n\n")
            f.write("Examples on how to run the scripts and notebooks.\n\n")
            f.write("## Contributing\n\n")
            f.write("Guidelines for contributing to the project.\n\n")
            f.write("## License\n\n")
            f.write("License information.\n")

    with open(os.path.join(base_path, repo_name, 'README.md'), 'w') as f:
        f.write(f"# {repo_name.replace('_', ' ')} Repository\n\n")
        f.write("## Overview\n\n")
        f.write("This repository contains various computer vision projects including Image Classification, Object Detection, and more.\n\n")
        f.write("## Projects\n\n")
        f.write("1. [Image Classification](./ImageClassification/README.md)\n")
        f.write("2. [Object Detection](./ObjectDetection/README.md)\n")
        f.write("3. [Other Projects](./OtherProjects/README.md)\n")
        f.write("\n## Directory Structure\n\n")
        f.write("```\n")
        f.write(f"{repo_name}/\n")
        for project in projects:
            f.write(f"{project}/\n")
            for folder in main_folders:
                f.write(f"  {folder}/\n")
            f.write("  README.md\n")
        f.write("README.md\n")
        f.write("```\n")
        f.write("\n## Requirements\n\n")
        f.write("List the overall repository requirements here.\n\n")
        f.write("## Installation\n\n")
        f.write("Steps to install the necessary dependencies for the entire repository.\n\n")
        f.write("## Usage\n\n")
        f.write("Examples on how to run the scripts and notebooks for different projects.\n\n")
        f.write("## Contributing\n\n")
        f.write("Guidelines for contributing to the repository.\n\n")
        f.write("## License\n\n")
        f.write("License information.\n")

base_path = 'D:\JHANSI SIRIPROLU\DEEP LEARNING\ComputerVision'
repo_name = 'ComputerVision'
create_cv_repo_structure(base_path, repo_name)

print("Repository structure created successfully!")
