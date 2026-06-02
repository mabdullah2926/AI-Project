def run(return_data: dict) -> dict:
    reason = return_data.get("reason", "").lower()
    condition = return_data.get("condition", "").lower()

    fraud_keywords = ["suspicious", "lost", "stolen", "never received", "scam"]
    is_fraud = any(kw in reason for kw in fraud_keywords)

    return_data["fraud_flag"] = is_fraud
    return_data["fraud_reason"] = "Suspicious keywords detected in reason" if is_fraud else "None"
    return return_data