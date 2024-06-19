import json

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'

sneakers = json.loads(json_str)

print(type(sneakers))

print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])
print(sneakers)  # {'id': 235, 'brand': 'Nike', 'qty': 84, 'status': {'isForSale': True}}

json_str2 = json.dumps(sneakers)
print(json_str2)

json_str3 = json.dumps(sneakers, indent=1)
print(json_str3)

json_array = '[1,2,3]'
l1 = json.loads(json_array)
print(l1)
