def fuel_price(litres, price_per_litre):
    if litres < 2:
        return litres*price_per_litre
    elif 2 <= litres < 4:
        return litres*(price_per_litre*100-10)/100
    elif 6 <= litres < 8:
        return litres*(price_per_litre*100-15)/100
    elif 8 <= litres < 10:
        return litres*(price_per_litre*100-20)/100

    else:
        return litres*(price_per_litre*100-25)/100
