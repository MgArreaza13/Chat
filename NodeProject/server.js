var http = require('http')
var server = http.createServer().listen(3000)
var io = require('socket.io').listen(server)