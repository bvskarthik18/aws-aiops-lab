import json
import time 

def lambda_handler(event, context):
    start_time = time.perf_counter()
    time.sleep(2)
    inventory = {
        "product": "laptop",
        "inventory_status": "available",
        "quantity_available": 10
    }

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

    print(json.dumps({
        "service": "inventory-service",
        "event": "inventory_check",
        "product": inventory["product"],
        "inventory_status": inventory["inventory_status"],
        "quantity_available": inventory["quantity_available"],
        "duration_ms": duration_ms
    }))

    return inventory