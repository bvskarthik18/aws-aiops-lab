import sys
from pathlib import Path

# Add the inventory-service directory so we can import it locally.

inventory_path = Path(__file__).parent.parent / "inventory-service"
sys.path.append(str(inventory_path))

from inventory import lambda_handler as inventory_handler

def lambda_handler(event, context):
    # Call the inventory service to get the inventory status for the product
    inventory = inventory_handler({}, None)

    return {
        "order_id": "123",
        "product": inventory["product"],
        "quantity": 1,
        "inventory_status": inventory["inventory_status"]
    }
