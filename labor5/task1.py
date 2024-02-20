import re

def check_ipv4(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        return True
    return False

def get_valid_ipv4(ip):
    if not check_ipv4(ip):
        raise ValueError("Не является IPv4")
    return ip

try:
    ip = get_valid_ipv4(input("Введите IPv4 адресс: \n"))
    print(ip)
except ValueError as e:
    print(e)