from datetime import *
from dateutil.relativedelta import *

now = datetime.now()

print (now)

now = now + relativedelta(month=1, week= 1, hour=10)

print(now)