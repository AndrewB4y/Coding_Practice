import snowflake.connector
import json
with open(“cred.json”,”r”) as f:
 cred = json.load(f)
# create “cred.json” JSON file and write or you can use Json’s dump to create JSON:
# {
# “userid”:”userid”,
# “password”:”xxxxx”,
# “account”:”px00000.ap-southeast-2"
# }

conn = snowflake.connector.connect(
 user=cred["userid"],
 password=cred["password"],
 account=cred["account"],
 session_parameters={
 "QUERY_TAG": "EndOfMonthFinance",
 }
)
print("success in connecting", conn)