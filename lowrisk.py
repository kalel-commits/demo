# lowrisk.py  (or core_pipeline.py)

def process_data(data):
    result = []
    for item in data:
        # ✅ proper validation (safe)
        if isinstance(item, dict) and "value" in item:
            result.append(item["value"] * 2)
    return result


def helper_sum(a, b):
    return a + b