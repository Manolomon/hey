$:.push('gen-rb')
$:.unshift '../../lib/rb/lib'

require 'thrift'

require 'hola_servicio'

begin
    port = ARGV[0] || 9090

    transport = Thrift::BufferedTransport.new(Thrift::Socket.new('localhost', port))
    protocol = Thrift::BinaryProtocol.new(transport)
    client = HolaServicio::Client.new(protocol)

    transport.open()

    mensaje = client.hola_func()
    puts"[Cliente] Se recibio " + mensaje

    transport.close()

rescue Thrift::Exception => tx
  print 'Thrift::Exception: ', tx.message, "\n"
end
