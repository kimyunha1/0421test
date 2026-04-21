import requests # 오류 포인트 1

# 1. 접속할 웹사이트 주소
url = "https://www.google.com"

# 2. 웹사이트에 정보 요청하기
response = requests.get(url)

# 3. 결과 출력
if response.status_code == 200:
    print("구글 접속에 성공했습니다!") # 오류 포인트 2
    print(f"응답 내용 중 일부: {response.text[:100]}")
else:
    print("접속 실패!")

# 4. 잘못된 데이터 접근
print(f"헤더 정보 확인: {response.headers}") # 오류 포인트 3