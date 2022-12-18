from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

filename = datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p")

junos = {
    'device_type': 'juniper_junos',
    'host':   input('Hostname or IP Address: '),
    'username': input('Username: '),
    'password': getpass(),
    'port' : 22,
    'session_log': filename + '.txt'
}

net_connect = ConnectHandler(**junos)


def vlan_exists(vlan):
    if isinstance(vlan, int) == True:
        vlan = str(vlan)
    output = net_connect.send_command('show vlans ' + vlan, use_textfsm=True)
    if type(output) == str:
        # TextFSM parser will fail if the output doesn't contain data,
        # When it fails it returns a string of the output
        print(output)
        print('VLAN: ' + vlan + ' does NOT exist.')
        return False
    elif type(output) == list:
        # TextFSM parser will return a list of dictionaries when the table
        # contains data
        print(output)
        print('VLAN: ' + vlan + ' already exists.')
        return True

def add_vlan(vlan,name,desc):
    if isinstance(vlan, int) == True:
        vlan = str(vlan)
    if isinstance(desc, str) == False:
        print('Please enter description variable as a string value.')
        return None
    if isinstance(name, str) == False:
        print('Please enter VLAN name variable as a string value.')
        return None
    if vlan_exists(vlan) == False:
        print('All Good, Ready for new configs.')
        vlan_name = 'v' + vlan + '-' + name
        vlan_desc = vlan_name + ': ' + desc
        commands = [
                    'set vlans ' + vlan_name + ' vlan-id ' + vlan + ' description \"' + vlan_desc + '\"',
                    'set interfaces et-0/0/24 unit 0 family ethernet-switching vlan members ' + vlan_name,
                    'set interfaces xe-0/0/23 unit 0 family ethernet-switching vlan members ' + vlan_name,
                    'show | compare'
                   ]
        output = net_connect.send_config_set(commands, exit_config_mode=False)
        output += net_connect.commit()
        print('Configs changed. New configs added. Check ' + filename + '.txt for log.')
    else:
        print('Did NOT change configs, something already existed.')
        net_connect.disconnect()
        return None

def main():
    #pint = input('Parent Interface: (example: \'eth1\'')
    vlan = 99
    #addr = '99.99.99.1/24'
    name = 'TEMP'
    desc = 'Automation Test'
    add_vlan(vlan,name,desc)
    net_connect.disconnect()

if __name__ == '__main__':
    main()
