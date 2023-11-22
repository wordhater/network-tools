import subprocess

##### FUNCTIONS #####
def find_networks():
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

networks = find_networks()