{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "authorship_tag": "ABX9TyOX9uqi0F6ZPIHXHLz+jxkF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/KimDeukGap/opensource/blob/main/Weather_info.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p5xDRlbm8IfC",
        "outputId": "0baf7f7c-e885-42dc-f97d-1c133cb31172"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "날씨 알림 스크립트 시작\n"
          ]
        }
      ],
      "source": [
        "import requests\n",
        "\n",
        "def get_weather(city, api_key):\n",
        "    url = f\"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=kr&units=metric\"\n",
        "    response = requests.get(url)\n",
        "    if response.status_code == 200:\n",
        "        data = response.json()\n",
        "        temp = data['main']['temp']\n",
        "        desc = data['weather'][0]['description']\n",
        "        print(f\"{city}의 현재 날씨: {desc}, 온도: {temp}°C\")\n",
        "    else:\n",
        "        print(\"날씨 정보를 가져올 수 없습니다. 도시 이름이나 API 키를 확인하세요.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"날씨 알림 스크립트 시작\")\n",
        "    city = input(\"도시 이름을 입력하세요 (예: Seoul): \")\n",
        "    api_key = input(\"OpenWeather API 키를 입력하세요: \")\n",
        "    get_weather(city, api_key)"
      ]
    }
  ]
}