from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

filename = datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p")

vyos = {
    'device_type': 'vyos',
    'host':   input('Hostname or IP Address: '),
    'username': input('Username: '),
    'password': getpass(),
    'port' : 22,
    'session_log': filename + '.txt'
}

net_connect = ConnectHandler(**vyos)


def subint_exists(vlan):
    if isinstance(vlan, int) == True:
        vlan = str(vlan)
    output = net_connect.send_command('show interfaces ethernet eth1.'+vlan+' brief', use_textfsm=True)
    if type(output) == str:
        # TextFSM parser will fail if the output doesn't contain data,
        # When it fails it returns a string of the output
        print('Sub-interface: eth1.'+vlan+' does NOT exist.')
        return False
    elif type(output) == list:
        # TextFSM parser will return a list of dictionaries when the table
        # contains data
        print('Sub-interface: eth1.'+vlan+' already exists.')
        return True

def addr_exists(addr):
    if isinstance(addr, str) == False:
        print('Please enter address variable as a string value:')
        print('\'99.99.99.1/24\'')
        return None
    output = net_connect.send_command('show interfaces', use_textfsm=True)
    for i in output:
        for a in i['ip_address']:
            if a == addr:
                print('Address: ' + addr + ' found on interface: ' + i['interface'])
                return True
    print('Address Does NOT Exist')
    return False

def add_subint_subnet(vlan,addr,desc):
    if isinstance(vlan, int) == True:
        vlan = str(vlan)
    if isinstance(addr, str) == False:
        print('Please enter address variable as a string value:')
        print('\'99.99.99.1/24\'')
        return None
    if isinstance(desc, str) == False:
        print('Please enter description variable as a string value.')
        return None
    if subint_exists(vlan) == False and addr_exists(addr) == False:
        print('All Good, Ready for new configs.')
        commands = [
                    'set interfaces ethernet eth1 vif ' + vlan + ' address ' + addr,
                    'set interfaces ethernet eth1 vif ' + vlan + ' description \'' + desc + '\''
                   ]
        output = net_connect.send_config_set(commands)
        output += net_connect.commit()
        output += net_connect.save_config()
        print('Configs changed. New configs added. Check ' + filename + '.txt for log.')
    else:
        print('Did NOT change configs, something already existed.')
        net_connect.disconnect()
        return None

def main():
    pint = input('Parent Interface: (example: \'eth1\'): ')
    vlan = 97
    addr = '97.99.99.1/24'
    desc = 'TEMP: Automation Test'
    add_subint_subnet(vlan,addr,desc)
    net_connect.disconnect()

if __name__ == '__main__':
    main()
