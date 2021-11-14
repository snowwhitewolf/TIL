# Vue

## Vue.js

```
SPA(Single Page Application)을 완벽하게 지원
단일 페이지 애플리케이션
서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성

페이지 규모가 계속해서 커지고 있고 사용하는 데이터도 늘어나고 사용자와의 상호작용도 많이 이루어짐
Data를 변경하면 이에 연결된 DOM은 알아서 변경
```

#### CSR

```
Client Side Rendering
서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성
최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링
SPA가 사용하는 렌더링 방식

장점 : 서버와 클라이언트 간 트래픽 감소, 사용자 경험 향상
단점 : SSR에 비해 전체 페이지 렌더링 시점이 느림, SEO에 어려움이 있음(검색 엔진 최적화)
```

#### SSR

```
Server Side Rendering
서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
전통적인 렌더링 방식

장점 : 초기 구동 속도가 빠름, SEO에 적합(Search Engine Optimization)
단점 : 모든 요청마다 새로운 페이지를 구성하여 전달, 서버의 부담이 클 수 있음
```

#### MVVM Pattern

```
Model, View, View Model

Model : Vue에서 Model dms JavaScript Object이다
View : Vue 에서 View는 DOM이다
ViewModel : Vue에서 ViewModel은 모든 Vue Instance이다
```



