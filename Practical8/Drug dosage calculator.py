
def calculator(weight, strength):
    if weight < 10 or weight > 100:
        return "Weight out of range (10-100 kg)"
    
    if strength not in [120, 250]:
        return "Error input strength. Please use 120 or 250."
    kg = 15
    total = kg * weight
    volume = (total / strength) * 5
    return volume
weight_input = input("enter the weight")
weight = float(weight_input)  
strength_input = input("enter the strength")
strength = float(strength_input) 
print(calculator(weight, strength)) 
#example:
print("example: ")
weight1 = 50
strength1 = 120
print(calculator(weight1, strength1)) 