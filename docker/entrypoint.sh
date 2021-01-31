#!/bin/bash

declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /opt/container.env

echo "SHELL=/bin/bash
BASH_ENV=/opt/container.env
*/10 * * * * /usr/local/bin/python /opt/do-ddns.py > /proc/1/fd/1 2>/proc/1/fd/2
" > entry.txt

crontab entry.txt
cron -f -L /dev/stdout

