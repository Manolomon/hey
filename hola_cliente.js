var thrift = require('thrift');
var HolaServicio = require('./gen-nodejs/HolaServicio');
var ttypes = require('./gen-nodejs/hola_types');
const assert = require('assert');

var transport = thrift.TBufferedTransport;
var protocol = thrift.TBinaryProtocol;

var connection = thrift.createConnection("localhost", 9090, {
  transport : transport,
  protocol : protocol
});

connection.on('error', function(err) {
  assert(false, err);
});

var client = thrift.createClient(HolaServicio, connection);

client.hola_func(function(err, response) {
  console.log(response);
  connection.end();
});