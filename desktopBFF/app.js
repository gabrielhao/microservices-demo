const express = require('express')
var path = require("path")

const app = express()

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname+'/views/index.html'));
  //res.send('Hello World!')
})

app.get('/eventlist', function (req, res) {
  res.sendFile('list.html')
})

app.get('/event', function (req, res) {
  res.sendFile('event.html')
})

app.get('/add', function (req, res) {
  res.sendFile('edit.html');
})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
