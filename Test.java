import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println("Integer Number 1:");
    // keyboard input
    Scanner kb = new Scanner(System.in);//kb : keyboard
    int num1 = kb.nextInt();
    System.out.println("Integer Number 2:");
    int num2 = kb.nextInt();
    int temp = num1 + num2;
    System.out.println("The total = " + temp);
    if (num1 < 18) {
      System.out.println("Go home watch cartoon!");
    }
    else{
      System.out.println("Welcome to cinema!");
    }
    for (int i = 0; i < 3; i++) {
      System.out.println("Testing...");
      System.out.println("Test Passed!");
    }
  }
}
