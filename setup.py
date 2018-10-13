# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:06:18 2018

@author: el_in
"""

import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'
executables = [cx_Freeze.Executable(r'C:\Users\el_in\Documents\carlos\tkinter\tkinter1.py',base=base)]

#r'C:\Users\el_in\OneDrive\Documentos\carlos\sismologico programas\dummier4\tk_Dummier.py'

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


cx_Freeze.setup(
    name = "Hyper",
    options = {"build_exe":{"packages":["tkinter","email","smtplib",'os'],
                            "include_files":[r"C:\Users\el_in\Documents\carlos\tkinter\funciones_sismicas.py",
                                             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                             os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                                             ]}},
    version = "0.01",
    description = "Programa que localiza la ciudad donde ocurre el evento y lo envia",
    executables = executables 
    )
