import React from "react";
import ReactDOM from "react-dom";
import { useForm, SubmitHandler } from "react-hook-form";

type Inputs = {
  ID : string,
  NickName : string,
  Email : string,
  MobileNumber : number,
};

export default function App() {
  const { register, handleSubmit } = useForm();
  const onSubmit: SubmitHandler<Inputs> = data => console.log(data);

  // 아이디 비밀번호 비밀번호 확인 닉네임 생년월일 최대주량 휴대전화번호
  return (
    <form>
      <input type="text" placeholder="아이디" {...register("ID", {required: true, maxLength: 80})} />
      <br />
      <input type="text" placeholder="닉네임" {...register("NickName", {required: true, maxLength: 100})} />
      <br />
      <input type="email" placeholder="이메일" {...register("Email", {required: true, pattern: /^\S+@\S+$/i})} />
      <br />
      <input type="tel" placeholder="휴대전화 번호" {...register("MobileNumber", {required: true, minLength: 6, maxLength: 12})} />
      <br />
      <input type="submit" />
    </form>
  );
}