!pip install sodapy
!pip install pandas

import pandas as pd
from sodapy import Socrata

client = Socrata("data.nj.gov", None)
results = client.get("45bd-gwii", limit=100000000)
