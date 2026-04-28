# ========================================================================
#                             Smart Pricing 
# ========================================================================

tier_multipliers = {  
    'A': 2.0,  
    'B': 3.0,
    'C': 3.0,
    'D': 4.0,
    'E': 5.0,
    'F': 5.0,
}

def calculate_seat_price(row_index, base_price):
    
    row = str(row_index).upper()
    multiplier = 1.0 
    
    if "A" in row: multiplier = tier_multipliers['A']
    elif "B" in row: multiplier = tier_multipliers['B']
    elif "C" in row: multiplier = tier_multipliers['C']
    elif "D" in row: multiplier = tier_multipliers['D']
    elif "E" in row: multiplier = tier_multipliers['E']
    elif "F" in row: multiplier = tier_multipliers['F']
        
    return base_price * multiplier

# ========================================================================
#                    Discount Codes / Promotions 
# ========================================================================

def apply_discount(total, code):
    promo = str(code).upper()
    
    # 1. CELEBRATEBD: 50% off total
    if promo == "CELEBRATEBD":
        return total * 0.50
        
    # 2. WELCOME25: 25% off total
    elif promo == "WELCOME25":
        return total * 0.75
        
    # 3. STUDENTLIFE: 15% off total
    elif promo == "STUDENTLIFE":
        return total * 0.85

    # If no code matches, just return the original total
    return total