const mongoose = require("mongoose");

const joblistSchema = new mongoose.Schema({
    company_name : {type:String,required:true},
    job_role : {type:String,required:true},
    discription : {type:String,required:true},
    package:{type:String}
});

module.exports = mongoose.model("joblist",joblistSchema);