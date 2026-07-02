#!/usr/bin/env python3
import os
import sys
import random
import datetime
from pathlib import Path


MOTD_VERSION = "0.1"
MOTD_SOURCE = Path.home() / ".motd"
CACHE_DIR = Path("/tmp")
CACHE_PREFIX = "MOTD"

def get_cache_filename():
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    return CACHE_DIR / f"${CACHE_PREFIX}-{date}.TEMP"

def get_random_motd():
    if not MOTD_SOURCE.exists():
        exit()

    with open(MOTD_SOURCE, 'r') as f:
        content = f.read()

    messages = [msg.strip() for msg in content.split("~!~") if msg.strip()]

    if not messages:
        exit()

    return random.choice(messages)

def clean_cache():
    for file in CACHE_DIR.glob(f"{CACHE_PREFIX}-*.TEMP"):
        file.unlink()

def refresh():
    cache_file = get_cache_filename()
    message = get_random_motd()
    with open(cache_file, 'w') as f:
        f.write(message)

def main():
    args = sys.argv[1:]

    if "clean" in args:
        clean_cache()
        return
    if "refresh" in args:
        refresh()
        return

    cache_file = get_cache_filename()
    if not cache_file.exists():
        refresh()

    with open(cache_file, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()
