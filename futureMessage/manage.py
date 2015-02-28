#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "futureMessage.settings")

    from django.core.management import execute_from_command_line
	from django.core.mail import EmailMessage
    execute_from_command_line(sys.argv)
