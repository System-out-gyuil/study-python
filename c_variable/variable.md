# 변수 - 저장공간

    변수는 값을 담는 저장공간이다.
    x = 10, x라는 이름의 저장공간이 RAM(메모리)에 만들어지고 10이라는 값이 들어간다.

## 자료형(Type) - 저장공간의 종류

    동적 바인딩: 값에 따라 자료형이 정해진다.

    자료형(type)       값
    정수(int)       0, 10, -187, ...
    실수(float)       0.0, 10.58, -77.568, ...
    문자열(str)       '0', "0.0", """한동석""", '''Python''', ...
    리스트(list)       [1, 2, 3], [0], [3,], ...
    튜플(tuple)       (1, 2), (), 1, 2, 3, (1,), ...
    딕셔너리(dict)   {key:value,}, ...
    집합(set)       {1, 2, 3}, {1}, ...
    불린(bool)       True, False

### 동적 바인딩(Dynamic Binding)

    동적 바인딩은 실행 시간(runtime)에 메소드나 함수와 같은 호출 대상이 
    실제로 어떤 코드나 메모리 위치에 바인드되는지 결정된다
    주로 객체지향 언어에서 사용되며, 다형성과 연관이 있다. 
    예를 들어, 가상 함수나 추상 메소드를 통해 동적으로 
    어떤 메소드가 호출될지를 실행 시간에 결정할 수 있다.

### 동적 타이핑(Dynamic Typing):

    동적 타이핑은 변수의 데이터 타입이 실행 시간에 결정되는 것을 의미한다.
    정적 타이핑(Static Typing)과 대조되며, 
    변수를 선언할 때 데이터 타입을 명시적으로 지정하는 대신, 
    실행 중에 변수가 어떤 타입의 데이터를 가질지 결정된다. 
    이는 개발자가 더 유연하게 코드를 작성할 수 있게 해준다

### 변수명 주의사항

    - 문자로 시작해야 한다.
    - 특수문자는 사용할 수 없다. 단, _는 허용한다.
    - 소문자로 시작한다.
    - 공백을 사용할 수 없다.
    - 되도록 한글은 사용하지 않는다.
    - 명사로 사용한다.
    - 뜻이 있는 단어를 사용한다.
        - a, b, c, d, e, ... (X)
        - data, number, age, name, ...(O)

### 변수의 선언과 사용

    - 선언: 대입 연산자가 있다면 선언이다, 값으로 봐서는 안된다!
    - 사용: 대입 연산자가 없다면 사용이다, 반드시 값으로 봐야한다

### 표기법

    파스칼 표기법(클래스명, 오류명) 
    - 대문자로 시작, 이어지는 문자 대문자로 시작
    - PascalCase
    카멜 표기법(Java 등에서 사용)
    - 소문자로 시작하고 이어지는 단어의 시작은 대문자
    - camelCase
    스네이크 표기법
    - 단어 사이에 언더스코어(_)를 작성한다
    - snake_case
    케밥 표기법(HTML, CSS, URL 등에서 사용)
    - kebab-case

### 서식문자 - 따옴표 안에서 변수 또는 값을 사용해야 할 때 작성한다.

    반드시 따옴표 안에서 작성한다

    ----------------------------------
    서식문자   설명
    ----------------------------------
    %d           10진수 정수 표현
    %f           실수 표현
    %s           문자열 표현
    ----------------------------------

### 변수를 사용하는 이유

    - 반복되는 값을 쉽게 관리하고자 할 때
    - 값에 의미 부여를 할 때 (자료구조)

### 알고리즘과 자료구조

    - 알고리즘이란
        - 문제가 발생했을 때 해결할 수 있는 절차
        - 예) 3과 1을 더해서 결과를 출력하시오
            1. 두 정수를 담을 변수 선언
            2. 두 정수의 합을 담을 변수 선언
            3. 형식에 맞게 작성한 문자열 값을 담을 변수 선언
            4. 형식을 출력

    - 자료구조란
        - 의미없는 값은 하나의 정보로 변호ㅘㄴ하고 이는 저장공간의 종류를 의미한다.
        - 예) 3개의 정수가 있을 때, 이를 빠르게 가져오는 서비스를 제작해야한다.
            1. 빠르게 가져올 때에는 list에 담아주는 젓이 효과적이다.

### 형변환

    bin(), oct(), hex(), int(), float(), str(), bool()
    




































