## Django: Behaviour Driven Development - Demo

This is a demo project for API development in Django using BDD approach

####Project directory structure

```
.
├── bdd_django_project
│   ├── bdd_django_app
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── bdd_django_project
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── behave.ini
│   ├── db.sqlite3
│   ├── manage.py
│   ├── README.md
│   ├── templates
│   └── tests
│       ├── acceptance
│       │   ├── environment.py
│       │   ├── features
│       │   │   └── example.feature
│       │   └── steps
│       │       └── steps.py
│       ├── __pycache__
│       └── reports
│           └── TESTS-features.example.xml
├── LICENSE
├── README.md
└── requirements.txt

```
#### Scenario
```
Feature: Test REST API

  Background:
    Given I set sample API url

    Scenario: Base url validation
      When Send GET HTTP request to api url
      Then I received valid HTTP response code 200

    Scenario: GET users API validation
      Given I set GET api endpoint as "api/v1/users"
      When I send GET HTTP request
      Then I receive valid HTTP response code 200
        And Response BODY is not-empty

```

#### Testing
```python
python manage.py behave
```
```
Creating test database for alias 'default'...
Feature: Test REST API # tests/acceptance/features/example.feature:1

Background:   # tests/acceptance/features/example.feature:3

Scenario: Base url validation                  # tests/acceptance/features/example.feature:6
Given I set sample API url                   # tests/acceptance/steps/steps.py:12 0.000s
When Send GET HTTP request to api url        # tests/acceptance/steps/steps.py:19 0.004s
Then I received valid HTTP response code 200 # tests/acceptance/steps/steps.py:25 0.000s

Scenario: GET users API validation               # tests/acceptance/features/example.feature:10
Given I set sample API url                     # tests/acceptance/steps/steps.py:12 0.000s
Given I set GET api endpoint as "api/v1/users" # tests/acceptance/steps/steps.py:32 0.000s
When I send GET HTTP request                   # tests/acceptance/steps/steps.py:38 0.006s
Then I receive valid HTTP response code 200    # tests/acceptance/steps/steps.py:47 0.000s
And Response BODY is not-empty                 # tests/acceptance/steps/steps.py:53 0.000s

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
8 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.010s
Destroying test database for alias 'default'...
```
