
# ipython [1]
def configure_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)

# ipython [10]
def configure_intf(intf_name, ip, mask):
    return f'interface {intf_name}\nip address {ip} {mask}'

# ipython [14]
def configure_intf(intf_name, ip, mask):
    return f'interface {intf_name}\nip address {ip} {mask}'

# ipython [16]
def configure_intf(intf_name, ip, mask):
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip

