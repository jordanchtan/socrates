/**
 * Created by socce on 6/17/2017.
 */
public class Main {

    public static void main(String[] args) {

        String input = "The teachers have treated us kindly";
        HelpingVerbsClass hvc = new HelpingVerbsClass();
        if (hvc.containsAHelpingVerb(input)){
            hvc.reorder(input);
        }
        // does case sensitive matter

        String nextinput = "He cleans the bathroom";
        OtherStatements os = new OtherStatements();
        os.printQuestion(nextinput);
    }

}
