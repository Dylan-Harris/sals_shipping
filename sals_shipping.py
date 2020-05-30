premium = 125.00
def ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.50) + 20.00
  elif weight >= 2 and weight <=6:
    return (weight * 3.00) + 20.00
  elif weight >= 6 and weight <= 10:
    return (weight * 4.00) + 20.00
  else: 
    (weight * 4.75) + 20.00


def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.50
  elif weight >= 2 and weight <= 6:
    return weight * 9.00
  elif weight >= 6 and weight <= 10:
    return weight * 12.00
  else:
    return weight * 14.25
  
print(ground_shipping(8.4))
print(drone_shipping(1.5))

def cheapest_method(weight):
  x = ground_shipping(weight)
  y = drone_shipping(weight)
  if x < y and x < premium:
    return f"Ground shipping is the cheapest. It will cost you about ${x}"
  elif y < x and y < premium:
    return f"Drone shipping is the cheapest. It will cost you about ${y}"
  else:
    return "Premium shipping is the cheapest. It will cost you $125.00"


print(cheapest_method(4.8))
print(cheapest_method(41.5))