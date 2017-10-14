import sys

sys.path.append('RAKE-tutorial')

import rake

# "Describe the incident which sparked the French Revolution."
# "What activity of the French monarchy hastened the Revolution?"
# "When did the French Revolution take place?"

def generateAnswerKeywords(correctAnswer):
    rake_object = rake.Rake("RAKE-tutorial\SmartStoplist.txt", 3, 3, 1)
    answerKeywordsTupleList = rake_object.run(correctAnswer)
    answerKeywordsUnsplit = []
    answerKeywords = []
    for t in answerKeywordsTupleList:
        answerKeywordsUnsplit.append(t[0])
    for k in answerKeywordsUnsplit:
        answerKeywords = answerKeywords + k.split()
    # print "correct answer is:"
    # print correctAnswer
    # print "correct answer keywords are:"
    # print answerKeywords
    return answerKeywords

def generateAnswerKeywordsAlt(correctAnswer):
    answerKeywords = correctAnswer.split()
    # print "correct answer is:"
    # print correctAnswer
    # print "correct answer keywords are:"
    # print answerKeywords
    return answerKeywords

def evaluateAnswer(questionFilePath, correctAnswerFilePath, userAnswerFilePath):
    questionFile = open(questionFilePath, 'r')
    question = questionFile.read()
    # print "question is:"
    # print question
    userAnswerFile = open(userAnswerFilePath, 'r')
    userAnswer = userAnswerFile.read()
    userAnswer = userAnswer.lower()
    # print "user answer is:"
    # print userAnswer
    correctAnswerFile = open(correctAnswerFilePath, 'r')
    correctAnswer = correctAnswerFile.read()
    correctAnswer = correctAnswer.lower()

    answerKeywords = generateAnswerKeywords(correctAnswer)
    if len(answerKeywords) == 0:
        answerKeywords = generateAnswerKeywordsAlt(correctAnswer)

    score = 0;
    for keyword in answerKeywords:
        if keyword in userAnswer:
            score = score + 1

    scorePercentage = float(score) / len(answerKeywords)
    if scorePercentage >= 0.80:
        print "Awesome answer!"
    elif scorePercentage >= 0.60:
        print "Great answer!"
    elif scorePercentage >= 0.40:
        print "Your answer was a pass."
    elif scorePercentage >= 0.20:
        print "Not too great."
    elif scorePercentage >= 0:
      print "Fail."
    # print scorePercentage
    return

def interactive():
    print "Whats the question ill ask you"
    question = raw_input("> ")
    questionFile = open("interactiveEval/question.txt", "w")
    questionFile.write(question)
    questionFile.close()
    print "Whats the correct answer"
    correctAnswer = raw_input("> ")
    correctAnswerFile = open("interactiveEval/correctAnswer.txt", "w")
    correctAnswerFile.write(correctAnswer)
    correctAnswerFile.close()
    print "Hi there, I have a question for you. The question is:"
    print question

    while(True):
        userAnswerFile = open("interactiveEval/userAnswer.txt", "w")
        userAnswer = raw_input("> ")
        userAnswerFile.write(userAnswer)
        userAnswerFile.close()
        evaluateAnswer("interactiveEval/question.txt", "interactiveEval/correctAnswer.txt", "interactiveEval/userAnswer.txt")
        print"You can try giving another answer, or quit by Ctrl C"
    return

interactive()

#Test 1
# evaluateAnswer("revolutionquestions/question1.txt", "revolutionanswers/correctAnswer1.txt", "revolutionanswers/userAnswer1A.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question1.txt", "revolutionanswers/correctAnswer1.txt", "revolutionanswers/userAnswer1B.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question1.txt", "revolutionanswers/correctAnswer1.txt", "revolutionanswers/userAnswer1C.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question1.txt", "revolutionanswers/correctAnswer1.txt", "revolutionanswers/userAnswer1D.txt")
#
# print "****************************************"
#
# evaluateAnswer("revolutionquestions/question2.txt", "revolutionanswers/correctAnswer2.txt", "revolutionanswers/userAnswer2A.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question2.txt", "revolutionanswers/correctAnswer2.txt", "revolutionanswers/userAnswer2B.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question2.txt", "revolutionanswers/correctAnswer2.txt", "revolutionanswers/userAnswer2C.txt")
# print "----------------------------------------"
#
# print "****************************************"
#
# evaluateAnswer("revolutionquestions/question3.txt", "revolutionanswers/correctAnswer3.txt", "revolutionanswers/userAnswer3A.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question3.txt", "revolutionanswers/correctAnswer3.txt", "revolutionanswers/userAnswer3B.txt")
# print "----------------------------------------"
#
# print "****************************************"
#
# evaluateAnswer("revolutionquestions/question4.txt", "revolutionanswers/correctAnswer4.txt", "revolutionanswers/userAnswer4A.txt")
# print "----------------------------------------"
# evaluateAnswer("revolutionquestions/question4.txt", "revolutionanswers/correctAnswer4.txt", "revolutionanswers/userAnswer4B.txt")
# print "----------------------------------------"

#Test2
# evaluateAnswer("bpquestions/question1.txt", "bpanswers/correctAnswer1.txt", "bpanswers/userAnswer1A.txt")
# print "----------------------------------------"
# evaluateAnswer("bpquestions/question1.txt", "bpanswers/correctAnswer1.txt", "bpanswers/userAnswer1B.txt")
# print "----------------------------------------"
#
# print "****************************************"
#
# evaluateAnswer("bpquestions/question2.txt", "bpanswers/correctAnswer2.txt", "bpanswers/userAnswer2A.txt")
# print "----------------------------------------"
# evaluateAnswer("bpquestions/question2.txt", "bpanswers/correctAnswer2.txt", "bpanswers/userAnswer2B.txt")
# print "----------------------------------------"
#
# print "****************************************"
#
# evaluateAnswer("bpquestions/question3.txt", "bpanswers/correctAnswer3.txt", "bpanswers/userAnswer3A.txt")
# print "----------------------------------------"
# evaluateAnswer("bpquestions/question3.txt", "bpanswers/correctAnswer3.txt", "bpanswers/userAnswer3B.txt")
# print "----------------------------------------"
#
# print "****************************************"
