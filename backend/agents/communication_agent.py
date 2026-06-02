def run(return_data: dict) -> dict:
    status = return_data.get("status", "pending")
    customer = return_data.get("customer_name", "Customer")
    order_id = return_data.get("order_id", "N/A")
    refund = return_data.get("refund_amount", 0.0)

    messages = {
        "approved": f"Hi {customer}, your return for order {order_id} has been approved. Refund of ${refund} will be processed in 3-5 business days.",
        "rejected": f"Hi {customer}, unfortunately your return for order {order_id} could not be approved. Please contact support for assistance.",
        "manual_review": f"Hi {customer}, your return for order {order_id} is under manual review. We will update you within 24 hours."
    }

    return_data["customer_message"] = messages.get(status, f"Hi {customer}, your return for order {order_id} is being processed.")
    return return_data