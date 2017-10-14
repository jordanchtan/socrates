public class OtherStatements {

    public OtherStatements() {
    }

    public void printQuestion(String s){
        String verb = getVerb(s);
        String subject = getSubject(s);
        boolean singularSubject = isSingularSubject(subject);
        boolean simplePresentTense = isSimplePresentTenseVerb(verb);
        if(singularSubject && simplePresentTense){
            String changedVerb = verb.substring(0,(verb.length()-1));
            System.out.println("Does " + s.replaceFirst(verb,changedVerb));
        }
        else if(!singularSubject && simplePresentTense){
            System.out.println("Do " + s);
        }
        else if(!simplePresentTense){
            String verbinpresent = getPresentTenseForm(verb);
            System.out.println("Did " + s.replaceFirst(verb,verbinpresent));
        }
        else {
            System.out.println("Sorry! Did not manage to interpret it :(");
        }
    }

    public String getVerb(String s){
        //TODO
        return null;
    }

    public String getSubject(String s){
        //TODO
        return null;
    }

    public boolean isSimplePresentTenseVerb(String s){
        //TODO
        return false;
    }

    public boolean isSingularSubject(String s){
        //TODO
        if(s.equals("you") || s.equals("You")){
            return false;
        }
        else if(true){

        }
        return false;
    }

    public String getPresentTenseForm(String s){
        //TODO
        return null;
    }

    // Use google cloud
}
