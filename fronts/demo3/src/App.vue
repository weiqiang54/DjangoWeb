<template>
  <div id="app">
    <h1>{{ title }}</h1>
    <div class="registerwindow">
      <div class="title">用户注册</div>
      <div class="item">
        <div class="text">用户名:</div>
        <input type="text" v-model="username">
      </div>
      <div class="item">
        <div class="text">密码:</div>
        <input type="text" v-model="pwd">
      </div>
      <div class="item">
        <div class="text">邮箱:</div>
        <input type="text" v-model="email">
      </div>
      <div class="item">
        <div class="text">手机号:</div>
        <input type="text" v-model="phone">
        <button :disabled="disabled" @click="authPhone">{{codebtn}}</button>
      </div>
      <div class="item">
        <div class="text">验证码:</div>
        <input type="text" v-model="code">
        <button @click="authUserinfo">确认注册</button>
      </div>
      <v-active :email='email'></v-active>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';
import Active from './components/Active';
export default {
  name: 'app',
  data () {
    return {
      title: '首页',
      codebtn: '获取验证码',
      disabled: false,
      time: 0,
      phone: '',
      username: '',
      pwd: '',
      code: '',
      email: ''
    }
  },
  components: {
    'v-active': Active
  },
  methods: {
    getCode(){
      //向后台发送请求，获取验证码
      var api='http://192.168.18.153:8000/sendcode/';
      Axios.get(api, {
        params: {
          phone: this.phone
        }
      }).then((response)=>{
        console.log(response.data)
      }).catch((error)=>{
        console.log(error)
      })
    },
    goRegister(){
      var api='http://192.168.18.153:8000/register/';
      Axios.get(api, {
        params: {
          phone: this.phone,
          username: this.username,
          pwd: this.pwd,
          code: this.code,
          email: this.email

        }
      }).then((response)=>{
        console.log(response.data)
      }).catch((error)=>{
        console.log(error)
      })
    },
    authPhone(){
      var reg=11 && /^((13|14|15|17|18)[0-9]{1}\d{8})$/;
      if(this.phone==''){
        alert("请输入手机号")
      }else if(!reg.test(this.phone)){
        alert("手机格式不正确")
      }else{
        this.time=60;
        this.disabled=true;
        this.timer();
        this.getCode();
      }
    },
    timer(){
      if(this.time>0){
        this.time--;
        this.codebtn=this.time+"s";
        setTimeout(this.timer, 1000);
      }else{
        this.time =0;
        this.codebtn="获取验证码";
        this.disabled=false;
      }
    },
    authUserinfo(){
      if(this.username==''){
        alert("用户名不能为空")
      }else if(this.pwd==''){
        alert("密码不能为空")
      }else if(this.phone==''){
        alert("手机号不能为空")
      }else if(this.code==''){
        alert("验证码不能为空")
      }else{
        this.goRegister()
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.registerwindow{
  margin: 0 auto;
  width: 350px;
  height: 200px;
  background: rgba(5, 55, 148, 0.5);
}
.title{
  margin: 0 auto;
  font-size: 30px;
  text-align: center;
}
.item{
  margin-top: 10px;
  display: flex;
  flex-direction: row;
}
.text{
  text-align: center;
  width: 80px;
}
input{
  width: 140px;
}
button{
  width: 80px;
  margin-left: 5px;
}
</style>
