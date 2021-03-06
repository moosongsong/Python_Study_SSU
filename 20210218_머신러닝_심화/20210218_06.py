# \d : 숫자 1개
# \D : 숫자가 아닌 문자 1개
# \s : 공백, 탭 1개
# \S : 공백이 아닌 문자 1개
# \w : 영어문자 한개
# \W : 한글이나 중국어 1개
# https://regexone.com/

import re  # 정규표현식 라이브러리
tel = '1234567890'
result = re.match(pattern='\d\d\d\d\d\d\d\d\d\d', string=tel)
print(result)

tel = '123 456 7890'
# result = re.match(pattern='\d\d\d\s\d\d\d\s\d\d\d\d', string=tel)
# result = re.match(pattern='\d\d\d \d\d\d \d\d\d\d', string=tel)
result = re.match(pattern='\d{3} \d{3} \d{4}', string=tel)
print(result)

tel = '(123) 456 7890'
result = re.match(pattern='\(\d{3}\) \d{3} \d{4}', string=tel)
print(result)

tel = '+1 (123) 456 7890'
result = re.match(pattern='\+\d \(\d{3}\) \d{3} \d{4}', string=tel)
print(result)

