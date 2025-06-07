#!/bin/bash
echo "Menyalakan BOT..."
nohup python bot.py > log.txt 2>&1 &
echo "BOT sedang berjalan di background."
