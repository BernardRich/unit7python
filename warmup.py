tic_tac_toe_list = ["1","2","3","4","5","6","7","8","9"]

turn = 0
while turn < 9:
    print( tic_tac_toe_list[0] + "|" + tic_tac_toe_list[1] + "|"+ tic_tac_toe_list[2] + "|")
    print('------')
    print( tic_tac_toe_list[3] + "|" + tic_tac_toe_list[4] + "|"+ tic_tac_toe_list[5] + "|")
    print('------')
    print( tic_tac_toe_list[6] + "|" + tic_tac_toe_list[7] + "|"+ tic_tac_toe_list[8] + "|")
    print('------')
    userturn = input( "enter number between 0-8 for your turn")

    numConverter = int( userturn)
    tic_tac_toe_list.insert(numConverter,"x")
    turn += 1 