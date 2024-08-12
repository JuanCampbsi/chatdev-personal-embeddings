import os
import yaml

def initialize():
  with open('config.yaml', 'r') as config_file:
      config = yaml.safe_load(config_file)
  os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']
  os.environ['PINECONE_API_KEY'] = config['PINECONE_API_KEY']