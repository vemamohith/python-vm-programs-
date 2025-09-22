import re

# str1 = """2025-09-10 12:01:45 INFO User login from 192.168.1.10
# 2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
# 2025-09-10 12:01:45 INFO User login from 192.168.1.10
# 2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
# 2025-09-10 12:05:12 INFO User logout from 172.16.0.7
# 2025-09-10 12:07:33 WARN Suspicious traffic from 192.168.1.10"""

# pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# matching = re.findall(pattern,str1)

# matchingunqiue = set(matching)

# for i in matchingunqiue:
#     if matching.count(i) > 1 :
#         print(i , ": ", matching.count(i))


# str2 = """
# Interface              IP-Address      OK? Method Status        Protocol
# GigabitEthernet0/0     192.168.1.1     YES manual up            up
# GigabitEthernet0/1     unassigned      YES unset  administratively down down
# FastEthernet0/0        10.0.0.1        YES manual up            up
# Loopback0              127.0.0.1       YES manual up            up
# Vlan1                  172.16.0.1      YES manual down          down
# Serial0/0/0            unassigned      YES unset  down          down
# """


# pattern = r"(\S+\d+).*?(up|down|administratively down)"

# res = dict(re.findall(pattern,str2))
# for i,j in res.items() :
#     print("'interface' :'" ,i, "'status : '" , j)
# print(type(res))



# st1 = """
# Router#show ip ospf neighbor Neighbor ID Pri State Dead Time Address Interface 
# 100.1.1.1 1 FULL/BDR 00:00:35 2.0.0.1 GigabitEthernet0/0 
# 102.1.1.1 1 FULL/DR 00:00:35 3.0.0.2 GigabitEthernet0/1 
# 107.1.1.1 0 FULL/  00:00:35 4.0.0.2 Serial0/0/0
# """

# patt  = r'(\S+\d+)\s+\S+\s+\S+\s+(\S+\s+)\S+\d+\s+\S+\d+'
# res = re.findall(patt,st1)
# print(res)

# str1 = """
# Protocol  Address          Age (min)  Hardware Addr   Type   Interface
# Internet  192.168.1.1             0   aabb.cc00.0100  ARPA   GigabitEthernet0/0
# Internet  192.168.1.2            15   aabb.cc00.0200  ARPA   GigabitEthernet0/1
# Internet  192.168.1.3            12   aabb.cc00.0300  ARPA   GigabitEthernet0/2
# """

# pattern = r'\S+\s+(\S+\d+)\s+\d+\s+\S+\s+\S+\s+(\S+\d+)'

# res = re.findall(pattern,str1)
# for address,interface in res :
#     print(address ,"is reachable via " , interface)
# print(res)


# str1 = """
# Interface              IP-Address      OK? Method Status                Protocol
# FastEthernet0/0        192.168.1.1     YES manual up                    up
# FastEthernet0/1        unassigned      YES unset administratively down  down
# FastEthernet1/0        10.0.0.1        YES manual up                    up
# """

# # FastEthernet0/0 has IP 192.168.1.1 and is up/up


# pattern = r'(\S+\d+)\s+(\S+)\s+\S+\s+\S+\s+(administratively down |down|up)\s+(\S+)'

# res = re.findall(pattern,str1)
# for interface,ipaddress,status,protocol in res:
#     print(interface,"has IP ",ipaddress ,"and is ",status,"/",protocol)
# print(res)


# str1 = """
#     10.0.0.0/24 is subnetted, 1 subnets
# C       10.0.0.0 is directly connected, FastEthernet0/0
# O       192.168.1.0/24 [110/2] via 10.0.0.2, 00:00:12, FastEthernet0/1
# O       172.16.0.0/16 [110/3] via 10.0.0.2, 00:00:10, FastEthernet0/1
# """
# # 192.168.1.0/24 reachable via 10.0.0.2 over FastEthernet0/1
# # 172.16.0.0/16 reachable via 10.0.0.2 over FastEthernet0/1


# pattern=r"\S+\s+(\S+\d+)\s+\S+\s+\S+\s+(\S+\d+)\,\s+\S+\s+(\S+\d+)"

# res = re.findall(pattern,str1)
# for ipaddress,viaip,interface in res:
#     print(f"{ipaddress} reachable via {viaip} over {interface}")


# print(res)


# str1 = """
# Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
# 10.0.0.2        4 65001     120     118        3    0    0 00:05:23        5
# 10.0.0.3        4 65002     200     199        3    0    0 00:10:42        8
# """

# # Neighbor 10.0.0.2 in AS 65001 has 5 prefixes


# pattern = r"(\S+\d+)\s+\S+\s+(\S+\d+)\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+(\S+)"
# res = re.findall(pattern,str1)
# for neighbor,asnumber,state in res:
#     print(f"Neighbor {neighbor} in AS {asnumber} has {state} prefixes") 
# print(res)


# str1 = """
# Mar  1 00:00:30.415: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up
# Mar  1 00:01:12.123: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to down
# """
# # FastEthernet0/0 changed state to up
# # FastEthernet0/1 changed state to down

# pattern = r"(\S+\d+\/\d+)\S+\s+\S+\s+\S+\s+\S+\s+(\S+)"

# res = re.findall(pattern,str1)
# for interface, status in res:
#     print(f'{interface} changed state to {status} ')
# print(res)

# str1 = """
# Tracing route to 8.8.8.8 over a maximum of 30 hops
#   1     2 ms     1 ms     1 ms  192.168.1.1
#   2    10 ms    11 ms     9 ms  10.0.0.1
#   3    25 ms    23 ms    22 ms  203.0.113.1
#   4    40 ms    39 ms    41 ms  8.8.8.8
# """

# pattern = r"\s+(\d+).*?(\S+\d+)$"

# res = re.findall(pattern,str1,re.MULTILINE)
# print(res)


str1 = """
VLAN Name                             Status    Ports
1    default                          active    Fa0/1, Fa0/2
10   Sales                            active    Fa0/3, Fa0/4
20   Marketing                        active    Fa0/5
"""

# VLAN 1 (default) active on ports Fa0/1, Fa0/2  
# VLAN ID, Name, Ports)

pattern = r"\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+.*?)$"

res = re.findall(pattern,str1,re.MULTILINE)

for vlanid,name,status,ports in res:
    print(f"VLAN {vlanid} ({name}) {status} on ports {ports} ")
print(res)
