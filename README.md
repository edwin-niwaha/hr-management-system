
https://github.com/edwin-niwaha/hr-management-system/assets/41472239/393b65cb-1391-400c-9137-062bcc3970cf
# hr-management-system

The Hr Management System keeps track of all of the employee’s information and data. I created the employee's leave application CRUD (create, read, update, and delete) operations. This is a role-based module in which the authorized user can login and perform any operation on the data.

## Features

• Register Employee - The the employee can self register and apply for the leave.

• View Employee Details - The employee can view his/her details

• Update Employee Details - The employee can edit his/her account details.

• Apply for Leave: The employee can submit leave Application.

• View Leave Application History - The employee can view leave application history.

• Update Leave Application - The employee can edit leave application details.

• Delete Leave Application - The employee can remove the leave application from the database.

> This Application was created using Python, Django, HTML/CSS, JavaScript and Bootstrap.

## Sample video of this Project

Hr Management System -
[![Watch the video](![HR SYSTEM](https://github.com/edwin-niwaha/hr-management-system/assets/41472239/be5052ae-dae8-4c12-9a12-d3e996b6b743)](https://youtu.be/0qaWrDrrk5k)

## Installation

This requires [Python](https://www.python.org/) v3.8+ and [Django](https://www.djangoproject.com/) v4.0.4+ to run.

**Clone the project**

```bash
$ git clone https://github.com/edwin-niwaha/hr-management-system.git
```

**Create Virtual Environment**

```bash
$ python -m venv .venv
$ source .venv/Scripts/activate
```

**Install Dependencies**

```bash
(.venv)$ pip install -r requirements.txt
```

**Add Environment Variables**
`SECRET_KEY = 'Enter your secret key'`

## Run Project

If you are running the project for the first time, run the following commands to create migrations and migrate them.

```bash
(.venv)$ python manage.py makemigrations
(.venv)$ python manage.py migrate
```

Then

```bash
(.venv)$ python manage.py runserver
```

Visit `http://127.0.0.1:8000/`


