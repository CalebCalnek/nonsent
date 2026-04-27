#!/bin/bash

printf '\e[?1049h'
clear

while true; do
	if [[ $@ == "--espeak" ]]; then
		python cfg.py | tee >(espeak-ng -v en-us+announcer -s 150)
	else
		python cfg.py
	fi
	read -rsn1 input
	case $input in
		c) clear ;;
		q) break ;;
		*) continue ;;
	esac
done

printf '\e[?1049l'
