# Vue CLI

```
Vue.js 개발을 위한 표준 도구
```

### SFC

```
Component
재사용 가능한 코드를 캡슐화 하는데 도움을 줌
컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라, 재사용성의 측면에서도 매우 강력한 기능을 제공
Vue 컴포넌트 === Vue 인스턴스

SFC(Single File Component)
하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일안에서 작성되는 코드의 결과물
Vue 컴포넌트 === Vue 인스턴스 === .vue 파일
```

### Node.js

```
자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경
단순히 브라우저만 조작할 수 있던 자바스크립트를 SSR 아키텍처에서도 사용할 수 있도록 함

NPM(Node Package Manage)
```

#### Babel

```
자바스크립트의 최신 코드를 이전 버전으로 번역/변환해 주는 도구 
```

#### Webpack

```
모듈간의 의존성 문제를 해결하기 위한 도구
프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
```

## Pass Props & Emit Events

#### 컴포넌트 등록 3단계

```
1. 불러오기(import)
2. 등록하기(component)
3. 보여주기
```

```
Props
props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야함
자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음
```

## Vue Router

```
Vue.js 공식 라우터
SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
```


