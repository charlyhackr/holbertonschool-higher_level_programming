#!/bin/bash
# Bash scripts that sends a POST request to a given url
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
