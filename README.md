# Python 2 - Data analysis with pandas #

## Set up ##
The required dependencies for this project are:
 - matplotlib 3.8
 - pandas 2.2

The recommended way to setup is through the setup script:
```console
./setup.sh
```
This may take a minute or two.

## Running ##

### Jupyter notebook ###
The jupyter notebook provides an easy way to interact with this project.
To start the notebook with an environment providing all the correct dependencies:
```console
./start_notebook.sh
```
### Scripts for all requirements  
All:
```console
./run_all.sh <FILEPATH>
```
Refine data:
```console
./run_consistency.sh <FILEPATH>
```
Data analysis summary:
```console
./run_summary.sh <FILEPATH>
```
Execute queries:
```console
./run_queries.sh <FILEPATH>
```
Generate plots:
```console
./run_plots.sh <FILEPATH>
```
Performance tests:
```console
./run_performance.sh <FILEPATH>
```
Unit testing:
```console
./test.sh
```
### PDF/HTML/LaTeX/MD notebook ###
The following commands enable simple conversion of the jupyter notebook.
Copy and pasting the following commands into the terminal can produce the
results located into the notebooks directory. Because of the way LeTeX is 
formatted on the lab machines, this commands will not run. To get this as
a reproducible result, the commands will be to be run on a personal machine.

PDF:
```console
jupyter nbconvert --to pdf --output notebooks notebooks/census2011.ipynb
```
HTML:
```console
jupyter nbconvert --to html --output notebooks notebooks/census2011.ipynb
```
LaTeX:
```console
jupyter nbconvert --to latex --output notebooks notebooks/census2011.ipynb
```
MD:
```console
jupyter nbconvert --to markdown --output notebooks notebooks/census2011.ipynb
```
Alternatively you can run the following shell script to produce all of the
results above instantly.
```console
./convert_notebook.sh
```