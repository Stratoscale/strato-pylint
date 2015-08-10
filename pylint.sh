#! /bin/bash

DIR_PATH=`dirname $0`
if [ -z "${PYLINTRC_PATH}" ]; then
    PYLINTRC_PATH=$DIR_PATH/.pylintrc  
fi

PYTHONPATH=$DIR_PATH:$PYTHONPATH find $1 -type f -iname "*.py" -exec pylint --rcfile=$PYLINTRC_PATH -r n '{}' ';' | ack --passthru --nocolor --match ".*"
if [ $? == 0 ] ; then
  exit 1
fi
exit 0
