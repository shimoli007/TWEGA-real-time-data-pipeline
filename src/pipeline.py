# src/demo_pipeline.py
import sys
import json
from order_processor import OrderProcessor

def run_demo():
    processor = OrderProcessor()
    print("\n=== Starting Twiga Foods Order Processing Demo ===\n")
    
    orders_processed = 0
    
    for line in sys.stdin:
        try:
            order = json.loads(line)
            result = processor.process_order(order)
            
            if result:
                orders_processed += 1
                print(f"\rProcessed orders: {orders_processed}", end="")
                
                # Show summary every 5 orders
                if orders_processed % 5 == 0:
                    summary = processor.get_summary()
                    print("\n\nCurrent Statistics:")
                    print(f"Total Orders: {summary['total_orders']}")
                    print(f"Total Revenue: KES {summary['total_revenue']:,.2f}")
                    print(f"Active Vendors: {summary['active_vendors']}")
                    print("\nInventory Levels:")
                    for product, quantity in summary['current_inventory'].items():
                        print(f"{product}: {quantity}")
                    print("\n" + "="*50 + "\n")
                
        except json.JSONDecodeError:
            print("Invalid JSON data")
        except Exception as e:
            print(f"Error processing order: {str(e)}")

if __name__ == "__main__":
    run_demo()