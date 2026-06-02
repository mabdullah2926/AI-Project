def run(return_data: dict) -> dict:
    reason = return_data.get("reason", "").lower()
    condition = return_data.get("condition", "").lower()

    if "defective" in reason or "broken" in reason or "damaged" in condition:
        return_data["category"] = "defective"
        return_data["priority"] = "high"
    elif "wrong" in reason or "incorrect" in reason:
        return_data["category"] = "wrong_item"
        return_data["priority"] = "medium"
    elif "not needed" in reason or "changed mind" in reason:
        return_data["category"] = "buyer_remorse"
        return_data["priority"] = "low"
    else:
        return_data["category"] = "other"
        return_data["priority"] = "medium"

    return return_data