> python3.6+

# {{ cookiecutter.repo_name }}
{{ cookiecutter.description }}

# Get Started 

```bash
python3 -m venv venv 
. venv/bin/activate
python3 setup.py install # or develop
```

# Create another project
Easy to try,

```bash
cd {{ cookiecutter.repo_name }} 
python3 manage.py start-project project_name
```


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