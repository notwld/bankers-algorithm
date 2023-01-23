#!/bin/bash

echo "Enter number of processes: " 
read num_processes
echo "Enter number of resources: "
read num_resources
python3 modified_banker.py  $num_resources $num_processes
