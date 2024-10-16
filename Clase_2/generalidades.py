import os

print(f"Sistema operativo: {os.name}")
"""
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
"""

os.system(os.system("cls") if os.name == "nt" else os.system("clear"))
