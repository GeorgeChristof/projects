package Server;

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
    private Socket s; //To socket tou client pou elegxei auto to thread
    private Hashtable<Socket, LinkedList<String>> clients; //To hashtable sto opoio apo8hkeuoume tous client kai ta arxeia tous
    private String clientIPandPort; //Ena string me thn IP:Port tou client
    private BufferedReader br; //To read gia auto to socket
    private PrintWriter pw; //To write gia auto to socket

    //Constructor
    //Apo8hkeuoume to socket kai to hashtable pou hr8e apo thn main
    //Ypologizoume to String clientIPandPort apo thn IP kai to Port tou socket
    //Dhmiourgoume BufferedReader kai PrintWriter gia auto to socket (gia na diavazoume kai na grafoume)
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

    //Methodos gia thn diaxeirisi tou Signin
    private void HandleSignin(String files)
    {
        System.out.println("Signing In!");
        files = files.replace("Signin", ""); //Afairoume thn le3h "Signin" apo to mhnuma pou hr8e
        String filenames[] = files.split(" "); //Xwrizoume tis le3eis kai ths apo8hkeuoume se pinaka
        LinkedList<String> clientFiles = new LinkedList<String>(Arrays.asList(filenames)); //Arxikopoioume LinkedList gia ta arxeia me ton pinaka filenames
        this.clients.put(s, clientFiles); //Apo8hkeuoume thn lista me arxeia sto Hashtable sto socket autou tou client
        SendOK(); //Stelnoume OK ston client
    }

    //Methodos gia thn diaxeiri tou Search
    private void HandleSearch(String keywordsAsString)
    {
        keywordsAsString = keywordsAsString.replace("Search",""); //Afairoume thn lexh "Search" apo to mhnuma pou hr8e
        String[] keywords = keywordsAsString.split(" "); //Xwrizoume ola ta keywords kai ta apo8hkeuoume se pinaka
        String searchResults = "Results\n"; //Etoimazoume to string gia to apotelesma, grafwntas "Results"

        Boolean matches = true; //Metavlhth pou krataei an to arxeio tairiazei me ola ta keywords

        for (Socket socket : clients.keySet()) //Gia ka8e client pou exoume sto Hashtable
        {
            LinkedList<String> clientFiles = clients.get(socket); //Vrisoume thn lista me ta arxeia (gia auton ton client)

            for (String file : clientFiles) { //Gia ka8e arxeio
                matches = true; //Arxikopoioume to matches se true. An kapoio keyword den tairiazei, 8a to kanoume false kai 8a stamathsoume ton elegxo (gia auto to arxeio)
                for (String keyword : keywords) //Gia ka8e keyword sthn anazhthsh
                {
                    if (!file.contains(keyword)) { //An h le3h den periexetai sto onoma tou arxeio
                        matches = false; //Kane to matches false
                        break; //Kai stamathse na to elegxeis
                    }
                }

                if (matches)
                    searchResults += file + ":" + clientIPandPort + '\n'; //An o elegxos teleiwse kai to matches einai akoma true, tote to arxeio tairiazei
            }
        }
        pw.println(searchResults); //Steile ston client ta apotelesmata
        pw.flush(); //Flush gia na fugoun ta dedomena
    }

    //Methodos pou diaxeirizetai to signout
    private void HandleSignout()
    {
        System.out.println(this.clientIPandPort + " Signing out!"); //Ektypwse ena mhnuma gia to signout
        this.clients.remove(s); //Afairese auton ton client kai ta arxeia tou apo to Hashtable
        SendOK(); //Steile OK
    }

    //Methodos pou stelnei "OK"
    private void SendOK()
    {
        pw.println("OK");
        pw.flush();
    }

    //Methodos pou trexei to thread
    public void run()
    {
        while (true)
        {
            String message = null;
            try { message = br.readLine();} //Diavase thn epomenh entolh apo ton client
            catch (IOException ex) { ex.printStackTrace(); }

            if (message.startsWith("Signin")) HandleSignin(message); //An einai Signin, trexe to HandleSignin
            else if (message.startsWith("Search")) HandleSearch(message); //An einai search, trexe to HandleSearch
            else if (message.startsWith("Signout")) //An einai Signout, trexe to HandleSignout (kai termathse to thread)
            {
                HandleSignout();
                break;
            }
            else System.out.println("Unknown Message: " + message); //Alliws ektypwse to agnwsto mhnuma
        }
    }
}

public class Server 
{

    private static Hashtable<Socket, LinkedList<String>> clients = new Hashtable<Socket, LinkedList<String>>(); //Arxikopoihse ena adeio HashTable gia olous tous clients kai ta arxeia tous

    public static void main(String args[]) 
    {
        ServerSocket serverSocket = null;

        try 
        {
            serverSocket = new ServerSocket(4242, 1, InetAddress.getByName("127.0.0.1")) ;
            System.out.println("Listening on Adapter: " + serverSocket.getLocalSocketAddress().toString());
        } 
        catch (Exception ex) {ex.printStackTrace();}

        //Perimenoume client na sunde8oun
        while (true) 
        {
            Socket clientSocket = null;
            try 
            {
                clientSocket = serverSocket.accept();
                System.out.println(clientSocket.getInetAddress().toString());
                System.out.println(clientSocket.getPort());
                new ServerThread(clientSocket, clients).start(); //Ftia3e kainourgio thread gia auton ton client
            }
            catch (IOException e)
            {
               e.printStackTrace();
            }
            
            
        }
    }
}
