#!/usr/bin/env zsh

# Start with a basic command to simulate. We'll robust it later.
while read LOG; do echo $LOG | nc -u -w 0 127.0.0.1 514; done < firewall_logs.log
