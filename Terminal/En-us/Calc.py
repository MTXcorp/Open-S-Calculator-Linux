import os as sys

Status = "none"
Mode = "none"
print("Open-Source Calculator")
Status = "ch-mode"
def modech():
    print("Choose Mode:")
    print("--p  - Plus")
    print("--m  - Minus")
    print("--t  - Times")
    print("--s  - Split")
    modeinp = input("|Mode|>")
    if modeinp == "--p":
        Mode = "plus"
        Status = "ready"
    elif modeinp == "--m":
        Mode = "minus"
        Status = "Ready,Verif-Other"
while Status == "run":
    calc = input("|>")
    if calc == "exit":
        Status = "exit"
    elif calc == " --mode":
        modech()
    elif calc == 