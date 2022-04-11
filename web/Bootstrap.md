# Bootstrap

```
트위터에서 시작된 오픈 소스 프론트엔드 라이브러리
```

## spacing

```
m, p
0.25, 0.5, 1, 1.5, 3 - 4, 8, 16, 24, 48 
```

## Grid system

```
flexbox로 제작됨
container, rows, column으로 컨텐츠를 배치하고 정렬
12개의 column
6개의 grid breakpoints
```

### Grid breakpoints

```
다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점
offset - 특정 칸 이후에 컨텐츠가 나옴
```

sizing 너비는 w-75

수평정렬 mx-auto 안됨 왜 >> 공백이 없어서 >> 부모요소에 마진을 충분히 줘야됨

부모요소에서 text-center

flex 그리드 사용 부모 row justify-content-center 자식 col-8

흰색 글꼴 text-white

d-flex 단순히 디스플레이를 플렉스로 바꾸는것 튀어나감



글자에 패딩주는것 px-3

글자에 볼드 fw-bold

공백 주는법 마진이나 패딩 py-3

hr 색깔 bg 굵게하려면 pt-1

테두리 주는법 전체에다가 border

전체를 작게하는법 p-2으로 패딩을 줌

글자는 p태그 링크는 a태그

수평으로 같은 높이로 만들고 양쪽으로 정렬하려면 부모에 d-flex justify-content-between

링크밑에 밑줄없애는법 text-decoration-none

전체 크기로 바꾸려면 w-100

가로로 바꿀려면 flex-column

sticky를 사용하면 겹치지 않음 fixed보다 나음

a태그 안에 버튼 넣는게 좋음



수평에서 정렬하는것 p m around evenly



부트스트랩 그리드

row 안에 col

row박스 안에는 12칸으로 나눠져있다

브레이크포인트 

col-sm-6  576이상이면 컬럼이 6칸을 가진다
