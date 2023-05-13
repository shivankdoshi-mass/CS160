import java.util.Scanner;

public class MainProgram {
	public static void main(String[] args){
		Scanner keyboardReader = new Scanner(System.in); 

		boolean exit = true;
		while (exit){
	
		System.out.println("Enter option from list below:");
		System.out.println("1) Display complete Directory");
		System.out.println("2) Enter new Person");
		System.out.println("3) Search for Person");
		System.out.println("4) Modify Person information");
		System.out.println("5) Delete a record.");
		System.out.println("Q) Quit");
		System.out.println("Enter your option:");

		String option = keyboardReader.nextLine();

		if (option.equals("1")) {
  		
		}

		else if (option.equals("2")) {

		}
		else if (option.equals("3")) {


			
		}
	
		else if (option.equals("4")) {

		}
		else if (option.equals("5")) {

		}
	
		else if (option.equals("Q") ||option.equals("q")) {
			exit = false;
		}
	
		else {
			System.out.println("Error");
		}


	}
	keyboardReader.close();	


	}

	
}
