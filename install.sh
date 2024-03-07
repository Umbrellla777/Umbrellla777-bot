#!/usr/bin/env bash

####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla777        #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

# const
readonly version="1.0"
readonly c_error='\033[5m'
readonly c_yellow='\033[33m'
readonly c_red='\033[31m'
readonly c_green='\033[32m'
readonly c_def='\033[0m'

# Update
pkg update -y

# install python
echo "${c_green}[Установка] ${c_def} Python 3"
pkg3 install -y python3
clear

# install Libs for python
echo "${c_green}[Установка] ${c_def} Библиотка telethon для Python"
pip3 install telethon
clear

# Sucsess
cd Umbrellla777-bot
mkdir users
chmod +777 start
cp start ~/start
cd ~/
chmod +777 start
echo "${c_green}[Завершено]${c_def} Установка успешна завершена!"
echo "${c_green}[Запуск]${c_def} Выполните ./start api_id api_hash"
