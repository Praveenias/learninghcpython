const express1 = require('express')
require("./mongo_model/database").connect();
const User = require("./mongo_model/user");
const Joblist = require("./mongo_model/joblist")
//const sequelizer = require('./model/database')
// const User = require('./model/login')
// const Foodlist = require('./model/fooditems')
// const Cart = require('./model/cart')
const home = require('./route')

const app = express1()

app.use('/',(home))



const host = 'http://127.0.0.1:3000'
app.listen(3001,'127.0.0.1',()=>{
    console.log('server started : '+host)
})







