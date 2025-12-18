const User = require("../mongo_model/user");
const Joblist = require("../mongo_model/joblist");
const crypto = require("cryptr");
const cryptr = new crypto('myTotallySecretKey');
const jwt = require("jsonwebtoken");
const config = require('../config/config');


const home =async (req,res)=>{
    res.send('Welcome to Nodejs Server')
}

const joblist = async(req,res) => {
    let columns = ['company_name','job_role','discription']
    let data = req.body;
    console.log(data);
    let datas = Joblist.create(data)
    res.send('got it')
}

const register = async(req,res) => {
    let columns = ['name','email','password']
    let data = req.body
    console.log(req.body);
    columns.forEach(element => {
        if(data[element] == '' || !(element in data)){
            return res.status(200).json({'status':'failure','err':element+" is null"});
        }
    });
    let email = data['email'];
    let pre_email = await User.findOne({email})
    if(pre_email != null){
        return res.status(200).json({'status':'failure','err':'email already present'});
    }else{
        data['password']=cryptr.encrypt(data['password']);
        let res_data = await User.create(data)
        console.log(res_data);
        return res.status(200).json({'status':'success','err':''});
    }
}

const login = async(req,res) => {
   // res.setHeader('Content-Type', 'text/plain');
   console.log(req.body);
    let columns = ['email','password']
    let data = req.body
    columns.forEach(element => {
        if(data[element] == '' || !(element in data)){
            return res.status(200).json({'status':'failure','err':element+" is null"});
        }
    });
    let user = await User.findOne({'email':data['email']});
    if(user != null){
        if(!(data['password'] == cryptr.decrypt(user.password))){
            return res.status(200).json({'status':'failure','err':'email or Password is wrong'});
        }
        const token = jwt.sign({id: user.email}, config.TOKEN_SECRETE,{expiresIn: "2h"});
        user.token = token;
        user.save();
        return res.status(200).json({'status':'success','err':'authunticated','data':{'name':user.name,'token':user.token}})
    }else{
        res.status(200).json({'status':'failure','err':'Email or Password is wrong'});
    }
}

const welcome = async(req,res) => {
    res.status(200).json({'status':'success','err':''});
}

const logout = async(req,res) =>{
    console.log(req.header('auth-token'))
}


module.exports = {home,register,login,welcome,logout,joblist};