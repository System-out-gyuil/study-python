## 파일

    외부의 파일을 생성하거나 내용을 작성할 수 있으며, 기존의 내용도 알아올 수 있다

### 파일 생성하기

    파일을 열고 작성할 때 사용한다
    'w'를 작성해서 운영체제에게 파일을 여는 족적을 알려줘야 하며, 이때 'w'를 작성한다
    open(path, 'w')

### 내용 추가하기

    기존의 내용을 업애지 않고 아래의 내용을 추가한다. 이 때에는 추가 모드인 'a'를 작성한다
    open(path, 'a')

### 파일 읽기

    기존 내용을 한 줄씩 읽어 올때 'r'를 작성하여 읽기 모드로 파일을 열러준다
    open(path, 'r')