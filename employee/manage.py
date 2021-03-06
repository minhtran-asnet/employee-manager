#!/usr/bin/env python
import os
import sys

from constants import environment

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings." + environment.ENV)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
