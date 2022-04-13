# USB-Hijack

## First Steps
  
 Since we are in Windows, the best way to detect USB pendrives, is to run the comand on the powershell:
 ```
 Get-WmiObject -Class Win32_LogicalDisk
 ```
+ The output of the powershell will give me 5 important informations to this project:
  + Device ID            -> Important since this is the path to all the files.
  + Volume Serail Number -> I Will use this to blacklist the driver after i hijack all data, to prevent deleting old files and run the code over and over.
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
