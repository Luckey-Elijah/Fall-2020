# Lab Homework 4

Elijah Luckey

Sept. 28, 2020

---

## A Ping Sweeping

![Angry IP Sweep](images/angry-ip.png)

---

## Port Scanning

### 1.

![Nmap Port SYN Scan](images/Nmap-Port-SYN-Scan.png)

### 2.

![Nmap Port NULL Scan](images/Nmap-Port-NULL-Scan.png)

### 3.

![Nmap Port XMAS Scan](images/Nmap-Port-XMAS-Scan.png)

### 4.

![Nmap Port Connect Scan](images/Nmap-Full-Connect-Scan.png)


---

## Packet Crafting

![Packet Crafting](images/packet-crafting.png)

---

## Discussion

Using these tools (`nmap`, `Angry IP Scanner`, and `hping`) can prove useful for testing network
insecurities for local systems. In this experiment, we didn't necessarily find any insecurities (since the connected devices are limited in number on the local network) but can see where each instance of the tools can be useful. The *Angry IP Scanner* and `nmap` tools both showed
`port 80` to be filtered/open in the experiment. Each of those tools can provide very wide scans
on teh network to reveal more open and even vulnerable ports.
