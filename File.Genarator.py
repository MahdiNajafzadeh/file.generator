import time
import os
def clear():
    os.system("cls")
# ---------------------
text = "*" * (1024 ** 2)
TimeNumber = [5,4,3,2,1]
SizeNumber = 1
# ---------------------
print(      "Location Example ====> C:\\new folder\\")
Des = input("Location Create File : ")
Sure = True if input("Are You Sure About that ? XD -- [Type \"Yes\" to Continue] : ") == "Yes" else False
# -----------------------------------
if Sure :
    print("Creating File ...")
    File = open(f"{Des}t.txt","a")
    print("Created File !")
    # -------------------------------
    for Time in TimeNumber:
        clear()
        print(f"Starting in {Time} Sec")
        time.sleep(1)
    # --------------------------------    
    while(Sure):
        clear()
        File.write(text)
        print(f"Size File = {SizeNumber} MB")
        SizeNumber += 1
    File.close()