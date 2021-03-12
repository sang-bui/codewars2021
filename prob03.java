import java.io.File;  // Import the File class
import java.io.*;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.ArrayList;

public class prob03 {
    public static void main(String[] args) throws IOException {
        ArrayList<String> map = new ArrayList<String>();

        
        Scanner s = new Scanner(new File("input.txt"));
        while(s.hasNextLine()){
            map.add(s.nextLine());
        }

        int pRow = -1;
        int pCol = -1;

        for(int row = 0; row<map.size(); row++){
            for(int col = 0; col<map.get(row).length(); col++){
                if(map.get(row).charAt(col) == 'P'){
                    pRow = row;
                    pCol = col;
                    break;
                }
            }
        }

        if(pRow == -1 && pCol == -1)
            System.out.println("No pigeon, try another map, Ace");
        else
            System.out.println("Ace, move fast, pigeon is at (" + pCol +", " + pRow + ")");

    }
}
