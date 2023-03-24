#!/bin/bash

cd ../../Projects/00-sample-voting-app

docker compose up

host="$(hostname -i || echo '127.0.0.1')"

echo "Congrats! Task executed completely!"
echo "The voting app was available on $host:8080 port"
echo "The resulting app was available on $host:8081 port"
echo "The end of the script"