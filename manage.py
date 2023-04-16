#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?") from exc

    # Codigo para debug usando o vs code
    if (os.environ.get("RUN_MAIN")
            or os.environ.get("WERKZEUG_RUN_MAIN")) and os.environ.get("VSCODE_DEBUGGER", True):
        try:

            print("Starting Debug ...")
            import debugpy
            debugpy.listen(('0.0.0.0', 5679))
            # debugpy.wait_for_client()
            # debugpy.breakpoint()

            print("Debug attached to port 5679")
        except Exception as e:
            print("Port 5679 already in use? Check .vscode/launch.json. Error:")
            print(e)
    else:
        print("Debugger already running?")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
