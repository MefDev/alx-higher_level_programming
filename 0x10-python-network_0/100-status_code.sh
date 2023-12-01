#!/bin/bash
# delete and display the body
curl -sI $1 | grep HTTP/1.1 | awk '{print $2}'
