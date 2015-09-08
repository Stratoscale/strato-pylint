#! /bin/bash

DIR_PATH=`dirname $0`
if [ -z "${PYLINTRC_PATH}" ]; then
    PYLINTRC_PATH=$DIR_PATH/.pylintrc
fi

ENABLE_CHECKER=""
if [ $CHECK_CONVENTIONS = yes ] ; then
	ENABLE_CHECKER="C0102,C0103,C0112,C0121,C0202,C0203,C0204,C0303,C0304,C0321,C0322,C0323,C0324,C1001"
fi

PYTHONPATH=$DIR_PATH:$PYTHONPATH find $1 -type f -iname "*.py" -exec pylint --enable="$ENABLE_CHECKER" --rcfile=$PYLINTRC_PATH -r n '{}' ';' | ack --passthru --nocolor --match ".*"
if [ $? == 0 ] ; then
  exit 1
fi
exit 0
