#!/usr/bin/env python3
# switch.py
# Switch script
# CIS3534C - Scripting for Network Professionals

from networkdevice import NetworkDevice

class Switch(NetworkDevice):
    
    # counter for how many switches are created
    counter = 0

    def __init__(self, IPAddr, MACaddr, hostname, gateway="0.0.0.0"):
        super().__init__(IPAddr, MACaddr)
        
        self.__hostname = self.validateHostname(hostname)
        self.__gateway = self.validateIP(gateway)
        
        #adds to the counter
        Switch.counter += 1

    def getHostname(self):
        #gives hostname
        return self.__hostname

    def getGateway(self):
        #gives gateway
        return self.__gateway

    def validateHostname(self, hostname):
        #makes sure hostname is valid
        if len(hostname) > 0:
            return hostname
        else:
            return "Switch Name Unknown"

    def setHostname(self, hostname):
        #updates hostname
        self.__hostname = self.validateHostname(hostname)

    def setGateway(self, gateway):
        #updates gateway
        self.__gateway = self.validateIP(gateway)

    def __str__(self):
        
        return "Your switch:  " + super().__str__() + \
            f"\n    hostname: {self.__hostname}, default gateway {self.__gateway}"

def main():
    # testing valid
    switch1 = Switch("192.168.1.99", "AA:BB:CC:DD:EE:FF", "switch1", "192.168.1.1")
    print(switch1)
    print()

    #testing invald
    switch2 = Switch("888.888.888.888", "AA:BB:CC:11:22:33", "", "192.168.1.1")
    print("Your switch: ", switch2)
    print()

    # testing update
    switch1.setHostname("WavyBlue")
    print("Your updated switch: ", switch1)
    
    # testing counter
    print("You created", Switch.counter, "switches today!")

if __name__ == "__main__":
    main()