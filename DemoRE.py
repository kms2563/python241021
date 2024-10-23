#demoRE.py

import re
result = re.search("[0-9]*th","  35th")
print(result)
print(result.group())
 
# result = re.match("[0-9]*th","  35th")
# print(result)
# print(result.group())

#demoRE.py

import re
result = re.search("ap", "this is apple")
print(result.group())
 
result = re.search("\d{4}", "올해는 2024년")
print(result.group())
 
result = re.search("\d{5}", " 우리동네 우편번호는 1234 가 아니라 12238")
print(result.group())






def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = re.search(pattern, email)
    if result:
        return f"{email}은(는) 유효한 이메일 주소입니다."
    else:
        return f"{email}은(는) 유효하지 않은 이메일 주소입니다."

# 테스트 샘플
test_emails = [
    "user@example.com",
    "user.name@example.co.kr",
    "user+tag@example.com",
    "123@example.com",
    "user@subdomain.example.com",
    "user@example",
    "user@.com",
    "@example.com",
    "user@example.",
    "user name@example.com"
]

# 테스트 실행
for email in test_emails:
    print(check_email(email))



