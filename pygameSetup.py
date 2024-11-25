"""
Name: proxlu
Date: Oct 30, 2024

Description: pygame installer.
"""
import os
import sys
import subprocess

install_dir = os.path.abspath('Libs')

if not os.path.exists(os.path.join(install_dir, 'pygame')):
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pygame', '--target', install_dir], check=True)

sys.path.append(install_dir)
