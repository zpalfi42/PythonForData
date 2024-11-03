"""_summary_
1. Import the `datetime` class from the `datetime` module to work with date and time.

2. Use `datetime.today()` to get the current date and time, storing it in the variable `today`.

3. Print the number of seconds since January 1, 1970 (Unix epoch) by calling `today.timestamp()`.
   - This is displayed in two formats:
     a. Standard notation with commas (`{today.timestamp():,f}`)
     b. Scientific notation (`{today.timestamp():.2e}`)

4. Use `strftime` to format the current date in "Month Day Year" format (e.g., "Nov 03 2024") and print it.
"""

from datetime import datetime

today = datetime.today()

print(f"Seconds since January 1, 1970: {today.timestamp():,f} or "
      f"{today.timestamp():.2e} in scientific notation")

print(today.strftime("%b %d %Y"))
