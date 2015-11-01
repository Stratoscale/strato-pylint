#! /bin/bash
base=$1
shift
find $base -type f -iname "*.py" -exec pep8 "$@" --max-line-length=145 '{}' ';' | ack --passthru --nocolor --match ".*"
if [ $? == 0 ] ; then
  exit 1
fi
exit 0
