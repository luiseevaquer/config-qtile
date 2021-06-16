#!/bin/bash
# Num  Colour    #define         R G B
# 0    black     COLOR_BLACK     0,0,0
# 1    red       COLOR_RED       1,0,0
# 2    green     COLOR_GREEN     0,1,0
# 3    yellow    COLOR_YELLOW    1,1,0
# 4    blue      COLOR_BLUE      0,0,1
# 5    magenta   COLOR_MAGENTA   1,0,1
# 6    cyan      COLOR_CYAN      0,1,1
# 7    white     COLOR_WHITE     1,1,1
NC=`tput sgr0` # Reset 
BOLD=`tput bold` # Bold
BLINK=`tput blink` # Blink
FCOLOR=`tput setaf $4` # Foreground Color
BCOLOR=`tput setab $5` # Background Color
while true
do
    echo -e "Red: ${FCOLOR}${BCOLOR}${BOLD} $3 ${NC}"
    prettyping $1 -I $2 -c 350 --last 100 --nolegend
    clear
done
