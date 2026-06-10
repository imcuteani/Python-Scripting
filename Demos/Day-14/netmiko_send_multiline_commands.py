from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}
with ConnectHandler(**device) as conn:
    target_ip ="8.8.8.8"
    count = "30"
    cmd_list = [
        "ping",
        "\n",
        target_ip,
        count,
        "\n",
        "\n",
        "\n",
        "\n"
    ]
    output = conn.send_multiline_timing(cmd_list)
    print(output)