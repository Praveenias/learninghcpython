const jwt = require("jsonwebtoken");
const config = require("../config/config")


const verifytoken = (req,res,next)=>{
    let token = req.header('auth_token')
    console.log("token",token);
    if(!token) return res.status(200).json({'status':'failure','err':'Access dinied'})
    try {
        const decoded = jwt.verify(token, config.TOKEN_SECRETE);
        req.user = decoded;
    } catch (err) {
        return res.status(200).json({'status':'failure','err':'Try another time'});
    }
    return next();
}

module.exports = verifytoken