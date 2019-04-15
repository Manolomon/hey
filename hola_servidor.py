import sys
sys.path.append("gen-py")
from hola import HolaServicio

from thrift.transport import TSocket

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HolaHandle:
    def hola_func(self):
        print("[Servidor] Atendiendo la solicitud del cliente")
        return "Hola desde el servidor python"

handler = HolaHandle()

procesador = HolaServicio.Processor(handler)

transporte_serv = TSocket.TServerSocket(port=9090)

transporte_fact = TTransport.TBufferedTransportFactory()

protocolo_fact = TBinaryProtocol.TBinaryProtocolFactory()

servidor =TServer.TSimpleServer(procesador, transporte_serv, transporte_fact, protocolo_fact)
servidor.serve()