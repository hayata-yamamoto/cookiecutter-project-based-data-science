# Cookiecutter-Data-Science-for-Team (CDST)

This template is designed for team data science project. 


# Structure

```
{{\ cookiecutter.repo_name\ }}/
├── .gitignore
├── Makefile
├── __init__.py
├── docs
├── requirements.txt
├── setup.py
└── {{\ cookiecutter.repo_name\ }}
    ├── __init__.py
    ├── core
    │   ├── config
    │   │   └── config.json
    │   └── src
    │       ├── __init__.py
    │       ├── datasets
    │       │   └── __init__.py
    │       ├── features
    │       │   └── __init__.py
    │       ├── models
    │       │   └── __init__.py
    │       ├── path_manager.py
    │       └── tasks
    │           └── __init__.py
    ├── data
    │   ├── .gitkeep
    │   └── {{\ cookiecutter.first_project_name\ }}
    │       ├── interim
    │       │   └── .gitkeep
    │       ├── processed
    │       │   └── .gitkeep
    │       └── raw
    │           └── .gitkeep
    ├── manage.py
    ├── management
    │   ├── __init__.py
    │   └── commands.py
    ├── modules
    │   └── .gitkeep
    └── {{\ cookiecutter.first_project_name\ }}
        ├── notebooks
        │   └── .gitkeep
        └── src
            ├── __init__.py
            ├── datasets
            │   └── __init__.py
            ├── features
            │   └── __init__.py
            ├── models
            │   └── __init__.py
            ├── tasks
            │   └── __init__.py
            └── tests
                └── __init__.py
```