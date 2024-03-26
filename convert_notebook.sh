#!/bin/bash
jupyter nbconvert --to pdf --output notebooks notebooks/census2011.ipynb
jupyter nbconvert --to html --output notebooks notebooks/census2011.ipynb
jupyter nbconvert --to latex --output notebooks notebooks/census2011.ipynb
jupyter nbconvert --to markdown --output notebooks notebooks/census2011.ipynb