#!/bin/bash
# Get bytes sie of url
curl -s "$1" | wc -c
