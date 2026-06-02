from __future__ import annotations


def run(return_data: dict) -> dict:
    records = return_data.get("all_records", [])
    total = len(records)
    approved = sum(1 for r in records if r.get("status") == "approved")
    rejected = sum(1 for r in records if r.get("status") == "rejected")

    return_data["analytics"] = {
        "total": total,
        "approved": approved,
        "rejected": rejected,
        "manual_review": total - approved - rejected,
        "approval_rate": round((approved / total * 100), 2) if total else 0,
    }
    return return_data


def get_summary(db) -> dict:
    records = db.query_return_records() if hasattr(db, "query_return_records") else []
    return run({"all_records": records})["analytics"]

