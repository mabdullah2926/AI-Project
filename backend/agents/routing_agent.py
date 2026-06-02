def run(return_data: dict) -> dict:
    category = return_data.get("category", "other")
    priority = return_data.get("priority", "medium")
    fraud = return_data.get("fraud_flag", False)

    if fraud:
        return_data["assigned_team"] = "fraud_investigation"
    elif priority == "high" or category == "defective":
        return_data["assigned_team"] = "quality_assurance"
    elif category == "wrong_item":
        return_data["assigned_team"] = "fulfillment"
    else:
        return_data["assigned_team"] = "general_support"

    return return_data