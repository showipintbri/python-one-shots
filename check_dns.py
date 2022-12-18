import dns.resolver
import sys

def dns_lookup(dns_servers: list,domain_names: list):
    for dns_server in dns_servers:
        if dns_server == '': continue
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [dns_server]
        for fqdn in domain_names:
            if fqdn == '': continue
            answer = resolver.resolve(fqdn, "A")
            print('Answers from DNS Server {}'.format(resolver.nameservers))
            for rr in answer:
                print('{} is @: {}'.format(fqdn, rr))

def read_domain_list(domain_list):
    try:
        with open(domain_list, 'rt') as domains:
            y = domains.read().splitlines()
    except:
        print('Something went wrong opening the file: {}'.format(domain_list))
        sys.exit()
    return  y

def read_dns_list(dns_server_list):
    try:
        with open(dns_server_list, 'rt') as dcs:
            x = dcs.read().splitlines()
    except:
        print('Something went wrong opening the file: {}'.format(dns_server_list))
        sys.exit()
            
    return x
 

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: '+str(sys.argv[0])+' [dns_servers.list] [domain_names.list]\n\n* dns_servers.list * - List of DNS servers. *1 per line*.\n* domain_names.list * - List of FQDN\'s you\'d like to query for.')
        sys.exit()
    else:
        dns_lookup(read_dns_list(sys.argv[1]),read_domain_list(sys.argv[2]))

