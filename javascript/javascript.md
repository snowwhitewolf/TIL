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

```
이벤트를 처리하는 Call Stack이 하나
즉시 처리하지 못하는 이벤트들을 Web API로 보내서 처리
처리된 이벤트들은 처리된 순서대로 Task queue에 줄을 세워 놓고
Call Stack이 비면 Event Loop가 대기 줄에서 가장 오래된 이벤트를 Call Stack으로 보냄
```

### Callback function

```
다른 함수에 인자로 전달된 함수
외부 함수 내에서 호출되어 일종의 루틴 또는 작업을 완료함
동기식, 비동기식 모두 사용됨

JavaScript의 함수는 일급객체
일급객체 : 다른 객체들에 적용할 수 있는 연산을 모두 지원하는 객체(함수)
조건 : 인자로 넘길 수 있어야함, 함수의 반환 값으로 사용할 수 있어야 함, 변수에 할당할 수 있어야 함

callback Hell 해결
1. 코드의 깊이를 얕게 유지
2. 모듈화
3. 모든 단일 오류 처리
4. Promise 콜백 방식 사용
```

### Promise

```
비동기 작업의 최종 완료 또는 실패를 나타내는 객체
성공에 대한 약속 .then()
실패에 대한 약속 .catch()
return 값이 반드시 있어야 함
```

## Axios

```
브라우저를 위한 Promise 기반의 클라이언트
XHR 객체 대신 편리한 AJAX 요청이 가능하도록 도움
```

