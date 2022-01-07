import json

confi_path = r"C:\Users\harriet\workspace\HyUSD\hyusd\config.json"

with open(confi_path) as f:
  data = json.load(f)
print(data)