#!/usr/bin/env python
import ipaddress
list1 = '''
208.65.144.0/21
208.81.64.0/21
129.232.225.234/32
129.232.226.2/32
185.212.104.0/22
161.69.22.122/32
208.42.251.123/32
108.60.148.187/32
162.250.3.37/32
108.60.136.186/32
108.60.136.187/32
108.60.148.186/32
108.60.150.130/32
108.60.150.131/32
161.69.14.137/32
161.69.14.139/32
162.250.3.36/32
184.75.215.242/32
184.75.215.98/32
208.65.150.192/32
208.65.151.192/32
54.207.98.206/32
54.94.201.194/32
74.91.14.2/32
74.91.14.3/32
161.69.112.0/20
185.125.224.0/22
52.2.191.60/32
52.201.117.185/32
52.201.118.139/32
52.201.126.139/32
52.38.180.253/32
52.38.193.184/32
52.38.57.115/32
52.8.124.42/32
52.86.6.124/32
52.9.157.23/32
52.9.171.209/32
54.233.172.148/32
54.233.176.255/32
54.233.186.156/32
54.94.215.173/32
54.94.230.23/32
185.212.104.0/22
124.47.168.139/32
161.69.192.123/32
161.69.206.27/32
203.97.87.59/32
103.231.89.18/32
103.231.89.22/32
120.138.17.53/32
120.138.17.54/32
208.81.65.192/32
208.81.66.192/32
208.81.67.192/32
208.81.69.192/32
43.240.64.104/32
43.240.64.105/32
43.249.37.35/32
43.249.37.38/32
49.50.81.12/32
49.50.81.17/32
161.69.240.0/20
185.125.224.0/22
52.196.141.193/32
52.62.9.167/32
52.62.96.66/32
52.63.18.189/32
52.68.234.173/32
52.69.46.184/32
52.74.5.157/32
52.77.108.133/32
52.79.175.47/32
52.79.50.71/32
185.212.104.0/22
193.128.33.248/32
208.81.64.248/32
208.81.64.192/32
208.81.68.192/32
213.239.220.71/32
213.239.220.72/32
78.46.116.105/32
161.69.176.0/20
185.125.224.0/22
52.50.161.113/32
52.50.234.32/32
52.58.111.233/32
52.58.116.88/32
52.58.127.186/32
185.37.148.186/32
185.37.148.187/32
'''

list2 = list1.splitlines()


for i in list2:
    if i:
        mask = ipaddress.IPv4Network(i).netmask
        ip = ipaddress.IPv4Network(i).network_address
        if str(mask) == '255.255.255.255':
            print('access-list RAS_VPN_TUNNEL_ALL_EXCLUDE standard permit host ' + str(ip))
        else:
            print('access-list RAS_VPN_TUNNEL_ALL_EXCLUDE standard permit ' + str(ip) + ' ' + str(mask))

