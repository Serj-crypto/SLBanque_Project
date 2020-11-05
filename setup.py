# -*- coding: utf-8 -

import sys
from cx_Freeze import setup, Executable

#includes = ['CClient', 'CCompte', 'traitement', 'manageData']  # nommer les modules non trouves par cx_freeze
excludes = ["tkinter"]
  # nommer les packages utilises
#packages = ["os","sys", "PyQt5"]
includefiles = ["logo.png", "Version_details.txt", "Sauvegardes",'CClient.py', 'CCompte.py', 'traitement.py', 'manageData.py'] #fichiers non python

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # pour application graphique sous Windows
x=Executable(script="App.py", base=base, icon = "logo.ico")
    
    
    
setup(
    name="SLouisBanque-Gestion",
    version="1.02",
    description="first exe",
    author="Serginau LOUIS",
    options={"build_exe":{'include_files':includefiles, 'excludes':excludes}},
    executables=[x]
    )