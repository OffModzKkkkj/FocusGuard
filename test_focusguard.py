import os
import pytest

def test_main_script_exists():
    """Verifica se o script principal existe"""
    assert os.path.exists("main.py") or os.path.exists("focusguard.py"), "O script principal (main.py ou focusguard.py) não foi encontrado."

def test_requirements_file_exists():
    """Verifica se o arquivo requirements.txt existe"""
    assert os.path.exists("requirements.txt"), "O arquivo requirements.txt não foi encontrado."
