import sys
sys.path.append("gen-py")
from hola import HolaServicio

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

transporte = TSocket.TSocket("localhost", 9090)
transporte = TTransport.TBufferedTransport(transporte)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)
cliente = HolaServicio.Client(protocolo)

transporte.open()
mensaje = cliente.hola_func()
print("[Cliente] Se recibio %s" % mensaje)
transporte.close()