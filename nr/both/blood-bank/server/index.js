const express = require('express')
const app = express()
const port = 7000
const approuteing = require('./routeing')
app.use("/",(approuteing))

app.listen( port ,'127.0.0.1')