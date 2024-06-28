<div align="center">

## Task Manager

[//]: # (<img src="" alt="logo" width="250" height="auto" />)
<h1>Task Manager</h1>

<p>
A flexible task management web application
</p>

### Hexlet tests and linter status:

[![Actions Status](https://github.com/Myakot/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Myakot/python-project-52/actions)
[![Run Tests](https://github.com/Myakot/python-project-52/actions/workflows/run_tests.yml/badge.svg)](https://github.com/Myakot/python-project-52/actions/workflows/run_tests.yml)
[![Lint Check](https://github.com/Myakot/python-project-52/actions/workflows/lint_check.yml/badge.svg)](https://github.com/Myakot/python-project-52/actions/workflows/lint_check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/71bb63846b242e0c53cb/maintainability)](https://codeclimate.com/github/Myakot/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/71bb63846b242e0c53cb/test_coverage)](https://codeclimate.com/github/Myakot/python-project-52/test_coverage)

</div>

### Demonstration

The production version of the app is (hopefully) available at the following URL:
[Page analyzer](https://python-project-52-adop.onrender.com)


## Installation and use

### Installation
```
https://github.com/Myakot/python-project-52/
cd python-project-52
make install
```

### Environment variables

For this app to work locally you have to manually create an `.env` file.
Then you will have to set the following environment variables: 
SECRET_KEY = 'anything'
DATABASE_URL = 'postgres://postgres:postgres@localhost:5432/postgres'

### Running the app

```
make start
```

### Database

I used free version of the render.com database. It's simple to register and use.

### Use migrations

```
make migrate
```

### Logging

Rollbar is used to log errors.

If you wish to use it, you can configure it in your `.env` file by adding the following line:

```
ROLLBAR_ACCESS_TOKEN=your_access_token
```