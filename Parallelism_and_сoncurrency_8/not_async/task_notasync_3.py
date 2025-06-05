import requests
import time

def limited_fetch(url: str) -> None:
    response = requests.get(url)
    text = response.text
    print(f"[{time.strftime('%X')}] {url} - {response.status_code} - {len(text)} bytes")

def main():
    time_start = time.perf_counter()
    url = "http://google.com"
    requests_count = 10
    delay = 0.1  # 0.1 секунды между запросами = 10 запросов в секунду
    for _ in range(requests_count):
        limited_fetch(url)
        time.sleep(delay)  # ограничиваем скорость запросов
    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")



if __name__ == "__main__":
    main()