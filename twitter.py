#Goal is to prompt user of their URL of Twitter profile and etract from that URL, the users name

import re

url= input("URL:").strip()

matches= re.search(r"^https?://(?:www\.)?twitter\.(?:com|org|edu)/([a-z0-9_]+)",url,re.IGNORECASE)

if matches:
    print(f"Username:",matches.group(1))
else:
    print("URL does not meet the syntax")
