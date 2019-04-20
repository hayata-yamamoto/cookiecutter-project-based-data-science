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
│   └── docs
├── extensions
└── {{ cookiecutter.repo_name }}
    ├── docs
    └── {{ cookiecutter.repo_name }}
        ├── core
        │   ├── config
        │   ├── datasets
        │   ├── features
        │   └── models
        ├── data
        │   └── {{ cookiecutter.project_name }}
        │       ├── interim
        │       ├── processed
        │       └── raw
        ├── modules
        ├── tests
        │   ├── core
        │   └── {{ cookiecutter.project_name }}
        └── {{ cookiecutter.project_name }}
            ├── notebooks
            │   ├── exploratory
            │   └── predictive
            └── src
                ├── datasets
                ├── features
                ├── models
                └── tasks
```