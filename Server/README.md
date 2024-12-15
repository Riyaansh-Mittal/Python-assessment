# Flask Application

This project is a simple web application built using Flask. It provides a basic framework for deploying web applications, handling routes, and rendering templates.

## Features

- Lightweight web framework built on Flask.
- Allows handling HTTP requests and rendering HTML templates.
- Simple and easy-to-extend structure for web applications.

## Prerequisites

- Python 3.x installed.
- Flask installed.
- Virtual environment setup (optional but recommended).

## Installation
-Install required python dependencies
  pip install -r requirements.txt

## Usage
python run.py

## Testing on Postman
-Add app
http://127.0.0.1:5000/add-app
{
  app_name: "Instagram",
  version: "1.0.0",
  description: "Social Media"
}

-Delete App
http://127.0.0.1:5000/delete-app/id

-Get App
http://127.0.0.1:5000/get-app/id



