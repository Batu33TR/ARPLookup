import argparse
import scapy.all as scapy


class ARPLookup():
    def __init__(self):
        print("ARPLookup started")

    def getUserInput(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-r', '--range', type=str, help="Enter an IP range for detecting other devices")
        args = parser.parse_args()

        if args.range != None:
            print(f"Broadcasting to " + args.range) # Debugging
            return args
        else:
            print("Usage: python arplookup.py -r <IP_RANGE>")
            exit()
    
    def broadcast_network(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet
        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
        answered_list.summary()


if __name__ == "__main__":
    arp_lookup = ARPLookup()
    user_input = arp_lookup.getUserInput()
    arp_lookup.broadcast_network(user_input.range)
