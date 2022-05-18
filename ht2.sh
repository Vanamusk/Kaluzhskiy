#!/bin/bash
cd ~
echo "time: $(date)" > info.txt 
echo "username:" $USER >> info.txt
echo "os:" $OSTYPE >> info.txt
echo "home directory: $(pwd)" >>  info.txt
echo "files: $(ls -R | wc -l)" >>   info.txt
#ls -R | wc -l | tee -a info.txt
echo "folders: $(ls -la | grep "^d" | wc -l)" >> info.txt
#ls -la | grep "^d" | wc -l | tee -a  info.txt
