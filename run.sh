#!/bin/bash

printf '\e[?1049h'

while true; do
	clear
	python cfg.py
	read -rsn1 input
	if [ $input == "q" ]; then
		break
	fi
done

printf '\e[?1049l'

