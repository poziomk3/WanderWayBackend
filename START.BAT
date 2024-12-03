@ECHO OFF
"%cd%\.venv\Scripts\Python.exe" manage.py migrate
"%cd%\.venv\Scripts\Python.exe" manage.py runserver
@ECHO ON