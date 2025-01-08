```markdown
# TWEGA Data Pipeline Demo

A demonstration of real-time order processing and inventory management system for TWEGA Foods interview preparation. This project simulates handling orders from multiple vendors while tracking inventory and revenue in real-time.

## Project Overview
The system demonstrates the ability to:
- Process multiple vendor orders in real-time
- Track inventory levels for various products
- Monitor revenue and vendor activity
- Generate real-time statistics and summaries

## Features
- Real-time order processing with validation
- Dynamic inventory management
- Revenue tracking and reporting
- Vendor activity monitoring
- Summary statistics every 5 orders

## Technical Details
Built using:
- Python for core processing
- JSON for data handling
- Object-oriented design for scalability
- Real-time data processing pipeline

## Sample Output
```
=== Starting TWEGA Foods Order Processing Demo ===

Current Statistics:
Total Orders: 20
Total Revenue: KES 175,116.23
Active Vendors: 19

Inventory Levels:
tomatoes: 295
potatoes: 299
onions: 632
cabbage: 225
carrots: 357
```

## Project Structure
```
TWEGA_DEMO/
├── src/
│   ├── data_generator.py    # Generates sample order data
│   ├── order_processor.py   # Processes orders and manages inventory
│   └── pipeline.py         # Main pipeline coordinating the process
```

## Running the Demo
```bash
python src/data_generator.py | python src/pipeline.py
```
```
