import time
from datetime import datetime

today = datetime.today()

print(f"Seconds since January 1, 1970: {today.timestamp():,f} or {today.timestamp():.2e} in scientific notation")
# print(today.timetuple())

print(today.strftime("%b %d %Y"))