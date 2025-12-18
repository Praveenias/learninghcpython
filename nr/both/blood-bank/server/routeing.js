const express = require("express");
const router = express.Router();
const cors = require("cors");
const bodyparser = require("body-parser");
const crypto = require("cryptr");
const cryptr = new crypto('myTotallySecretKey');
const mysql = require("mysql2");


// database
const db = mysql.createConnection({
    host: 'localhost',
    port:'3307',
    user: 'Praveen',
    password: 'Praveen@123',
    database: 'thiru'
});

db.connect(function(err) {
    if (err) {
        console.log(err);
        return;
    };
    console.log("Connected!");
});

router.use(cors())
router.use(express.json())
router.use(bodyparser.urlencoded({extended:true}))
// register
router.post("/register",(req,res) =>{
    const data = req.body;
    const name = data.name;
    const email = data.email;
    const password = data.password;
    // enceryption
    const password2=cryptr.encrypt(password)
    const query="insert into login(username,emailid,password) values(?,?,?)"
    db.query(query,[name,email,password2],(err,result) =>{
        if (err) {
            return res.send({'status':'failure','msg':err.sqlMessage})
        }
        else{
        return res.send({'status':'success','msg':""})
        }
    })

})
// Login form
router.post("/login",(req,res)=>{
    const data = req.body;
    //console.log(req)
    const name = data.name;
    const password=data.password;
    if(name== '' || password == ''){
        return res.send({'status':'failure','msg':"Kindly Fill All Details"})
    }
    console.log(name,password,'hit')
    let password2;
    db.query("select password from login where username = ?",[name],(err,result)=>{
        if(err){
            console.log(err);
            return res.send({'status':'failure','msg':err.sqlMessage})
        }
        console.log(result);
        console.log(result,'login result');
        if(result.length == 0 ){
            console.log('hit');
            return res.send({'status':'failure','msg':"no such user name"})
        }
        password2=result[0].password;
        password2=cryptr.decrypt(password2);
        if (password == password2){
            res.send(name)
        }
        else{
            res.send({'status':'failure','msg':"Please Enter Valid Password"})
        }
      
    })
    
})


// donate form
router.post("/Donate",(req,res) => {
    const data =req.body;
    console.log(req)
    if(data.name == ''){
        return res.send({'status':'failure','msg':'send data'})
    }
    console.log(data,'in form')
   // return res.send('check')
    const name = data.name;
    const m_num= data.m_num;
    console.log(m_num)
    const b_group = data.b_group;
    const location = data.location;
 
    const query="insert into bloodbank(name,mobilenumber,bloodgroup,location)values(?,?,?,?)"
    db.query(query,[name,m_num,b_group,location],(err,result)=>{
        if (err) {
            console.log(err)
            return res.send({'status':'failure','msg':err.sqlMessage})
        }
        else{
            return res.send({'status':'success','msg':''})
        }
    }) 
})

//request deatils deatils
router.post("/Request",(req,res) =>{
    const data =req.body;
    console.log(data);
    const Bloodgroup =data.Bloodgroup;
    const location = data.location;
    console.log(Bloodgroup);
    console.log(location);
    const query="select * from bloodbank where Bloodgroup = ?"
    db.query(query,[Bloodgroup,location],
    (err,result) =>{
        if (err){
            res.send(err)
        }
        res.send(result)
        console.log(result)
    })
})
// update
router.post("/update",(req,res) =>{
    const data =req.body;
    console.log(req)
    if(data.name == ''){
        return res.send({'status':'failure','msg':'send data'})
    }
    console.log(data,'in form')
   // return res.send('check')
    const name = data.name;
    const m_num= data.m_num;
    console.log(m_num)
    const b_group = data.b_group;
    const location = data.location;
    const query="update bloodbank set mobilenumber = ?,bloodgroup = ?,location=?  where name = ?"
    db.query(query,[m_num,b_group,location,name],(err,result) =>{
        if (err) {
            console.log(err);
            return res.send(err);
        }
        else{
            res.send(result);
        }
     })
 })

//delete 
router.delete("/delete/:number",(req,res) =>{
    const data=req.params;
    const m_num = data.number;
    console.log(m_num,'deteding')
    const query = "delete from bloodbank where mobilenumber = ?"
    db.query(query,[m_num],(err,result)=>{
        if (err){
            return res.send({'status':'failure','msg':err.sqlMessage})
        }
        else{
            res.send("deleted");
        }
    })
})


// function to return
router.get("/",(req,res) =>{
    res.send("server is runing")
})

module.exports = router;
