import os
import requests
from bs4 import BeautifulSoup

def fetch_youtube_captions(video_id):
    url = f"https://www.youtube.com/api/timedtext?lang=en&v={video_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def save_captions(video_id, captions, output_dir="data/raw"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(os.path.join(output_dir, f"{video_id}.txt"), "w", encoding="utf-8") as file:
        file.write(captions)

def main(video_ids):
    for video_id in video_ids:
        captions = fetch_youtube_captions(video_id)
        if captions:
            save_captions(video_id, captions)
        else:
            print(f"Failed to fetch captions for video: {video_id}")

if __name__ == "__main__":
    # 예제 비디오 ID 리스트
    video_ids = ["KwTHok_B-5w", "eVTXPUF4Oz4"]
    main(video_ids)
