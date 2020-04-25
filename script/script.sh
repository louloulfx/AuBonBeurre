#!/bin/bash

#set -e
exec python3 -u /server.py &
exec python3 -u /generate.py $1