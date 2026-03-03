# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

# def ips_between(start, end):
#     start = list(map(int, start.split(".")))
#     end = list(map(int, end.split(".")))
#     difference = list(map(lambda x: x[1]-x[0], zip(start,end)))
#     total = list(map(lambda x: x[1]* x[0], zip(difference,[256**3,256**2,256,1])))
#     return sum(total)


from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))
