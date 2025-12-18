import axios from "axios";

const url = 'http://127.0.0.1:7000/'
const Loginpost = (data) => {
    let suburl = 'login'
    return axios.post(url+suburl,data)
}

const Requestblood = (data) => {
    let suburl = 'Request'
    return axios.post(url+suburl,data)
}

const RegisterUser = (data) => {
    console.log(data)
    let suburl = 'register'
    return axios.post(url+suburl,data) 
}

const Donate_data = (data) => {
    console.log(data)
    let suburl = 'Donate'
    return axios.post(url+suburl,data) 
}

const Update_blooddata = (data) => {
    console.log(data)
    let suburl = 'update'
    return axios.post(url+suburl,data) 
}

const Delete_blood = (data) => {
    console.log(data,'in service')
    let suburl = 'delete/'
    return axios.delete(url+suburl+data)
}

export {Loginpost,Requestblood,RegisterUser,Donate_data,Update_blooddata,Delete_blood}