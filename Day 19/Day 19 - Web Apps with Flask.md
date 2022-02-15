# Day 19 - Web Apps with Flask

# Python for Web

- python is a general purpose language and can be used for many places
- there are many python web frame works
- Django and Flask are the most popular ones

# Flask

- a web development framework written in Python
- uses Jinja2 template engine
- can also be used with other modern frontend libraries such as React
- use it with a virtual environmet will allow it to isolate project dependencies from the local machine dependencies

## Folder Structure

- once a flask project is created, the file structure should look like this:

```other
├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

- app.py file is the main file in the project
   - need to import flask and os module
   - to run the flask application, write python app.py in the main flask app directory
      - after you run it check local host 5000
- HTML files are stored in the templates folder

