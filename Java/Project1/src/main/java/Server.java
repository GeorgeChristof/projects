import java.io.IOException;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.util.*;

public class Server 
{   
    HashMap<Integer,String> userNames = new HashMap<Integer,String>();
    
    public static void main(String args[]) 
    {
        DatagramSocket socket = null;
        
        //Dhmiourgeia socket gia send kai receive
        try 
        {
            socket = new DatagramSocket(4242);
        } 
        catch (SocketException ex) 
        {
            ex.printStackTrace();
        }
        
        while (true) 
        {
            try 
            {
                String s = NetworkTools.receiveData(socket);
                String []sp = s.split(":"); //sp[0] = keimeno mhnymatos, sp[1] = IP apostolea san String, sp[2]= port apostolea san String
                User.userIp = sp[1];
                User.userPort = sp[2];
                System.out.println("Message: " + sp[0] + " from " + " Username: " + userNames.get(User.userPort)); ///+ User.userIp + ":" + Integer.parseInt(User.userPort) 
            } 
            catch (IOException ex) 
            {
                ex.printStackTrace();
            }
        }
    }
    static void addUserName(String userName) {
        userNames.put(Integer.parseInt(User.userPort),User.userName);
    }
}
