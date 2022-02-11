# CSS 스타일

- 버튼 앞에 로고 넣기

  ```
  float
  ```

- Icon 사용법

  ```
  
  ```
  
- 스크롤바 제어

  ```
  
  ```
  
- 조건문

  ```
  
  ```
  

- 동작 시 클래스 추가

  ```typescript
  import "./home.css";
  import { useHistory } from "react-router-dom";
  import { useState } from "react";
  export default function Home() {
    const history = useHistory();
    const [move, setMove] = useState<boolean>(false);
    function routeLogin() {
      setMove(true);
      setTimeout(function () {
        history.push("/login");
        const bg = document.getElementsByClassName("home-container");
        console.log(bg);
      }, 1000);
    }
      
    return (
      <div className={`home-container ${move ? "login-move" : ""}`}>
        <div className="home-box">
          <img src="/images/logo1.png" alt="" />
          <button onClick={routeLogin} className="home-button">
            입장하기
          </button>
        </div>
      </div>
    );
  }
  ```

  