# src/data_generator.py
import json
import random
from datetime import datetime
import time

def generate_order():
    products = ['tomatoes', 'potatoes', 'onions', 'cabbage', 'carrots']
    vendors = [f'VENDOR_{i}' for i in range(1, 101)]  # Changed to 100 vendors
    
    order = {
        'order_id': f'ORD_{int(time.time())}_{random.randint(1000, 9999)}',
        'vendor_id': random.choice(vendors),
        'timestamp': datetime.now().isoformat(),
        'items': [
            {
                'product': random.choice(products),
                'quantity': random.randint(1, 100),
                'unit_price': random.uniform(10, 100)
            } for _ in range(random.randint(1, 5))
        ],
        'amount': 0
    }
    
    order['amount'] = sum(item['quantity'] * item['unit_price'] 
                         for item in order['items'])
    
    return order

if __name__ == "__main__":
    # Generate only 20 sample orders instead of infinite loop
    for _ in range(20):  # This will generate just 20 orders
        order = generate_order()
        print(json.dumps(order))
        time.sleep(0.5)  # Reduced wait time to 0.5 seconds