#!/bin/bash
# Aosmix - Minimalist Termux Theme
# Author: Hynx Studios

# Load colors
source $HOME/Aosmix/colors.properties

# Clear screen
clear

# Show banner
cat $HOME/Aosmix/banner.txt | lolcat

# Show MOTD
echo -e "${GREEN}Welcome to Aosmix - Minimalist Termux Theme${RESET}"
echo -e "${BLUE}Type 'help' to see custom commands${RESET}"
