import yaml

# Função para carregar arquivos YAML
def carregar_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)