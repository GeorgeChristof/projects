package Client;

import java.io.*;
import java.net.Socket;
import java.util.LinkedList;

public class Client {

    private static LinkedList<String> files;
    private static String path;
    private static PrintWriter pw;
    private static BufferedReader br_socket;

    //Vriskei ola ta arxeia sto path kai ta vazei sto LinkedList files
    private static void getFileNames() {

        files = new LinkedList<String>();

        File folder = new File(path);
        File[] listOfFiles = folder.listFiles();

        for (int i = 0; i < listOfFiles.length; i++)
            if (listOfFiles[i].isFile()) files.add(listOfFiles[i].getName());
    }

    private static String FileNamesAsString()
    {
        String fileNames = "";
        for (String file : files) fileNames += file + " ";
        return fileNames;
    }

    //Kanei SignIn, stelnwntan
    public static boolean DoSignIn()
    {
        getFileNames();
        pw.println("Signin " + FileNamesAsString());
        pw.flush();
        return ExpectOK();
    }

    public static boolean ExpectOK()
    {
        boolean result = false;
        try {
           String response = br_socket.readLine();
           if (response.contentEquals("OK")) result = true;
        } catch (IOException e) { result = false; }

        return result;
    }

    public static void DoSearch(String command)
    {
        pw.println(command);
        pw.flush();
        DoPrintResults();
    }

    public static void DoPrintResults()
    {
        String line;
        try {
            while (br_socket.ready() == false);
            while (br_socket.ready() && (line = br_socket.readLine()) != null) System.out.println(line);
        } catch (IOException e) { e.printStackTrace();}
    }

    public static boolean DoSignout()
    {
        pw.println("Signout");
        pw.flush();
        return ExpectOK();
    }

    public static void main(String[] args){
        if (args.length != 1) {
            System.out.println("Error: you forgot <server IP>");
            return;
        }

        String serverIP = args[0];
        Socket socket = null;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        path = "testfiles"; //The path of the files to share

        try {
            socket = new Socket(serverIP, 4242);
            pw = new PrintWriter(socket.getOutputStream());
            br_socket = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        } catch (Exception e) { e.printStackTrace();}

        System.out.println("Signing in");

        boolean result = DoSignIn();

        if (result)
        {
            System.out.println("Sign in Successful!");
            while (true) {
                try {
                    System.out.println("Enter Search <keywords> to search, or Signout to exit");
                    String command = br.readLine();

                    if (command.startsWith("Search")) DoSearch(command);
                    else if (command.startsWith("Signout")) if (DoSignout()) break;

                } catch (IOException e) { e.printStackTrace();}
            }

        }
        else System.out.println("Failed to sign in");
        System.out.println("Exiting");
    }


}