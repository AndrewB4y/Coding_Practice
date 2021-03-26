

import os

os.system('export ALGO=1122334455')

algo = os.environ.get('ALGO')

print(algo)