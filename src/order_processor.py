# src/order_processor.py
import json
from datetime import datetime

class OrderProcessor:
    def __init__(self):
        self.processed_orders = []
        self.inventory = {
            'tomatoes': 1000,
            'potatoes': 1000,
            'onions': 1000,
            'cabbage': 1000,
            'carrots': 1000
        }
        self.orders_by_vendor = {}
        
    def process_order(self, order_data):
        """Process incoming order and update metrics"""
        if self.validate_order(order_data):
            # Update inventory
            self.update_inventory(order_data)
            
            # Track vendor orders
            vendor_id = order_data['vendor_id']
            if vendor_id not in self.orders_by_vendor:
                self.orders_by_vendor[vendor_id] = []
            self.orders_by_vendor[vendor_id].append(order_data)
            
            # Store processed order
            processed_order = {
                'order_id': order_data['order_id'],
                'vendor_id': order_data['vendor_id'],
                'processed_at': datetime.now().isoformat(),
                'amount': round(order_data['amount'], 2)
            }
            self.processed_orders.append(processed_order)
            
            return processed_order
        return False
    
    def validate_order(self, order_data):
        """Validate order data"""
        required_fields = ['order_id', 'vendor_id', 'items', 'amount']
        return all(field in order_data for field in required_fields)
    
    def update_inventory(self, order_data):
        """Update inventory levels"""
        for item in order_data['items']:
            product = item['product']
            quantity = item['quantity']
            if product in self.inventory:
                self.inventory[product] -= quantity
    
    def get_summary(self):
        """Get processing summary"""
        return {
            'total_orders': len(self.processed_orders),
            'total_revenue': round(sum(order['amount'] for order in self.processed_orders), 2),
            'active_vendors': len(self.orders_by_vendor),
            'current_inventory': self.inventory
        }