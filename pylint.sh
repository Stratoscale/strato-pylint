#! /bin/bash
find $1 -type f -iname "*.py" -exec pylint --rcfile=`dirname $0`/.pylintrc -r n '{}' ';'
