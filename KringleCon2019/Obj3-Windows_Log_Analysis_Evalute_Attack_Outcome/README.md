## Problem Statement:

> 3) Windows Log Analysis: Evaluate Attack Outcome

> Difficulty: 1/5

> We're seeing attacks against the Elf U domain! Using the [event log data](./Security.evtx.zip), identify the user account that the attacker compromised using a password spray attack. Bushy Evergreen is hanging out in the train station and may be able to help you out.

td:lr Answer: **supatraa**

================================================================================================
## Solution:

**The following is done in Windows OS**

First we should look for Bushy Evergreen who is in the train station
He needs help to exit from the Ed Standard Text Editor

[Simple guide on Ed](http://cs.wellesley.edu/~cs249/Resources/ed_is_the_standard_text_editor.html)

A simple google or understanding on Ed will reveal the solution:

`Type w, then <enter>`

`Type q, then <enter>`


Having helped Bushy Evergreen with his task, he will hint that using the DeepBlueCLI might help with understanding the password spray attack artifacts we obtained from this problem.
[DeepBlueCLI Github](https://github.com/sans-blue-team/DeepBlueCLI)

Download the DeepBlueCLI zipfile from the github and extract it.
Download the [event log data](./Security.evtx.zip) from the objective.

Next we will run Powershell (*run as Administrator*).

`Navigate to DeepBlueCLI folder`

`.\DeepBlue.ps1 <filepath of the event log data>`

> if you encounter an error 'running scripts is disabled on this system', we will need to execute either:

`Set-ExecutionPolicy RemoteSigned`

`Set-ExecutionPolicy Bypass`

then re-run the DeepblueCLI again. (Will take a while for DeepBlueCLI to analyse the logs)

Looking through the logs, we will see that only 3 accounts has success logons, the rest failed. 

![](./pic1.png)

Answer: **supatree**



