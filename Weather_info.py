import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"{city}의 현재 날씨: {desc}, 온도: {temp}°C")
    else:
        print("날씨 정보를 가져올 수 없습니다. 도시 이름이나 API 키를 확인하세요.")

if __name__ == "__main__":
    print("날씨 알림 스크립트 시작")
    city = input("도시 이름을 입력하세요 (예: Seoul): ")
    api_key = input("OpenWeather API 키를 입력하세요: ")
    get_weather(city, api_key)
