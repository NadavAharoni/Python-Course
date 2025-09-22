import time
import datetime
from datetime import datetime, timezone

# Get the current local date and time
current_datetime1 = datetime.now(timezone.utc)
# Print the result
# time.sleep(1e-6)
current_datetime2 = datetime.now(timezone.utc)
print(current_datetime1)
print(current_datetime2)

delta = current_datetime2 - current_datetime1
print(type(delta))
print(delta)

