#!/usr/bin/env python3
proto = ["ssh", "http", "https"] # List 1
protoa = ["ssh", "http", "https"] # List 2
print(proto) # Print List 1

proto.append("dns") # this line will add "dns" to the end of List 1
protoa.append("dns") # this line will add "dns" to the end of List 2
print(proto)# Print List 1 with dns add it the list

proto2 = [ 22, 80, 443, 53 ] #List 3,  a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)# Print List 1 with arguments from proto2 add it to the list
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)# Print List 2 with List 3 add to the end of the list as last item

