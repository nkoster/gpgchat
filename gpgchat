#!/bin/bash

echo
echo "GPG chat 1.0"
echo

if [ $# -lt 4 ]; then
    echo "Usage: $0 <remote PGP id> <host> <local port> <remote port>"
    echo
    exit 1
fi

user_remote="$1"
host="$2"
port_local="$3"
port_remote="$4"

keys=$(gpg --list-keys "$user_remote" | grep -c '^$')
if [ $keys -gt 1 ]; then
    echo "Too many keys for remote user"
    exit 1
fi

export GPG_TTY=$(tty)

echo -n 'Private key password (will not echo): '
read -s password
echo
echo

echo "Starting listener at port $port_local"
while true ; do output=`ncat -l $port_local | gpg -d --batch --passphrase "$password" 2>/dev/null` ; echo -e "\033[32m${output}\033[0m" ; done &

echo -e "Initiating chat with ${user_remote} at $host, port $port_remote"
echo

while true
do
    read n
    echo "$n" | gpg -e -r "$user_remote" | ncat $host $port_remote
done

