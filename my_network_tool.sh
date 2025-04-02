#!/bin/bash

while true; do

    clear;

    echo "Choose an option:"

    echo ""

    echo "  1) Check Network Interface Information"

    echo "  2) Ping a host"

    echo "  3) Port Scan with Nmap"

    echo "  4) Display Routing table"

    echo "  5) Traceroute to Host"

    echo "  6) Exit"

    echo ""         

    read -p "Enter choice [1-6]:" choice

    echo ""

    case $choice in 

        1) echo " -> Check Network Interface Information";exit 0;;

        2) echo "Ping a host";exit 0;;

        3) echo "Port Scan with Nmap";exit 0;;

        4) echo "Display Routing Table";exit 0;;

        5) echo "Traceroute to Host";exit 0;;

        6) echo "Exiting ...";exit 0;;

        *) echo "None of the above";

    esac

done

