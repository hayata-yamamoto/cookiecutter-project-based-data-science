# {{ cookiecutter.repo_name }}
{{ cookiecutter.description }}

# Structure 

```text
{{ cookiecutter.repo_name }}
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
    │   └── {{ cookiecutter.first_project_name }}
    │       ├── interim
    │       ├── processed
    │       └── raw
    ├── management
    ├── modules
    └── {{ cookiecutter.first_project_name }}
        ├── notebooks
        └── src
            ├── datasets
            ├── features
            ├── models
            ├── tasks
            └── tests
```