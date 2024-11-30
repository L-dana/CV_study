import requests
import json 
from pprint import pprint

# 요청 헤더
headers = {
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
    "x-rpc-device_fp": "38d7f41658d91",
    "x-rpc-device_id": "d7700efa-583f-4878-bb9c-31660e1b1e06",
    "x-rpc-env": "default",
    "x-rpc-lang": "ko-kr", # 변경 x
    "x-rpc-language": "ko-kr", # 변경 x
    "x-rpc-page": "v5.2.0-ys_#/ys/role/all",
    "x-rpc-platform": "5" # 4 = 모바일, 5 = PC
}

# 요청에 필요한 쿠키 (민감 정보 포함)
cookies = {
    "account_mid_v2": "1f2l59umhb_hy",
    "account_id_v2": "82283321",
    "cookie_token_v2": "v2_CAQSDGM5b3FhcTNzM2d1OBokNDM3YzQ1MmEtMTYxOS00NzUyLWJmYzMtZDAyNTgyOTg4YmM3IO3dqroGKKTYjbgHMLmWnidCC2Jic19vdmVyc2Vh.7a5KZwAAAAAB.MEUCIQDA98SHK-pO1U9n21illzSwu59-q2-o6CoKC9wKX18ASwIgCdvCIzzNZo1CedKOSQ7c1FQqSMaQCxB4OSCaTYW1QIs",
    "ltoken_v2": "v2_CAISDGM5b3FhcTNzM2d1OBokNDM3YzQ1MmEtMTYxOS00NzUyLWJmYzMtZDAyNTgyOTg4YmM3IO3dqroGKIfwrfUCMLmWnidCC2Jic19vdmVyc2Vh.7a5KZwAAAAAB.MEYCIQDyCw54cpONjTCnkijR_N9jHawcv0BES63jwW9Xy23yngIhANJoiEWbOt16rH0-tJMkSm2THSjgkwje_lc-KmdbZpfY",
    "ltuid_v2": "82283321"
}

# 요청 데이터
payload = {
    "role_id": "826744262",  # UID
    "server": "os_asia",     # 서버 정보
    "sort_type": 1           # 정렬 유형
}

# POST 요청
response = requests.post(
    'https://sg-public-api.hoyolab.com/event/game_record/genshin/api/character/list',
    headers=headers,
    cookies=cookies,
    json=payload
)

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