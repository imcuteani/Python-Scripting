# Configuration Template using pyyaml and Jinja 2 library. 
# You can dynamically construct device configuration by pushing variables structured inside YAML, directly 
# to a reusable jinja2 text template. 

# 1. Pyyaml -> library for network automation to parse and emit the yaml data. Serves as the foundation of 
# managing decoupled inventory files and device configurations. By seperating network logic from files 
# device configurations, it allows to dynamically update infra details without modifying core automation tools. 

import yaml
from jinja2 import Environment, FileSystemLoader

# step1: Read structured yaml data 
with open("variables.yaml", "r") as file:
    config_data = yaml.safe_load(file)


# step 2: Load Jinja2 configuration template 

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.j2")

# Step 3: Render the variables into standard Cisco CLI syntax

rendered_config = template.render(config_data)

# Step 4: output generated deployed text file 

with open(f"{config_data['hostname']}.txt", "w") as out_file:
    out_file.write(rendered_config)

print("Configuration file generated successfully")    
