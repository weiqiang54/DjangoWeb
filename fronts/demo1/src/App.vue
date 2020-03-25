<template>
  <div id="app">
    <div id="all">
      <div class="one">
        <div class="oneType" v-for="(item, index) in one" :key="index">
          <b>{{ one[index].name }}</b>
        </div>
      </div>
      <div class="twothreefour">
        <div class="two">
          <div class="twoType" v-for="(item, index) in two" :key="index" @mouseenter="open(index)">
            <b>{{ two[index].name }}</b>
          </div>
        </div>
        <div class="threefour" v-if="flag" @mouseleave="close()">
          <div class="threefourType" v-for="(item, index) in three1" :key="index">
            <span class="three">{{ three1[index] }}</span>
            <span class="four" v-for="(item4, index4) in four1" :key="index4">{{ four1[index4] }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      type: [],
      one: [],
      two: [],
      three1: [],
      four1: [],
      flag: false
    }
  },
  methods: {
    getData(){
      const api='http://192.168.18.153:8000/api/types/';
      var _this = this

      Axios.get(api).then(function(response){
          _this.type=response.data;
          for(var i=0; i<_this.type.length; i++){
            if(_this.type[i].category_type===1){
              _this.one.push(_this.type[i])
            }
          }
          console.log(_this.type.length)
          for(var j=0; j<_this.type.length; j++){
            if(_this.type[j].category_type===2){
              _this.two.push(_this.type[j])
            }
          }
      }).catch(function(error){
        console.log(error)
      })
    },
    open(index){
      this.three1 = []
      this.four1 = []
      var parent=this.two[index].id
      for(var i=0; i<this.type.length; i++){
        if(this.type[i].category_type===3){
          this.three1.push(this.type[i].name)
        }
        if(this.type[i].category_type===4){
          this.four1.push(this.type[i].name)
        }
      }
      this.flag=true
    },
    close(){
      this.flag=false
    }
  },
  mounted(){
      this.getData()
  }
}

</script>

<style>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
.all{
  width: 80%;
  height: 400px;
  background: #eee;
  margin: 50px auto;
  display: flex;
  display: -webkit-flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.one{
  width: 100%;
  height: 50px;
  background: #FF8888;
  display: flex;
  display: -webkit-flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.oneType{
  width: 20%;
  height: 50px;
  line-height: 50px;
  text-align: center;
}
.oneType:hover{
  background-color: chocolate;
  ccolor: #eee;
}
.twothreefour{
  width: 100%;
  height: 350px;
  background: #66FF66;
  display: flex;
  display: -webkit-flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.two{
  width: 15%;
  height: 100%;
  background: #77FFCC;
  display: flex;
  display: -webkit-flex;
  flex-direction: column;
}
.twoType{
  width: 100%;
  height: 40px;
  line-height: 40px;
  text-align: center;
  background: #EEFFBB;
}
.twoType: hover{
  background-color: black;
  ccolor: #eee;
}
.threefour{
  width: 40%;
  margin-right: 45%;
  height: 100%;
  background: #33FFDD;
  display: flex;
  display: -webkit-flex;
  flex-direction: column;
}
.threefourType{
  margin: 10px auto;
}
.three{
  font-family: 微软雅黑, 黑体;
  font-size: 16px;
  font-weight: 800;
}
.four{
  font-family: 宋体;
  font-size: 12px;
  font-weight: 400;
}
</style>
