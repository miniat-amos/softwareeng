REM Ensuring python dependencies are met
python3 -m pip install -r requirements.txt

REM Creating the executable
python3 -m PyInstaller --windowed --onefile .\src\main.py 

REM Creating the installation file
ISCC.exe installer.iss