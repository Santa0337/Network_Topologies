import re
s='''Codes: C – connected, S – static, I – IGRP, R – RIP, M – mobile, B – BGP
D – EIGRP, EX – EIGRP external, O – OSPF, IA – OSPF inter area
N1 – OSPF NSSA external type 1, N2 – OSPF NSSA external type 2
E1 – OSPF external type 1, E2 – OSPF external type 2, E – EGP
i – IS-IS, L1 – IS-IS level-1, L2 – IS-IS level-2, ia – IS-IS inter area
* – candidate default, U – per-user static route, o – ODR
P – periodic downloaded static route

Gateway of last resort is not set

10.0.0.0/30 is subnetted, 2 subnets
C 10.10.10.0 is directly connected, Serial0/0/0
D 10.10.10.4 [90/2172416] via 10.10.10.2, 01:00:09, Serial0/0/0
C 192.168.10.0/24 is directly connected, FastEthernet0/0
D 192.168.20.0/24 [90/2172416] via 10.10.10.2, 01:00:09, Serial0/0/0
D 192.168.30.0/24 [90/2174976] via 10.10.10.2, 01:00:09, Serial0/0/0'''
def ip(s):
    pattern = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',s)
    return pattern
k=ip(s)
valid=[]
for i in k:
    parts=i.split('.')
    if all(0 <= int(p) <= 255 for p in parts):
        valid.append(i)
print(f"these are the valid ip's from the log {valid}")
def private_ip(valid):
    class_a=[]
    class_b=[]
    class_c=[]
    for i in valid:
        parts=i.split('.')
        if int(parts[0])==10:
            class_a.append(i)
        if int(parts[0])==172 and int(parts[1])==16:
            class_b.append(i)
        if int(parts[0])==192 and int(parts[1])==168:
            class_c.append(i)
    result = f"class_a ip's are {class_a}\n class_b ip's are {class_b} \n class_c ip's are {class_c}"
    print(result)
def class_full(valid):
    class_a=[]
    class_b=[]
    class_c=[]
    for i in valid:
        first_octet = int(i.split('.')[0])
        if 1 <= first_octet <= 126:
            class_a.append(i)
        elif 128 <= first_octet <= 191:
            class_b.append(i)
        elif 192 <= first_octet <= 223:
            class_c.append(i)
    result = f"class_a ip's are {class_a}\nclass_b ip's are {class_b}\nclass_c ip's are {class_c}" 
    print(result)
private_ip(valid)
class_full(valid)
def network_broadcast(valid):
    network=[]
    broadcast=[]
    for i in valid:
        o = list(map(int, i.split('.')))
        first = o[0]
        if (first==10 and o[1]==0 and o[2]==0 and o[3]==0) or (first==192 and o[1]==168 and o[2]==0 and o[3]==0) or (first==172 and o[1]==16 and o[2]==0 and o[3]==0):
            network.append(i)
        if (first==10 and o[1]==255 and o[2]==255 and o[3]==255) or (first==192 and o[1]==168 and o[2]==255 and o[3]==255) or (first==172 and o[1]==16 and o[2]==255 and o[3]==255):
            broadcast.append(i)
    result= f"all the network id's {network} \n all the broadcast id's {broadcast}"
    print(result)
network_broadcast(valid)
