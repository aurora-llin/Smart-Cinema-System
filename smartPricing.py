
tier = {  
    'A': 2.0,  
    'B': 3.0,
    'C': 3.0,
    'D': 4.0,
    'E': 5.0,
    'F': 5.0,
}

def get_seat_price(row_letter):
    row = row_letter.upper()
    return tier.get(row, 0.0)

# ========================================================================
#                    Discount Codes / Promotions 
# ========================================================================

def apply_discount(total, code):
    promo = str(code).upper()
    
    # 1. CELEBRATEBD: 50% off total
    if promo == "CELEBRATED":
        return total * 0.50
        
    # 2. WELCOME25: 25% off total
    elif promo == "WELCOME25":
        return total * 0.25
        
    # 3. STUDENTLIFE: 15% off total
    elif promo == "STUDENTLIFE":
        return total * 0.15

    # If no code matches, just return 0 discount
    return 0.0