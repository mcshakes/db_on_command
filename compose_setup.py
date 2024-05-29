import yaml
import os

with open('setup_psql_environment.yaml', 'r') as file:
    env_vars = yaml.safe_load(file)

with open('docker-compose.template.yml', 'r') as file:
    template = file.read()

for key, value in env_vars.items():
    template = template.replace(f"${{{key}}}", str(value))

with open('docker-compose.yml', 'w') as file:
    file.write(template)

# os.system('docker-compose up -d')
