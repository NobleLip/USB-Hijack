# USB-Hijack
```
UU   UU  SSSSS  BBBBB          HH   HH iii   jjj                kk     
UU   UU SS      BB   B         HH   HH             aa aa   cccc kk  kk 
UU   UU  SSSSS  BBBBBB  _____  HHHHHHH iii   jjj  aa aaa cc     kkkkk  
UU   UU      SS BB   BB        HH   HH iii   jjj aa  aaa cc     kk kk  
 UUUUU   SSSSS  BBBBBB         HH   HH iii   jjj  aaa aa  ccccc kk  kk 
                                           jjjj                        
```
  
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

## 2º Step

After step one is done, we just need to convert all the data to a compressed file and store it with the proper name, in this case, the name will be the Volume Serial Number. 
First, I was using zipfile library to do this, but I came across shutil library, since i dont need to over comlicate the project i used shutil to compress the directory and store it on the same folder as the script.

## 3º Step

Just run the code in the background, and let it do the work, every 10 seconds the code search for a USB Removable Driver, if detected the data of the usb will be hijacked. 

** Dont Remove the Driver, let the Script compress all the files before u do **
