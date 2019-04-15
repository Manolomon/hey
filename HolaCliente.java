import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.TException;

public class HolaCliente {
    public static void main(String[] args) {
        TSocket trans = new TSocket("localhost", 9090);
        TBinaryProtocol protocolo = new TBinaryProtocol(trans);
        HolaServicio.Client cliente = new HolaServicio.Client(protocolo);
        
        try {
            trans.open();
            String cadena = cliente.hola_func();
            System.out.println("[Cliente] recibido: " + cadena);
        } catch (TException ex) {
            ex.printStackTrace();
        }
        trans.close();
    }
}