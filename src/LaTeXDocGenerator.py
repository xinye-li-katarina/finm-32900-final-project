from pathlib import Path
import subprocess
import os

"""
Combines multiple files from our project, like .txt, .tex, and .png into a single .tex document
which is then converted to a pdf, with images forced to appear in the exact order listed.
"""

# Define the base directory and output directory
base_dir = Path('../output')
output_file_path = base_dir / 'combined_document.tex'

# LaTeX document header: ADD \usepackage{float}
latex_document = [
    "\\documentclass{article}",
    "\\usepackage[utf8]{inputenc}",
    "\\usepackage{graphicx}",
    "\\usepackage{geometry}",
    "\\usepackage{xcolor}",
    "\\geometry{left=1in, right=1in, top=1in, bottom=1in}",  # Adjust margins as needed
    "\\usepackage{adjustbox}",
    "\\usepackage{booktabs}",
    "\\usepackage{float}",          # <--- Added so we can use [H]
    "\\begin{document}",
    "\\large"
]

# List of files in the order to be included
files = [
    "title.tex",
    "table02_writeup.txt",
    "table02_sstable.tex",
    "table02.tex",
    "table02_figure.png",
    "table03_writeup01.tex",
    "table03.tex",
    "table03_summary.txt",
    "table03_panelA_sstable.tex",
    "table03_panelB_sstable.tex",
    "update.txt",
    "updated_table03.tex",
    "updated_table03_summary.txt",
    "updated_table03_panelA_sstable.tex",
    "updated_table03_panelB_sstable.tex",
    "table03_writeup02.txt",
    "Intermediary_capital_ratio_and_risk_factor_figure.png",
    "updated_Intermediary_capital_ratio_and_risk_factor_figure.png",
    "table03_writeup03.txt",
    "table03_figure.png",
    "updated_table03_figure.png",
    "conclusion.txt"
]

def escape_latex_special_chars(text):
    # List of LaTeX special characters that need to be escaped
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
        '\\': r'\textbackslash{}',
    }
    # Escape each special character in the text
    for char, escaped_char in special_chars.items():
        text = text.replace(char, escaped_char)
    return text

# Function to read content from a file
def read_content(filename):
    with open(base_dir / filename, 'r', encoding='utf-8') as file:
        return file.read()

# Include the content from each file
for filename in files:
    if filename.endswith('.tex'):
        content = read_content(filename)

        if filename in ("updated_table03_panelA_sstable.tex", "updated_table03_panelB_sstable.tex", "table03_panelA_sstable.tex", "table03_panelB_sstable.tex",):
            
            content = content.replace(
                "\\begin{tabular",
                "\\begin{adjustbox}{max width=\\textwidth}\n\\begin{tabular"
            )
            content = content.replace(
                "\\end{tabular}",
                "\\end{tabular}\n\\end{adjustbox}"
            )
            latex_document.append(content)
        else:
            latex_document.append(content)

    elif filename.endswith('.txt'):
        content = read_content(filename)
        content = escape_latex_special_chars(content)
        latex_document.append("\\clearpage\n" + content + "\\clearpage\n")

    elif filename.endswith('.png'):
        latex_document.append(
            "\\begin{figure}[H]\n"
            "\\centering\n"
            "\\includegraphics[width=\\linewidth]{" + filename + "}\n"
            "\\end{figure}\n"
            "\\par\n"
        )

# LaTeX document footer
latex_document.append("\\end{document}")

# Write the combined LaTeX document
with open(output_file_path, 'w') as file:
    file.write('\n'.join(latex_document))

print(f"LaTeX document generated at: {output_file_path}")

def tex_to_pdf(tex_file_path):
    # Make sure the .tex file exists
    if not os.path.exists(tex_file_path):
        print(f"The file {tex_file_path} does not exist.")
        return

    try:
        # Run pdflatex command with a timeout of 60 seconds
        process = subprocess.run(
            ['pdflatex', tex_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )

        # Check if pdflatex command ran successfully
        if process.returncode == 0:
            print(f"PDF generated successfully: {tex_file_path.replace('.tex', '.pdf')}")
        else:
            print("Failed to generate PDF. Here's the error:")
            print(process.stdout)
            print(process.stderr)
    except subprocess.TimeoutExpired:
        print("pdflatex command timed out.")

#
# tex_to_pdf(r'..\output\combined_document.tex')
#


