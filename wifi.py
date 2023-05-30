# import subprocess
#
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))
# input("")
#
# import subprocess
#
#
# network_name = "Get your own wifi" #your_wifi_network_name
#
# result = subprocess.run(['netsh', 'wlan', 'show', 'profile', network_name, 'key=clear'], stdout=subprocess.PIPE)
# output = result.stdout.decode()
#
# for line in output.split('\n'):
#     if "Key Content" in line:
#         print(line.split(":")[1].strip())

for x in range(1,11):
    if x == 10:
        break
        print("reached max number")



