<template>
    <div>
        <h1>{{title}}</h1>
        <button @click="sendcode">认证激活</button>
    </div>
</template>

<script>
import Axios from 'axios';
export default {
    data(){
        return{
            title: '认证激活'
        }
    },
    props: ['email'],
    methods: {
        sendcode(){
            var api='http://192.168.18.153:8000/sendactivecode/';
            Axios.get(api, {
                params: {
                email: this.email

                }
            }).then((response)=>{
                console.log(response.data)
            }).catch((error)=>{
                console.log(error)
            })
        }
    }

}
</script>