import os
import shutil
from datetime import datetime

def create_directory_structure():
    # Create base dist directory if it doesn't exist
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    
    os.makedirs('dist')
    
    # Create child service directories
    os.makedirs('dist/child-service')
    os.makedirs('dist/child-bis-service')
    
    # Generate service files
    generate_child_service_file()
    generate_child_bis_service_file()
    
    print("✅ Generated service files in dist directory")

def generate_child_service_file():
    with open('dist/child-service/child_service_v1.py', 'w') as f:
        f.write(f"""# Child Service V1
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

from dataclasses import dataclass

@dataclass
class ChildServiceV1:
    service_name: str
    is_active: bool = True
    env: str = "dev1"
""")

def generate_child_bis_service_file():
    with open('dist/child-bis-service/child_bis_service_v1.py', 'w') as f:
        f.write(f"""# Child Bis Service V1
# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

from dataclasses import dataclass

@dataclass
class ChildBisServiceV1:
    service_name: str
    is_active: bool = True
    env: str = "dev2"
""")

if __name__ == "__main__":
    create_directory_structure()
