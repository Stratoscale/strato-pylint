#! /bin/bash
DIR_PATH=`dirname $0`
PYTHONPATH=$DIR_PATH:$PYTHONPATH find $1 -type f -iname "*.py" -exec pylint --rcfile=$DIR_PATH/.pylintrc -r n '{}' ';' | ack --passthru --nocolor --match ".*"
if [ $? == 0 ] ; then
  exit 1
fi
exit 0
