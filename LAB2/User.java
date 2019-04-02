import java.net.*; import java.io.*;
public class User {
	private Socket sckt= null;
	private DataInputStream in= null;
	private DataOutputStream out = null;
	public User(String address, int port)
	{
		try
		{
			sckt = new Socket(address, port);
			System.out.println("Status: Connected to the server");
			System.out.println("Ip Address:"+address+" Port:"+port);
			in = new DataInputStream(System.in);
			out = new DataOutputStream(sckt.getOutputStream());
		} 
		catch(UnknownHostException exe)
		{
			System.out.println(exe);
		} 
		catch(IOException ioExe)
		{
			System.out.println(ioExe);
		} 
		String line = "";
		try
		{
			String ip = "Client 1:"+address;
			out.writeUTF(ip);
		}
		catch(IOException ioExe)
		{
			System.out.println(ioExe);
		} 	
		while (!line.equals("Bye Server"))
		{
			try
			{
				System.out.println("You :");
				line = in.readLine();
				out.writeUTF(line);
			} 
			catch(IOException ioExe)
			{
				System.out.println(ioExe);
			} 
		} 
		line = "";
		try
		{
			out.writeUTF(line);
			System.out.println("Closed the connection with server");
			in.close();
			out.close();
			sckt.close();
		} 
		catch(IOException ioExe)
		{
			System.out.println(ioExe);
		} 
	} 
	public static void main(String args[])
	{
		User user = new User("128.171.8.114",5009);
	} 
}
