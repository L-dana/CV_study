import requests
import json 
from pprint import pprint

class RequestBuilder:
    def __init__(self, x_rpc_device_fp = "38d7f41658d91", x_rpc_device_id = "d7700efa-583f-4878-bb9c-31660e1b1e06"):
        self.HEADERS = {
            "Accept": "application/json, text/plain, */*", # 요청/응답 인코딩 방식
            "Accept-Encoding": "gzip, deflate, br, zstd", # 요청/응답 인코딩 방식
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8", # 요청/응답 인코딩 방식
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36", # 접속자 정보
            "Origin": "https://act.hoyolab.com",
            "Referer": "https://act.hoyolab.com/",
            "x-rpc-app_version": "1.5.0", # 서버 맞춰서(호요버스에서 바꾸지 않으면 변경 x)
            "x-rpc-client_type": "5",
            "x-rpc-device_fp": "",
            "x-rpc-device_id": "",
            "x-rpc-env": "default",
            "x-rpc-lang": "ko-kr", # 변경 x
            "x-rpc-language": "ko-kr", # 변경 x
            "x-rpc-page": "v5.2.0-ys_#/ys/role/all",
            "x-rpc-platform": "5" # 4 = 모바일, 5 = PC
        }

        if self.HEADERS["x-rpc-device_fp"] == "":
            self.HEADERS["x-rpc-device_fp"] = x_rpc_device_fp
        if self.HEADERS["x-rpc-device_id"] == "":
            self.HEADERS["x-rpc-device_id"] = x_rpc_device_id

        self.COOKIES= {
            "account_mid_v2": "",
            "account_id_v2": "",
            "cookie_token_v2": "",
            "ltoken_v2": "",
            "ltuid_v2": ""
        }
        self.PAYLOAD = None

    def set_cookie_field(self, key, value):
        self.COOKIES[key] = value
    
    def get_character_list(self):
        if self.PAYLOAD == None:
            raise Exception("요청이 올바르지 않습니다.")
        
        response = requests.post(
            'https://sg-public-api.hoyolab.com/event/game_record/genshin/api/character/list',
            headers= self.HEADERS,
            cookies=self.COOKIES,
            json=self.PAYLOAD
        )
        return response


client = RequestBuilder()
response = client.get_character_list()

# 응답 상태 코드와 JSON 데이터 출력
print("HTTP 상태 코드:", response.status_code)

# 응답 본문(JSON 데이터)
try:
    # JSON 데이터를 딕셔너리로 변환
    data = response.json()
    print("\n응답 데이터:")
    pprint(data, width=80)  # 보기 좋게 포맷팅된 JSON 출력
except json.JSONDecodeError:
    print("JSON 디코딩 오류 발생. 응답 내용:")
    print(response.text)