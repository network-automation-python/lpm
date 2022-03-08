# LPM
Using Pandas &amp; Numpy for implementing **LPM -longest prefix match** logic for IPv4 prefixes

**LPM** - Is a route-lookup logic. Typically this logic, in most packet forwarding software such as the Linux kernel or in software routers is implemented using a Patricia Trie. In packet switching ASICs, the LPM is typically implemented using a TCAM (Ternary CAM). 
So why this code in Python using Pandas? -Because I needed it for my team to identify subnets and their associated attributes without doing manual excel lookups for various reasons.

**Few sample outputs:**

**1- Code output when IP "10.7.0.10" was supplied as destination IP in the script, which matches to major network 10.0.0.0/8 and subnet "10.7.0.8/30", subnet 10.7.0.8/30 was only retuned by the script using Longest prefix match method.**
+--------------+---------------+
|              | 10.7.0.8/30   |
|--------------+---------------|
| Comment      | Subnet-18     |
| Location     | DC-1          |
| VLAN         | 18.0          |
| Firewall     | DC-1-FW-1     |
| Secrity_Zone | Trust         |
+--------------+---------------+

**2- Code output when IP "10.20.0.10" was supplied as destination IP in the script, which matches to major network "10.0.0.0/8" with Longest prefix match method.**
+--------------+--------------+
|              | 10.0.0.0/8   |
|--------------+--------------|
| Comment      | Company NET  |
| Location     | DC1/2        |
| VLAN         | nan          |
| Firewall     | nan          |
| Secrity_Zone | Untrust      |
+--------------+--------------+

**3- Code output when IP "10.12.8.1" was supplied as destination IP in the script, which matches to major network "10.0.0.0/8", subnets 10.12.8.0/23 & 10.12.8.0/24, Subnet 10.12.8.0/24 was only retuned by the script using Longest prefix match method.**
+--------------+----------------+
|              | 10.12.8.0/24   |
|--------------+----------------|
| Comment      | Subnet-47      |
| Location     | DC-2           |
| VLAN         | 47.0           |
| Firewall     | DC-2-FW-2      |
| Secrity_Zone | DMZ            |
+--------------+----------------+
