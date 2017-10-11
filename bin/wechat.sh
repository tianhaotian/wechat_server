#!/bin/bash



CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

SRC_PATH=$CURDIR/../src
CONF_PATH=$CURDIR/../conf

cd $CONF_PATH
LOG_PATH=`awk -F '=' '/\[loger\]/{a=1}a==1&&$1~/path/{print $2;exit}' app.conf`

if [ ! -x "$LOG_PATH" ]; then
  mkdir "$LOG_PATH"
fi
OUT_PATH=$LOG_PATH/output

function shutdown(){
    count=`ps -ef |grep $1|grep $2|grep -v "grep"|awk '{print $2}'|xargs kill -9`
    echo 'kill success'
}

function start_server(){
    cd $SRC_PATH&& nohup python gis_server.py $1 > $OUT_PATH 2>&1 &
    echo $1
    echo 'start success'
}
function stop(){
    count=`ps -ef |grep gis_server.py |grep -v 'grep'|awk '{print $10}'|sort|uniq`
    echo $count
    count1=($count)
    declare -p count1
    for item in ${count1[@]};do
        echo $item
        shutdown gis_server.py $item
    done
}

function get_server_options(){
    count=`ps -ef |grep gis_server.py |grep -v 'grep'|awk '{print $10}'|sort|uniq`
    echo $count
    count1=($count)
    declare -p count1
    for item in ${count1[@]};do
        echo $item
        shutdown gis_server.py $item
    done
    for item in ${count1[@]};do
        start_server $item
    done
}

function usage(){
    echo 'Usage : bash gis.sh [参数]'
    echo '参数 : start ------ 启动服务'
    echo '       stop ------ 停止服务'
    echo '      restart ------ 重启服务'
}


function clean(){
    count=`ps -ef |grep gis.sh|grep -v 'grep'|awk '{print $2}'|xargs kill -9`
    echo 'finish'
}
if [ $# -eq 1 ];then
    if [ $1 == 'start' ];then
        cd $CONF_PATH
        port=`awk -F '=' '/\[port\]/{a=1}a==1&&$1~/port/{print $2;exit}' app.conf`

        ports=(${port//,/ })

        for i in ${ports[@]}
        do
            start_server $i
        done

        echo 'server start success'
        clean

    elif [ $1 == 'stop' ];then
        stop

    elif [ $1 == 'restart' ];then
        get_server_options
        clean
    else
        usage
    fi
else
    usage
fi