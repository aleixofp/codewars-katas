import java.util.ArrayList;
public class SumSquaredDivisors 
{  
  public static String listSquared(long m, long n) {           
    String result = "[";
    for(; m < n; m++){          
      int divisorSum = 0;                    
      for(int i = 1; i <= m; i++){                            
        if (m % i == 0) {                  
          divisorSum += Math.pow(i, 2);
        }          
      }          
      double sqrt = Math.sqrt(divisorSum);                    
      String arr;
      if (sqrt == (int)sqrt){
        arr = "[" + m + ", " + divisorSum + "]";
        result += arr;
      } else
        arr = "[]";
    }            
    return result.replace("][", "], [") + "]";
  }
}
