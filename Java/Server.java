import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.ServerSocket;
import java.util.Arrays;
import java.util.Hashtable;
import java.util.LinkedList;

class ServerThread extends Thread
{
    private Socket s;
    private Hashtable<Socket, LinkedList<String>> clients;
    private String clientIPandPort;
    private BufferedReader br;
    private PrintWriter pw;

    public ServerThread(Socket s, Hashtable clients)
    {
        this.s = s;
        this.clients = clients;
        this.clientIPandPort = s.getInetAddress() + ":" + s.getPort();
        try {
            br = new BufferedReader(new InputStreamReader(s.getInputStream()));
            pw = new PrintWriter(s.getOutputStream());
        } catch (IOException e) { e.printStackTrace(); }
    }

    private void HandleSignin(String files)
    {
        System.out.println("Signing In!");
        files = files.replace("Signin", "");
        String filenames[] = files.split(" ");
        LinkedList<String> clientFiles = new LinkedList<String>(Arrays.asList(filenames));
        this.clients.put(s, clientFiles);
        SendOK();
    }

    private void HandleSearch(String keywordsAsString)
    {
        keywordsAsString = keywordsAsString.replace("Search","");
        String[] keywords = keywordsAsString.split(" ");
        String searchResults = "Results\n";

        Boolean matches = true;

        for (Socket socket : clients.keySet()) 
        {
            LinkedList<String> clientFiles = clients.get(socket);

            for (String file : clientFiles) {
                matches = true;
                for (String keyword : keywords) 
                {
                    if (!file.contains(keyword)) { 
                        matches = false;
                        break;
                    }
                }

                if (matches)
                    searchResults += file + ":" + clientIPandPort + '\n';
            }
        }
        pw.println(searchResults);
        pw.flush();
    }

    private void HandleSignout()
    {
        System.out.println(this.clientIPandPort + " Signing out!");
        this.clients.remove(s);
        SendOK();
    }

    private void SendOK()
    {
        pw.println("OK");
        pw.flush();
    }

    public void run()
    {
        while (true)
        {
            String message = null;
            try { message = br.readLine();}
            catch (IOException ex) { ex.printStackTrace(); }

            if (message.startsWith("Signin")) HandleSignin(message);
            else if (message.startsWith("Search")) HandleSearch(message);
            else if (message.startsWith("Signout")) 
            {
                HandleSignout();
                break;
            }
            else System.out.println("Unknown Message: " + message);
        }
    }
}

public class Server 
{

    private static Hashtable<Socket, LinkedList<String>> clients = new Hashtable<Socket, LinkedList<String>>();

    public static void main(String args[]) 
    {
        ServerSocket serverSocket = null;

        try 
        {
            serverSocket = new ServerSocket(4242) ;
        } 
        catch (Exception ex) {ex.printStackTrace();}

        while (true) 
        {
            Socket clientSocket = null;
            try 
            {
                clientSocket = serverSocket.accept();
                new ServerThread(clientSocket, clients).start();
            }
            catch (IOException e)
            {
               e.printStackTrace();
            }
            
            
        }
    }
}
