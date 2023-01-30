from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.1'
DESCRIPTION = 'A python based tool for prediction patient diagnosis i.e. (Alzheimer or Healthy) from single cell data.'
LONG_DESCRIPTION = (this_directory/"README.md").read_text()

# Setting up
setup(
    name="AlzScPred",
    version=VERSION,
    author="Aman Srivastava and Akanksha Jarwal",
    author_email="<aman20333@iiitd.ac.in>",
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas','numpy','tensorflow','keras',],
    keywords=['python', 'Alzheimers', 'Diagnosis', 'Single cell', 'Genomics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    license_files='LICENSE.txt'
)
