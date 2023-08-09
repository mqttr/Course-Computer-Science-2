def Main():
    totalNumber = int(input("Total number of students: ").strip())

    # Invalid Response Handling
    while True:
        numberList = input(f"Enter {totalNumber} score(s): ").strip().split()
        scoreList = [ int(ele) for ele in numberList ]

        if len(numberList) >= totalNumber:
            # Chop off scoreList excess
            scoreList = scoreList[0:totalNumber]
            break

    highScore = max(scoreList)

    for individualStudentScore in scoreList:
        grade = "x"

        if individualStudentScore >= highScore - 10: grade = "A"
        elif individualStudentScore >= highScore - 20: grade = "B"
        elif individualStudentScore >= highScore - 30: grade = "C"
        elif individualStudentScore >= highScore - 40: grade = "D"
        else: grade = "F"

        print(f"Student {scoreList.index(individualStudentScore)+1} score is {individualStudentScore} and grade is {grade}")

if __name__ == "__main__":
    print(set('cat hat'))