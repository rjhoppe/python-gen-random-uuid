import uuid
import pandas as pd

test = uuid.uuid4()

for _ in range(10000):
    if uuid.uuid4() == test:
        print('Conflict')

# Mathematically it is possible to get a conflict
# But it is highly unlikely