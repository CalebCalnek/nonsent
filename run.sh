#!/bin/bash

printf '\e[?1049h'
clear

while true; do
	python cfg.py
	read -rsn1 input
	case $input in
		c) clear ;;
		q) break ;;
		*) continue ;;
	esac
done

printf '\e[?1049l'

