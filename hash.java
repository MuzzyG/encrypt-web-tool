import java.io.FileNotFoundException;
import java.security.*;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;


public class hash {
  public static void main(String[] args) {
    byte[] input_bytes = null;
    try {
      //Read file into bytes
      input_bytes = Files.readAllBytes(Paths.get(args[1]));
    } catch (FileNotFoundException e) {
      System.out.println("File not found");
      return;
    } catch (IOException e) {
      System.out.println("File not found");
      return;
    }

    if (args[0].equals("md5")) {
      try {
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] output_hash = md.digest(input_bytes);

        //Convert to string
        BigInteger no = new BigInteger(1, output_hash);
        String output_string = no.toString(16);
        System.out.println(output_string);

      } catch (NoSuchAlgorithmException e) {
        //This error shouldn't happen but apparently needs to be caught
        e.printStackTrace();
        return;
      }
    } else if (args[0].equals("sha256")) {
      try {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] output_hash = md.digest(input_bytes);

        //Convert to string
        BigInteger no = new BigInteger(1, output_hash);
        String output_string = no.toString(16);
        System.out.println(output_string);
      } catch (NoSuchAlgorithmException e) {
        //This error shouldn't happen but apparently needs to be caught
        e.printStackTrace();
        return;
      }
    } else if (args[0].equals("sha512")) {
      try {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] output_hash = md.digest(input_bytes);

        //Convert to string
        BigInteger no = new BigInteger(1, output_hash);
        String output_string = no.toString(16);
        System.out.println(output_string);
      } catch (NoSuchAlgorithmException e) {
        //This error shouldn't happen but apparently needs to be caught
        e.printStackTrace();
        return;
      }
    } else {
      System.out.println("Algorithm not accepted.");
    }
  }
}
