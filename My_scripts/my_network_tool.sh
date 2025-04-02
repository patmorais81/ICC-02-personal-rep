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

        1) ip a;exit 0;;

        2) ping "google.com";exit 0;;

        3) nmap -sn 127.0.0.1;exit 0;;

        4) netstat -r;exit 0;;

        5) traceroute google.com;exit 0;;

        6) echo "Exiting ...";exit 0;;

        *) echo "None of the above";

    esac

done

