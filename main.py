import subprocess
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

print("STARTED")

find_networks()
print("enter the number following the network ssid to select")
for i in range(len(ssid_list)):
    print(f"> {ssid_list[i]} < ({i})")
selected_network = input("Enter number here: ")