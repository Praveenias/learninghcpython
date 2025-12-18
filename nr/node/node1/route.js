const express = require("express");
const router = express.Router();
const bodyparser = require('body-parser')
const homecontroller = require('./controller/homecontroller');
const auth = require('./middleware/authen')
const cors = require('cors');


router.use(bodyparser.urlencoded({extended:true}))
var jsonParser = bodyparser.json();
router.use(cors({
    origin:["http://localhost:3000"],
    methods:["GET","POST"],
    credentials:true
}))

router.get('/',homecontroller.home);
router.post('/register',homecontroller.register);
router.post('/login',jsonParser,homecontroller.login);
router.post('/joblist',homecontroller.joblist);


//auth middleware setted
router.get('/welcome',auth,homecontroller.welcome)
router.get('/logout',auth,homecontroller.logout)

module.exports = router;