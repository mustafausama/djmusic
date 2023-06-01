# Django application for managing artists and their related albums

## Index 
- [Demo application](#demo-application)
- [Results documentation](#results-documentation)
- [App installation](#app-installation)
  - [Prerequites](#prerequites)
  - [Clone](#clone)
  - [Virtual Environment](#virtual-environment)
  - [Install](#install)
  - [Configurations](#configurations)
  - [Migrations](#migrations)
  - [Create a superuser](#create-a-superuser)
  - [Running tests](#running-tests)
  - [Running the server](#running-the-server)
- [App Usage](#app-usage)
  - [Creating Artists and Albums](#creating-artists-and-albums)
  - [Artist list view](#artist-list-view)
  - [Login and logout](#login-and-logout)
  - [REST API](#rest-api)
  - [Authentication](#authentication)
  - [User Details API](#user-details-api)

## Demo application

**Demo application has the second part only**

Final application is deplyed on heroku
[Admin Link](https://djmusic-django.herokuapp.com/admin)

> username: admin  
> password: pass1234

## Results documentation

The development steps and their results are documented in the file [RESULTS.md](djmusic/musicplatform/RESULTS.md)

## App installation

### Prerequites

You should have the following installed in order to run the application:

- Python
- Poetry
- PostgreSQL (local or remote)

### Clone

Run the following terminal command in order to clone the app and go into its directory.

```console
git clone https://gitlab.com/mustafa.abdelrahman/django-training.git && cd django-training
```

### Virtual Environment

While in the root directory (django-training), run the following command to use the poetry environment

```console
poetry shell
```

Or you can list all the available virtual environments with the command `poetry env list --full-path`, then copy the path of the virtual environment you want to use and run the following command with the path instead of **/full/path/to/python**

```console
poetry env use /full/path/to/python
```

### Install

Run the following terminal command in order to install the app

```console
poetry install
```

### Configurations

In djmusic directory, change the name of the **.env.example** file to **.env**  
Fill the .env file with the database credentails, and the secret key of the app.

> You can generate a secret key with either of the following commands
>
> ```console
> openssl rand -base64 32
> ```
>
> ```console
> head -c 32 /dev/urandom | base64
> ```
>
> To be safe, store the secret key in the .env file inside the quotations marks.

### Migrations

In the root (django-training) directory. Run the following code to prepare the database migrations

```console
poetry run python djmusic/manage.py makemigrations
```

Then run the following command to apply the migrations

```console
poetry run python djmusic/manage.py migrate
```

### Create a superuser

In order to create a super user, run the following command and enter the credentials interactively

```console
poetry run python djmusic/manage.py createsuperuser
```

### Running tests
In order to run the created endpoint tests, run the following command
```console
poetry run pytest
```
A message with the testing result, percentage, passing tests, and time will be printed.

### Running the server

Run the following comman to start serving the application

```console
poetry run python djmusic/manage.py runserver
```

> If port 8000 is busy, try running on another port of your choice as follows
>
> ```console
> poetry run python djmusic/manage.py runserver 8080
> ```
>
> You can replace 8080 with the port you wish.

Now visit [http://localhost:8000](http://localhost:8000) or [http://localhost:8080](http://localhost:8080) or replace 8000 with the port you have specified while running the server

You can visit the admin panel using this link [http://localhost:8000/admin](http://localhost:8000/admin)
Now you can login using the credentials you created in the [previous section](#create-a-superuser)

## App Usage

## Creating Artists and Albums
> These Views do not work anymore after the sixth part

Artists and albums can be created using the following links, repectively.

**Artist**: [http://localhost:8000/artists/create/](http://localhost:8000/artists/create/)
> Starting with the **fifth part**, the artist's view endpoints are followed by **/old/** because a serialized REST API view was linked to the original endpoint  
  **List View**: [http://localhost:8000/artists/old/create/](http://localhost:8000/artists/old/create/)

**Album**: [http://localhost:8000/albums/create/](http://localhost:8000/albums/create/)

## Artist list view
> These Views do not work anymore after the sixth part

A list view of the artists and their respective albums can be viewed using the following link.

**List View**: [http://localhost:8000/artists/](http://localhost:8000/artists/)
> Starting with the **fifth part**, the artist's view endpoints are followed by **/old/** because a serialized REST API view was linked to the original endpoint  
  **List View**: [http://localhost:8000/artists/old/](http://localhost:8000/artists/old/)


## Login and logout
> This View does not work anymore after the sixth part

Using the following links, you can:
- **Login**: [http://localhost:8000/accounts/login/](http://localhost:8000/accounts/login/)
- **Logout**: [http://localhost:8000/accounts/logout/](http://localhost:8000/accounts/logout/)

## REST API
Two rest-api endpoints were added to the application.
- Artist View (JSON): **GET** [http://localhost:8000/artists/](http://localhost:8000/artists/)  
  Data will be returned in the following format
  ```javascript
  [
      {
          "id": '<id>', // Numeric
          "stage_name": "<stage_name>", // String
          "social_link": "<social_link>" // String
      },
      ...
  ]
  ```
- Artist Creation (JSON body): **POST** [http://localhost:8000/artists/](http://localhost:8000/artists/)
  > Requires authentication as Basic Authentication (**username** and **password**) along with the request
  
  Requires a body with the following keys
  - **stage_name**: required, unique, max length of 200 characters
  - **social_link**: optional

  Data will be returned in the following format
  ```javascript
  {
      "id": '<id>', // Numeric
      "stage_name": "<stage_name>", // String
      "social_link": "<social_link>" // String
  }
  ```

## Authentication
- Register: **POST** [http://localhost:8000/authentication/register/](http://localhost:8000/authentication/register/)  
  It accepts a body with the following fields
  - **username**: required, unique
  - **email**: optional, unique
  - **password1**: require, strong password
  - **password2**: matches password1

  It returns a json with the following format
  ```javascript
  {
    "username": "<username>",
    "email": "<email>"
  }
  ```
- Login: **POST** [http://localhost:8000/authentication/login/](http://localhost:8000/authentication/login/)  
  It accepts a body with the following fields
  - **username**: required
  - **password**: required  

  It returns a json with the following format
  ```javascript
  {
    "token": "<knox token>",
    "user": {
      "id": '<id>', // Numeric
      "username": "<username>",
      "email": "<email>",
      "bio": "<bio>"
    }
  }
  ```
- Logout: **POST** [http://localhost:8000/authentication/logout/](http://localhost:8000/authentication/logout/)  
  It requires an authorization header with in the following format
  > Authorization: Token *token_here*

## User Details API
- Retrieve User: **GET** [http://localhost:8000/users/<int:pk>/](http://localhost:8000/users/<int:pk>/)  
  It returns a json with the following format
  ```javascript
  {
    "id": '<id>',
    "username": "<username>",
    "email": "<email>",
    "bio": "<bio>"
  }
  ```
- Update the whole user: **PUT** [http://localhost:8000/authentication/login/](http://localhost:8000/authentication/login/)  
  
  It accepts a body with the following **required** fields
  - **username**: required

  It accepts a body with the following **optional** fields
  - **email**
  - **bio**
  
  It requires an authorization header with in the following format
  > Authorization: Token *token_here*

  It returns a json with the following format
  ```javascript
  {
    "id": '<id>',
    "username": "<username>",
    "email": "<email>",
    "bio": "<bio>"
  }
  ```
- Update specific user fields: **PUT** [http://localhost:8000/authentication/login/](http://localhost:8000/authentication/login/)
  It accepts a body with any (or all) the following **optional** fields
  - **username**
  - **email**
  - **bio**

  It requires an authorization header with in the following format
  > Authorization: Token *token_here*

  It returns a json with the following format
  ```javascript
  {
    "id": '<id>',
    "username": "<username>",
    "email": "<email>",
    "bio": "<bio>"
  }
  ```

