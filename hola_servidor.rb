$:.push('gen-rb')
$:.unshift '../../lib/rb/lib'

require 'thrift'

require 'hola_servicio'
require 'hola_types'

class HolaHandle

  def hola_func()
    puts("[Servidor] Atendiendo la solicitud del cliente")
    return "Hola desde el servidor ruby"
  end

end

handler = HolaHandle.new()
processor = HolaServicio::Processor.new(handler)
transport = Thrift::ServerSocket.new(9090)
transportFactory = Thrift::BufferedTransportFactory.new()
server = Thrift::SimpleServer.new(processor, transport, transportFactory)

server.serve()
puts "done."