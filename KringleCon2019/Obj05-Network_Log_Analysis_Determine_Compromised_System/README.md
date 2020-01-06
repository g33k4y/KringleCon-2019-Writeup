## Problem Statement:

> 5) Network Log Analysis: Determine Compromised System  
Difficulty: 2/5  
> The attacks don't stop! Can you help identify the IP address of the malware-infected system using these Zeek logs? For hints on achieving this objective, please visit the Laboratory and talk with Sparkle Redberry.

td:lr Answer: **ntdsutil**

===============================================================================
## Solution(hint):

Let's visit Sparkle Redberry at _laboratory_ for the hint.

Spark wants to restart the laser by changing the configuration.

hint given for this sub-problem:

> [SANS' PowerShell Cheat Sheet](https://blogs.sans.org/pen-testing/files/2016/05/PowerShellCheatSheet_v41.pdf


Start up the terminal:  
![](./res/pic1.png)

Use following command to check for more info on the laser:  
`(Invoke-WebRequest -Uri http://localhost:1225/).RawContent`:  
![](./res/pic2.png)

We need to change 4 variables: refraction, temperature, angle and gas.

First clue:  
`type /home/callingcard.txt`  
![](./res/pic3.png)

`history | Format-Table -Autosize -Wrap`:  
![](./res/pic4.png)

At line 7, we get the angle value: 65.5

Look for environment variables. No clue in standard variables:  
`Get-ChildItem env: | Format-Table -Wrap`  
![](./res/pic5.png)

Riddle: Do a -Recurse on all /etc files, and sort to find the newest LastWriteTime:  
`dir /etc -Recurse | Sort-Object -Property LastWriteTime`:  
![](./res/pic6.png)

Unzip archive file in `/home/elf`:  
`Expand-Archive /etc/apt/archive -DestinationPath /home/elf`  
`cd /home/elf/refraction`  
`chmod +x runme.elf`  
`./runme.elf`  --get refraction?val=1.867

2nd Clue:  
`type riddle`:  
![](./res/pic7.png)

`$hash = type /home/elf/refraction/riddle | Select-String -Pattern "255"` --saves hash as a variable  
`Get-ChildItem -Path /home/elf/depths -Recurse -File | Get-FileHash -Algorithm MD5 | Format-Table -Wrap -AutoSize | Out-String -Stream | Select-String -Pattern $hash`  
![](./res/pic8.png)

`$file1=/home/elf/depths/produce/thhy5hll.txt"  
`type $file1` --get temperature?val=-33.5  

3rd clue:  
![](./res/pic9.png)

`Get-ChildItem /home/elf -Recurse -File | Sort-Object -Property Length`  --will find the txtfile with the deepest directory length `0jhj5xz6.txt`  
`$file2 = Get-ChildItem depths -Recurse -File -Name "0jhj*.txt"` -- register filepath as a variable  
`type $file2`:  
![](./res/pic10.png)

Kill process in order:  
`Get-Process -IncludeUserName`  
`Stop-Process -id 24`  --id might differ
`Stop-Process -id 25`  --id might differ
`Stop-Process -id 28`  --id might differ
`Stop-Process -id 29`  --id might differ
`type /shall/see`:  
![](./res/pic11.png)

`cd /etc`  
`$file = Get-ChildItem /etc -File -Recurse -Name "*.xml"` --event log found  
`type $file | Select-String gas`:  
![](./res/pic12.png)

We got all our values, so now to change the values on the laser:  
`Invoke-WebRequest -Uri http://localhost:1225/api/off`
`Invoke-WebRequest -Uri http://localhost:1225/api/refraction?val=1.867`
`Invoke-WebRequest -Uri http://localhost:1225/api/temperature?val=-33.5`
`Invoke-WebRequest -Uri http://localhost:1225/api/angle?val=65.5`
`$postParams=@{O=6;H=7;He=3;N=4;Ne=22;Ar=11;Xe=10;F=20;Kr=8;Rn=9}`
`Invoke-WebRequest -Uri http://localhost:1225/api/gas -Method POST -Body $postParams`
`Invoke-WebRequest -Uri http://localhost:1225/api/on`
`Invoke-WebRequest -Uri http://localhost:1225/api/output`:  
![](./res/pic13.png)








