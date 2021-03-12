import java.io.File;  // Import the File class
import java.io.*;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
import java.util.Collections;


public class prob06 {
    public static void main(String[] args) {
    
        String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String cipher = "FGHIJKLMNOPQRSTUVWXYZABCDE";
        Scanner s = new Scanner(System.in);
        s.nextInt();
        s.nextLine();
        String word = "";
        word = s.nextLine();
        String decode = "";
        for(int i = 0; i<word.length(); i++){
            try{
                decode+=alpha.charAt(cipher.indexOf(word.charAt(i)));
            }catch(Exception e){
                decode+=" ";
            }
            
        }
        System.out.println(decode);
    }
}
