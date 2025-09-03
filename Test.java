package Test;
import java.utli.Scanner;
public class TestPackageClass{
  public static void main(string[]){
    // keyboard input
    scanner kb = new scanner (system.in);
    system.out.println("Input a integer number: ");
    int num1 = kb.nextline();
    system.out.println("Input one more integer number: ");
    int num2 = kb.nextline();
    int temp = num1 + num2;
    system.out.println("The total of two numbers = " + temp);
    if (num1 < 18){
      system.out.println("Go home watch cartoon!");
    }
    else{
      system.out.println("wlcome to cinema!");
    }
  }
}
