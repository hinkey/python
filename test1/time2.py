import time
from datetime import datetime

starttime = datetime.now()
while (datetime.now()-starttime).seconds < 1:
    print('ww')
    time.sleep(1)