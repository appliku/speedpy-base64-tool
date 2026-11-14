#!/bin/bash

# Run the Django development server on all interfaces (0.0.0.0) 
# to make it accessible via tailnet or other networks

python manage.py runserver 0.0.0.0:8000