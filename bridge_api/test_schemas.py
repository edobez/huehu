from jsonschema import validate
from pathlib import Path
import yaml, json

api_specs_file = Path('./bridge_api_specs.yaml')
api_specs = yaml.safe_load(api_specs_file.read_text()) 








