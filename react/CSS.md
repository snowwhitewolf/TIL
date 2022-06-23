# CSS 스타일

- 버튼 앞에 로고 넣기

  ```
  float
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

  

- 스크롤 방지

  ```javascript
  useEffect(() => {
    document.body.style.cssText = `
      position: fixed; 
      top: -${window.scrollY}px;
      overflow-y: scroll;
      width: 100%;`;
    return () => {
      const scrollY = document.body.style.top;
      document.body.style.cssText = '';
      window.scrollTo(0, parseInt(scrollY || '0', 10) * -1);
    };
  }, []);
  ```

  ```javascript
  class Mypage extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        isModalOpen: false
      }
      //! 모달창 띄웠을 때 스크롤 방지
      document.body.style.overflow = "hidden";
    }
  
    handleModal = () => {
      this.setState({
        isModalOpen: !this.state.isModalOpen
      })
      // 스크롤 방지 해제
      document.body.style.overflow = "unset"
    }
    ... 생략
  ```

  