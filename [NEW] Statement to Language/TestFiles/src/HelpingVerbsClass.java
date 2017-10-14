public class HelpingVerbsClass {

    public HelpingVerbsClass() {
    }

    String[] helpingVerbs = {
            "am ",
            "is ",
            "are ",
            "was ",
            "were ",
            "be ",
            "being ",
            "been ",
            "have ",
            "has ",
            "had ",
            "do ",
            "does ",
            "did ",
            "could ",
            "should ",
            "would ",
            "can ",
            "shall ",
            "will ",
            "may ",
            "might ",
            "must "
    };

    public void reorder(String string){
        String reordered = statementToQuestion(string);
        System.out.println(reordered);
    }

    public String statementToQuestion(String string){
        String thishelpverb = "";
        for(String helpverb : helpingVerbs){
            if(containsThisHelpingVerb(string,helpverb)){
                thishelpverb = helpverb;
                break;
            }
        }
        return thishelpverb + string.replaceFirst(thishelpverb,"");
    }

    public boolean containsAHelpingVerb(String string){
        for(String helpverb : helpingVerbs){
            if(containsThisHelpingVerb(string,helpverb)){
                return true;
            }
        }
        return false;
    }

    private boolean containsThisHelpingVerb(String string, String helpVerb){
        return string.contains(helpVerb);
    }
}
