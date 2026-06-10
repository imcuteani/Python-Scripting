from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.80.129",
    "port": "5004",
    "username": "admin",
    "password": "cisco123",
}
with ConnectHandler(**device) as conn:
    data = ""
    commands = [
        "ping", 
        "\n", 
        "8.8.8.8", 
        "\n", 
        "\n", 
        "\n", 
        "\n", 
        "\n"
    ]
    for cmd in commands:
        data += conn.send_command_timing(
            cmd, 
            strip_command=False,
            strip_prompt=False
        )
    print(data) 

    bgp_data = conn.send_command_timing(
        "show ip bgp",
        read_timeout=0
    )
    print(bgp_data)