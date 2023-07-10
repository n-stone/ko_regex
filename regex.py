import re

def cleansing(text):
    pattern = '<.*?>'
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^A-Za-z0-9가-힣 ! ? ~ . , \s]'
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '\!{2,}' 
    text = re.sub(pattern=pattern, repl='!', string=text)
    pattern = '\?{2,}' 
    text = re.sub(pattern=pattern, repl='?', string=text)
    pattern = '\~{2,}' 
    text = re.sub(pattern=pattern, repl='~', string=text)
    pattern = '\.{2,}'
    text = re.sub(pattern=pattern, repl='.', string=text)
    pattern = '\,{2,}'
    text = re.sub(pattern=pattern, repl=',', string=text)
    pattern = '\s{2,}'
    text = re.sub(pattern=pattern, repl=' ', string=text)
    text = text.lower()
    return text

sentence = "<span class=>Hello  world!!!!!!43434!!!!!!!ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ!!!!!!!!!!!!! ''😀 How are you    today~???? ------12-43=5=6=75=8=76898=6=467!@#$%$^%^&%&^*^&*^%^&*#====[]=()=;:=<=>=?/------😊, 안녕하세요~~~~~~~~~,,,"",,, 우리는,,,,, 오늘도 열심히 일을 합니다.....</span>44444422ㅇㅇㅇㅇㅇ"
# sentence = '<span class=>파이썬으로 파일을 읽어서 특정 부분 찾기</span>'
dtx = cleansing(sentence)
print(dtx)