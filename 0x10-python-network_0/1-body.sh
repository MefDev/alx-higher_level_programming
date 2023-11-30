#!/bin/bash
# get the body
status_code=$(curl -sI "$1" | grep "HTTP/1.1" | awk '{print $2}' 2>/dev/null); if [ "$status_code" = "200" ]; then curl -X GET "$1"; fi
