# 소스 코드 README

- 이 소스 코드는 텍스트 데이터를 정제하는 데 사용되는 Python 함수를 포함하고 있습니다. 
- 이 함수는 HTML 태그, 특수 문자 및 중복 기호를 제거하고, 문장의 공백과 대소문자를 정규화합니다.

## 1. 사용 방법

1. `cleansing` 함수를 가져오기 위해 `re` 모듈을 import 합니다:

    ```python
    import re
    ```
2. 텍스트 데이터를 정제하려는 경우, cleansing 함수를 호출합니다. 함수는 다음과 같은 방식으로 사용될 수 있습니다:

    ```
    sentence = "How are you doing?"
    dtx = cleansing(sentence)
    print(dtx)
    ```

3. 위의 예제에서는 cleansing 함수를 사용하여 sentence 변수의 텍스트 데이터를 정제하고, 정제된 결과를 출력합니다.

## 2. 함수 동작
cleansing 함수는 다음과 같은 단계로 텍스트 데이터를 정제합니다:

- HTML 태그를 제거합니다.
- 영문 대소문자, 숫자, 한글, 공백, 물음표, 느낌표, 마침표, 쉼표, 물결표 등 허용된 문자 외의 모든 문자를 제거합니다.
- 중복된 느낌표, 물음표, 물결표, 마침표, 쉼표, 공백을 단일 기호로 대체합니다.
- 연속된 공백을 단일 공백으로 대체합니다.
- 문장을 소문자로 변환합니다.

## 3. 참고사항
- 이 함수는 주어진 텍스트 데이터의 정제를 위해 설계되었습니다.
- 입력으로 받은 텍스트 데이터를 수정하지 않고 반환합니다.