#!/usr/bin/env bash
gunicorn --workers 10 --bind 0.0.0.0:5000 wsgi
