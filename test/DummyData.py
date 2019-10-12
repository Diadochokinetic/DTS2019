

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from datetime import datetime

def timeGenerator(x=1):
    return datetime.utcfromtimestamp(datetime.timestamp(datetime(2019, 10, 12, 13, 25, 5)) + x).strftime('%Y-%m-%d %H:%M:%S')

df = pd.DataFrame({})

size = 20

df['timestamp'] = pd.Series([timeGenerator(x) for x in range(size)])
print(df['timestamp'])
