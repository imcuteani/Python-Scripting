# nornir hello script
from nornir import InitNornir

def say_hello(task):
    print("Hello, Nornir")

nr = InitNornir(config_file="C:/Users/Administrator/Downloads/Python-Scripting/Demos/Day-14/nornir-labs/config.yaml")
nr.run(task=say_hello)