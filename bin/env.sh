#!/bin/bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

SRC_PATH=$CURDIR/../src
CONF_PATH=$CURDIR/../conf

cd $CONF_PATH
LOG_PATH=`awk -F '=' '/\[loger\]/{a=1}a==1&&$1~/path/{print $2;exit}' app.conf`
OUT_PATH=$LOG_PATH/output