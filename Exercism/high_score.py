def high_score_viewer(a_list):
    print("Last Added Score: " + str(a_list[-1]))
    a_list.sort()
    print("Highest Score: " + str(a_list[-1]))
    print("Last 3 Scores: " + str(a_list[-3:]))


a_list = [100, 631, 399, 571]

high_score_viewer(a_list)
