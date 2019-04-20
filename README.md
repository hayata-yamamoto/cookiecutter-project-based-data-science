# Cookiecutter-Data-Science-for-Team (CDST)

This template is designed for team data science project. 


# Structure

```
cookiecutter-data-science-for-team/
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