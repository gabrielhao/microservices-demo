const express = require('express')
const bodyParser = require('body-parser')

const app = express()

app.get('/', function (req, res) {
  res.sendFile('index.html');
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

app.listen(80, function () {
  console.log('Example app listening on port 80!')
})
