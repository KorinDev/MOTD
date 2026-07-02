#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

HOME = Path.home()
BIN_DIR = HOME / ".local" / "bin"
BASH_RC = HOME / ".bashrc"
MOTD_SRC = Path("motd.py")

def install():
    BIN_DIR.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(MOTD_SRC, BIN_DIR / "motd")
    os.chmod(BIN_DIR / "motd", 0o755)
    
    motd_file = HOME / ".motd"
    if not motd_file.exists():
        with open(motd_file, 'w') as f:
            f.write(f"Whoopsie do! you need to edit me!~ go to ${motd_file} and write some stuff!")
        print("Created ~/.motd")
    
    print("MOTD installed successfully")
    print("   Run 'motd' to see your motd.")
    print("   Edit ~/.motd to add more.")

if __name__ == "__main__":
    install()
