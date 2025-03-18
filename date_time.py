import datetime
import pytz
import time
import calendar
from dateutil import parser

# Parse a string into a datetime object
date_string = "2025-03-17 14:30:00"
parsed_date = parser.parse(date_string)
print("Parsed date using dateutil:", parsed_date)


# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get current date only
current_date = datetime.date.today()
print("Current date:", current_date)

# Get current time only
current_time = datetime.datetime.now().time()
print("Current time:", current_time)

# Creating a specific datetime object
dt = datetime.datetime(2025, 3, 17, 14, 30, 0)
print("Specific date and time:", dt)

# Format datetime to a string
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_time)

# Parse string to datetime
date_string = "2025-03-17 14:30:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_date)

# Date arithmetic with timedelta
future_date = now + datetime.timedelta(days=10)
print("Date 10 days from now:", future_date)

###################################################################################################

# Get UTC time
utc_time = datetime.datetime.now(pytz.utc)
print("UTC time:", utc_time)

# Convert to US Eastern time
eastern_time = utc_time.astimezone(pytz.timezone('US/Eastern'))
print("US Eastern time:", eastern_time)

# Convert to another timezone (e.g., 'Europe/London')
london_time = utc_time.astimezone(pytz.timezone('Europe/London'))
print("London time:", london_time)

###################################################################################################

# Parse a string into a datetime object
date_string = "2025-03-17 14:30:00"
parsed_date = parser.parse(date_string)
print("Parsed date using dateutil:", parsed_date)

###################################################################################################

# Get the current time in seconds since the Unix epoch
timestamp = time.time()
print("Current timestamp:", timestamp)

# Convert the timestamp back to a structured time
structured_time = time.localtime(timestamp)
print("Structured time:", structured_time)

# Format the time in a readable way
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", structured_time)
print("Formatted time:", formatted_time)

###################################################################################################

# Get the weekday of a specific date (0 = Monday, 6 = Sunday)
weekday = calendar.weekday(2025, 3, 17)
print("Weekday:", weekday)  # 0=Monday, 1=Tuesday, ..., 6=Sunday

# Get the name of the month
month_name = calendar.month_name[3]  # March (index 3)
print("Month name:", month_name)

# Check if a year is a leap year
is_leap = calendar.isleap(2025)
print("Is a leap year =", is_leap)