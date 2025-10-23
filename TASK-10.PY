facts = [
    "john_is_cold.",
    "raining.",
    "john_Forgot_His_Raincoat.",
    "fred_lost_his_car_keys.",
    "peter_footballer."
]

def verify_fact(fact):
    fact = fact.rstrip(".")
    if fact in ["john_Forgot_His_Raincoat", "raining", "foggy"]:
        return True
    return False

for fact in facts:
    print(f"{fact} - {'Yes' if verify_fact(fact) else 'No'}")

