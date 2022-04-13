# USB-Hijack
  
##  1º Step
 
 First we need to get the best way of detecting the drivers connected to the computer, since we are in Windows, the best way to detect USB pendrives, is to run the comand on the powershell:
 ```
 Get-WmiObject -Class Win32_LogicalDisk
 ```
+ The output of the powershell will give me 5 important informations to this project:
  + Device ID            -> Important since this is the path to all the files.
  + Volume Serail Number -> Used to blacklist the driver after the hijack, to prevent deleting old files and run the code over and over.
  + Free Space           -> Free Space of the Drive.
  + Size                 -> Size of the Drive.
  
  + Driver Type:
    + 0 : Unknown
    + 1 : No Root Directory
    + 2 : Removable Disk  <- We will use this one.
    + 3 : Local Disk
    + 4 : Network Drive
    + 5 : Compact Disc
    + 6 : Ram Disk

Since i just need this 5 important informations , i will just run the code to exclusively get them and convert them directly to json:
 ```
 Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid, volumeserialnumber, drivetype, freespace, size| ConvertTo-Json
 ```


