#!/bin/bash
flake8 --ignore=E501 $1
if [ $? == 0 ] ; then
  exit 1
fi
exit 0
