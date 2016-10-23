import java.util.*;
/**
 * Created by lisabug on 3/5/16.
 */
public class Solution {
    public int calculate(String s) {
        Stack<Character> stack = new Stack<>();
        int num = 0;
        List<String> post = new ArrayList<String>();
        Character c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (c == ' ') continue;
            switch (c) {
                case '+': ;
                case '-':
                    post.add(String.valueOf(num));
                    num = 0;
                    if (stack.isEmpty()) stack.push(c);
                    else {
                        while (!stack.isEmpty()){
                            post.add(stack.pop().toString());
                        }
                        stack.push(c);
                    }
                    break;
                case '*': ;
                case '/':
                    post.add(String.valueOf(num));
                    num = 0;
                    if (stack.isEmpty() || stack.peek() == '+' || stack.peek() == '-') {
                        stack.push(c);
                    }
                    else {
                        while (!stack.isEmpty() && stack.peek() != '+' && stack.peek() != '-') {
                            post.add(stack.pop().toString());
                        }
                        stack.push(c);
                    }
                    break;
                default:
                    num = num*10 + c - '0';
            }
        }
        post.add(String.valueOf(num));
        while (!stack.isEmpty()) {
            post.add(stack.pop().toString());
        }

        Stack<Integer> result = new Stack<>();
        int a,b;
        for (int i = 0; i < post.size(); i++) {
            if (post.get(i).equals("+")) {
                result.push(result.pop()+result.pop());
            }
            else if (post.get(i).equals("-")) {
                result.push(-result.pop()+result.pop());
            }
            else if (post.get(i).equals("*")) {
                result.push(result.pop()*result.pop());
            }
            else if (post.get(i).equals("/")) {
                a = result.pop();
                b = result.pop();
                result.push(b/a);
            }
            else {
                result.push(Integer.parseInt(post.get(i)));
            }
        }
        return result.pop();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s = "1+2*5/3+6/4*2";
        System.out.println(solution.calculate(s));
    }
}
