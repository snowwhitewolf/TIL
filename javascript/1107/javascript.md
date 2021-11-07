# JavaScript

##  javascript의 필요성

```
브라우저 화면을 동적으로 만들기 위함
브라우저를 조작할 수 있는 유일한 언어
```

## DOM

```
Document Object Model

DOM 조작 : 문서(HTML) 조작

HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
문서를 구조화하고 구조화된 구성요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델

Parsing : 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

BOM : Browser Object Model
자바스크립트가 브라우저와 소통하기 위한 모델
```

```
DOM 선택
Document.querySelector(selector)
Document.querySelectorAll(selector) : 실시간 반영 X

id, class, tag 선택자 등을 모두 사용가능하므로, 더 구체적이고 유연하게 선택 가능

Document.createElement() : 작성한 태그명의 HTML 요소를 생성하여 반환
Document.append() : 특정 부모 Node의 자식 NodeList중 마지막 자식 다음에 삽입, 여러 Node 객체와 문자열 추가, 반환 값 X
Document.appendChild() : Node만 추가 가능, 한번에 하나의 Node만 추가 가능
```

## Event

```
이벤트 발생
마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
```

```
EventTarget.addEventListener() : 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
target.addEventListener(type, listener[, options])

Event.preventDefault()
현재 이벤트의 기본 동작을 중단
태그의 기본 동작을 작동하지 않게 막음
```



## AJAX

```
Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)
서버와 통신하기 위해 XMLHttpRequest 객체를 활용
```

```
동기식
순차적, 직렬적 Task 수행
요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐

비동기식
병렬적 Task 수행
요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐
```

```
사용자 경험
매우 큰 데이터를 동반하는 앱이 있다고 가정
동기식 코드라면 데이터를 모두 불러온 뒤 앱이 실행됨
더욱 쾌적한 사용자 경험을 제공
```

