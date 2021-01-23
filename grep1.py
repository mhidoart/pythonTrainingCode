import re
lines = "The ghost that says boo haunts the loo"
matches = re.findall(".oo", lines, re.IGNORECASE)
print(matches)
