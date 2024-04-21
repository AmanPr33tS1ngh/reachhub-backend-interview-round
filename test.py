import requests
import json
import random
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

INGESTION_URL = "http://localhost:8000/api/"
QUERY_URL = "http://localhost:8000/api/"
THREAD_COUNT = 50
LOG_ENTRIES_PER_THREAD = 100
LEVELS = ["INFO", "ERROR"]

def generate_log():
    timestamp = datetime.datetime.now().isoformat()
    level = random.choice(LEVELS)
    message = f"Sample log message with level {level}"
    user_id = random.randint(1, 100)
    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
        "userId": str(user_id)
    }

def post_log():
    log_entry = generate_log()
    response = requests.post(INGESTION_URL, json=log_entry)
    return response.status_code

def query_logs():
    level = random.choice(LEVELS)
    user_id = random.randint(1, 100)
    params = {
        "level": level,
        "userId": user_id
    }
    response = requests.get(QUERY_URL, params=params)
    return response.status_code, response.json()

def main():
    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        futures = [executor.submit(post_log) for _ in range(LOG_ENTRIES_PER_THREAD * THREAD_COUNT)]
        futures += [executor.submit(query_logs) for _ in range(LOG_ENTRIES_PER_THREAD * THREAD_COUNT // 10)]
        for future in as_completed(futures):
            result = future.result()
            print("Task completed with result:", result)

if __name__ == "__main__":
    main()