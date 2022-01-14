import time
import telnetlib


class CiscoTelnet:
    """Telnet connection to Cisco"""

    def __init__(self, ip, username, password, enable, disable_paging=True):
        """Instance creation"""
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self.telnet.write(username.encode("utf-8") + b"\n")
        self.telnet.read_until(b"Password:")
        self.telnet.write(password.encode("utf-8") + b"\n")
        self.telnet.write(b"enable\n")
        self.telnet.read_until(b"Password:")
        self.telnet.write(enable.encode("utf-8") + b"\n")
        if disable_paging:
            self.telnet.write(b"terminal length 0\n")
        time.sleep(1)
        self.telnet.read_very_eager()

    def send_show_command(self, command):
        """Sending show command"""
        self.telnet.write(command.encode("utf-8") + b"\n")
        time.sleep(2)
        return self.telnet.read_very_eager().decode("utf-8")


if __name__ == "__main__":
    r1 = CiscoTelnet("192.168.100.1", "cisco", "cisco", "cisco")
    print(r1.send_show_command("sh ip int br"))
