"""Run or update the project. This file uses the `doit` Python package. It works
like a Makefile, but is Python-based
"""
import sys
from src import config
from pathlib import Path
from doit.tools import run_once
from doit import create_after
from doit import task
import os
import subprocess
import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
import warnings
warnings.filterwarnings("ignore")

def task_table02_main():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def create_original_table():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -c "import sys; sys.path.insert(0, \'src\'); import Table02Prep; Table02Prep.main()"')
        os.chdir(original_dir)  # Reset the directory back to the original after the action is done

    return {
        'actions': [create_original_table],  
        'verbosity': 1,
    }

def task_table02_testing_main():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def test_table02():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -m unittest Table02_testing.py')
        os.chdir(original_dir) # Reset the directory back to the original after the action is done

    return {
        'actions': [test_table02],
        'verbosity': 1,
    }

def task_table03_main():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def create_table03():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -c "import sys; sys.path.insert(0, \'src\'); import Table03; Table03.main()"')
        os.chdir(original_dir)  # Reset the directory back to the original after the action is done
    def create_updated_table03():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -c "import sys; sys.path.insert(0, \'src\'); import Table03; Table03.main(UPDATED=True)"')
        os.chdir(original_dir)  # Reset the directory back to the original after the action is done
    return {
        'actions': [create_table03, create_updated_table03],
        'verbosity': 1,
    }


def task_table03_testing_main():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def test_table03():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -m unittest Table03_testing.py')
        os.chdir(original_dir) # Reset the directory back to the original after the action is done

    return {
        'actions': [test_table03],
        'verbosity': 1,
    }


def task_walkthrough_table():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def run_notebook():
        os.chdir(os.path.join(current_dir, "src"))

        # read notebook
        with open("Walkthrough_table_2_and_table_3.ipynb", "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
        client = NotebookClient(nb, timeout=600, kernel_name="python3")
        client.execute()  

        # HTMLExporter to convert from ipynb to html
        html_exporter = HTMLExporter()
        body, _ = html_exporter.from_notebook_node(nb)

        with open("Walkthrough_table_2_and_table_3_executed.html", "w", encoding="utf-8") as f:
            f.write(body)
        os.chdir(original_dir) # Reset the directory back to the original after the action is done

    return {
        "actions": [run_notebook],
        "verbosity": 1,
    }


def task_create_latex_document():
    original_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define a wrapper function for your action that resets the directory afterwards
    def create_latex_doc():
        os.chdir(os.path.join(current_dir, "src"))
        os.system('python -c "import sys; sys.path.insert(0, \'src\'); import LaTeXDocGenerator"')
        os.chdir(original_dir)  # Reset the directory back to the original after the action is done

    return {
        'actions': [create_latex_doc],
        'verbosity': 1,
    }


def task_compile_latex_docs():
    """Compile LaTeX document to PDF."""
    base_path = os.getcwd()  # get the current working directory
    tex_directory = os.path.join(base_path, "output")  # directory of the .tex file
    tex_file = "combined_document.tex"  # the .tex file name
    target_pdf = os.path.join(base_path, "reports/report_final.pdf")  # path to the .pdf file

    # Define the commands as lists
    compile_command = ["latexmk", "-pdf", "-pdflatex=xelatex %O %S", tex_file]
    clean_command = ["latexmk", "-C"]

    def compile_tex():
        # Run the compile command in the tex_directory
        subprocess.run(compile_command, cwd=tex_directory, check=True)

    def clean_aux_files():
        # Run the clean command in the tex_directory
        subprocess.run(clean_command, cwd=tex_directory, check=True)

    return {
        "actions": [clean_aux_files, compile_tex],
        "targets": [target_pdf],
        "file_dep": [os.path.join(tex_directory, tex_file)],
        "clean": True,
    }
