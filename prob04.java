import java.io.File;  // Import the File class
import java.io.*;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
import java.util.Collections;

public class prob04 {
    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<String>> graph = new ArrayList<>();
        Scanner s = new Scanner(new File("input.txt"));
        int numOfInputs = s.nextInt();
        s.nextLine();
        for(int row = 0; row<numOfInputs; row++){
            Scanner b = new Scanner(s.nextLine());
            graph.add(new ArrayList<String>());
            b.useDelimiter("");
            while(b.hasNext()){
                graph.get(row).add(b.next());
            }
        }

        //for(ArrayList<String> r : graph){
            //Collections.reverse(r);    
        //}
        Collections.reverse(graph);
        
        for(ArrayList<String> r : graph){
            for(String c : r){
                System.out.print(c);
            }
            System.out.println();
        } 
    }    
}
