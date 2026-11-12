import sys
import json
import time

from pathlib import Path

# Add the inventory-service directory so we can import it locally.

inventory_path = Path(__file__).parent.parent / "inventory-service"
sys.path.append(str(inventory_path))

from inventory import lambda_handler as inventory_handler

def lambda_handler(event, context):

    start_time = time.perf_counter()
    
    # Call the inventory service to get the inventory status for the product
    inventory = inventory_handler({}, None)

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

    print(json.dumps({
        "service": "orders-service",
        "event": "order_lookup",
        "order_id": "123",
        "product": inventory["product"],
        "inventory_status": inventory["inventory_status"],
        "duration_ms": duration_ms
    }))

    return {
        "order_id": "123",
        "product": inventory["product"],
        "quantity": 1,
        "inventory_status": inventory["inventory_status"]
    }
