from classes import Operations
from utils import unpacking_json

# unpacking_json()
unpacking_json = unpacking_json()
print(unpacking_json)
for a in unpacking_json:
    print(f"{a.get_data()[-2:]}.{a.get_data()[4:-2]}.{a.get_data()[:4]} {a.get_description} {a.get_from_} -> {a.get_to_} {a.get_amount} {a.get_currency}")
    print(a.get_data())
