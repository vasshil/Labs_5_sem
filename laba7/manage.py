#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laba7.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# python3 manage.py runserver
# http://127.0.0.1:8000/goods/?token=113823e1-fa66-4ec2-82ea-974174d5362c
# http://127.0.0.1:8000/new_good/?token=113823e1-fa66-4ec2-82ea-974174d5362c&name=lemon&amount=11&price=6