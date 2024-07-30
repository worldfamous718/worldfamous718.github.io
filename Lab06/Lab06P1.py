#
# World McCrea
# 6/11/24
# This program demonstrates my understanding
# of nested lists

def main():
    # Get 3 scores from Ashley one by one
    a_list = [] # this is my blank list for Ashley scores

    print("Please enter Ashley's scores one by one.")
    for score in range(3):
        score = int(input('Enter a score: '))
        a_list.append(score) # this adds Ashleys scores to list
    print(f"Ashley's scores: {a_list} ")
    print('')

    # Get 5 scores from Barb one by one
    b_list = []  # blank list for Barb's scores

    print("Please enter Barb's score one by one.")
    for score in range(5):
        score = int(input('Enter a score: '))
      # add scores to list
        b_list.append(score)
    print(f"Barb's scores: {b_list} ")
    print('')


    # Get 4 scores for Carl one by one
    c_list = [] # blank list for Carl's scores

    print("Please enter Carl's scores one by one.")
    for score in range(4):
        score = int(input('Enter a score: '))
        c_list.append(score)
    print(f"Carl's scores: {c_list} ")
    print('')


    # create list with all student scores

    all_scores = [a_list[:], b_list[:], c_list[:],]
    print(f'All scores: {all_scores} ')

    # apply extra credit to each score
    for scores in all_scores: # this represents outer loop
        # im using len to deal with the differences in list lengths
        for index in range(len(scores)):
            scores[index] = int(scores[index] * 1.05)
    #display the extra credit scores
    print(f'All scores after extra credit: {all_scores}')

    score_spreads = [] # blank list to store the score spreads

     # get the min and max spreads
    for scores in all_scores:
        high = max(scores)
        low = min(scores)
        spread = high - low
        score_spreads.append(spread)

        # Display score spreads
    print(f'Score spreads: {score_spreads}')
    print('')


    print('Original Scores')
    print(f"Ashley's scores: {a_list}")
    print(f"Barb's scores: {b_list}")
    print(f"Carl's scores: {c_list}")



main()





