import java.io.File;  // Import the File class
import java.io.*;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;
import java.util.Collections;


public class prob05{
    
    public static ArrayList<String> removeDuplicates(ArrayList<String> list) 
    { 
        ArrayList<String> newList = new ArrayList<String>(); 
        for (String element : list) { 
            if (!newList.contains(element)) { 
                newList.add(element); 
            } 
        } 
        return newList;
    } 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(new File("input.txt"));
        ArrayList<String> dates = new ArrayList<String>();
        ArrayList<String> dupes = new ArrayList<String>();
        int numOfInputs = s.nextInt();
        s.nextLine();

        for(int i = 0; i<numOfInputs; i++)
            dates.add(s.nextLine());

        for(int i = 0; i<dates.size(); i++){
            dates.set(i, dates.get(i).substring(0,dates.get(i).lastIndexOf("/")));
        }

        for (int i = 0; i < dates.size(); i++) {
            for (int j = i + 1 ; j < dates.size(); j++) {
                 if (dates.get(i).equals(dates.get(j))) {
                    dupes.add(dates.get(i));
                 }
            }
        }
        dupes = removeDuplicates(dupes);
        if(dupes.size() == 0){
            System.out.println(dupes.size());
            System.out.println("duplicates: None");
        }
        else{
            System.out.println(dupes.size());
            for(String i : dupes)
                System.out.print(i + " ");    
        }
    
    }

}

