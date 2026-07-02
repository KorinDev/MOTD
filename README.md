# MOTD
A simple "**M**essage **O**f **T**he **D**ay" script!

---

## Setup
1. To setup MOTD you need to run `install.py` which will setup the .local/bin folder, copy the motd.py file, and setup an alias in .bashrc.
2. To create "MOTD" messages, you'll need to create a `~/.motd` file.


## `.motd` Syntax
```
This is a message of the day!
~!~
The items are seperated by ~ ! ~.
~!~
Thanks to that,
They can be multiline!
```

## About
**MOTD** when ran, creates a file in /tmp.
more specifically, MOTD-DD-MM-YYYY.TEMP
that TEMP file contains:
Current **MOTD**.

MOTD automatically checks for MOTD-... files in /tmp, removing old ones, and checking if it should update.

You can always run `motd clean` or `motd refresh` to "change" the current MOTD and clear the TEMP files.
