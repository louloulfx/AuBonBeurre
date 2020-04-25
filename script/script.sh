#!/bin/bash

set -e

exec python ./server.py & 
exec python ./generate.py