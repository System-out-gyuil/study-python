## 모듈

    변수와 함수, 클래스등을 모아 놓은 파이썬 파일

### 모듈 사용

    import [모듈명]: 사용할 함수의 소속을 직접 코드에 작성하고 모든 필드를 사용하고자 할때
    import [모듈명] as [사용할 이름]: 모듈명이 길거나 복잡할 때 원하는 이름으로 설정에서 사용
    from [모듈명] import [필드명]: 모듈명을 직접 코드에 작성하지 않고 필드를 바로 사용하고자 할때
    from [모듈명] import *: 모듈 안에 있는 모든 필드를 바로 사용하고자 할때

### 패키지

    폴더를 생성하며 .py또는 ipynb파일을 관리 하고자 할때 해당 폴더를 패키지라고 한다
    __init__.py 파일을 생성해야 패키지로 인식되지만, 상위 버전(3.3부터)에서느
    __init__.py 파일이 없어도 패키지로 인식한다
    하지만, 하위 버전(3.3미만)에서도 인식되기 위해서는 직접 생성해 놓은 것이 좋다

## 주의 사항

    모듈을 사용할 파일의 이름이 모듈과 같으면 절대 못 쓴다