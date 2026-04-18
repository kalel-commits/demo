# core_pipeline.py

def process_data(data):
    result = []
    for item in data:
        if "value" in item:  # safe validation
            result.append(item["value"] * 2)
    return result