# Project Based Data Science (Cookiecutter)

# Get Started 

```bash
pip3 install cookiecutter 
cookiecutter https://github.com/hayata-yamamoto/cookiecutter-project-based-data-science
```


# Structure

```
cookiecutter-project-based-data-science/
├── docs
└── {{ cookiecutter.repo_name }}
    ├── docs
    └── {{ cookiecutter.repo_name }}
        ├── core
        │   ├── config
        │   └── src
        │       ├── datasets
        │       ├── features
        │       ├── models
        │       └── tasks
        ├── data
        │   └── {{ cookiecutter.project_name }}
        │       ├── interim
        │       ├── processed
        │       └── raw
        ├── modules
        └── {{ cookiecutter.project_name }}
            ├── notebooks
            └── src
                ├── datasets
                ├── features
                ├── models
                ├── tasks
                └── tests
```