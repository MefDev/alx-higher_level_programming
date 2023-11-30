#!/bin/bash
# display the allowed options
curl -sX OPTIONS -i $1 | grep Allow | cut -d ' ' -f2-
