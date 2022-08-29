python -m venv .env
.env\Scripts\python.exe -m pip install -e .
rmdir /s /q IP_Check.egg-info
.env\Scripts\python.exe -m pip install -r requirements.txt
pause