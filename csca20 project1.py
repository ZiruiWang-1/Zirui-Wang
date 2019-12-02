game2of2 = ['thief', 'PSS']
game_choice = input('Which game you want to play? thief or PSS? ')
while str(game_choice) not in game2of2:
    print('You should choose thief or PSS only!')
    game_choice = input('Again, thief or PSS? ')
if str(game_choice) == 'PSS':
    import random
    list  = ['paper','scissor','stone']
    round = ['3','5']
    index = 0
    player_win = 0
    machine_win = 0
    play_times = input('3 rounds or 5 rounds? ')
    print('play ' + str(play_times) + ' times')
    while str(play_times) not in round:
        print('You should choose 3 or 5 rounds only!')
        play_times = input('Again, 3 or 5 rounds? ')
    while index < int(play_times):
        player_answer = input("What is your choice? ")
        machine_answer = random.choice(list)
        if player_answer not in list:
            print('Please input: paper or scissor or stone')
        else:
            if str(player_answer) == machine_answer:
                print('tie, no one win this round, machine answer is '+ machine_answer)
            if str(player_answer) == 'paper' and machine_answer == 'scissor':
                print('you lose, machine answer is '+ machine_answer)
                index = index + 1
                machine_win = machine_win + 1
            if str(player_answer) == 'paper' and machine_answer == 'stone':
                print('you win, machine answer is '+ machine_answer) 
                index = index + 1
                player_win = player_win + 1
            if str(player_answer) == 'scissor' and machine_answer == 'paper':
                print('you win, machine answer is '+ machine_answer)
                index = index + 1
                player_win = player_win + 1
            if str(player_answer) == 'scissor' and machine_answer == 'stone':
                print('you lose, machine answer is '+ machine_answer)
                index = index + 1
                machine_win = machine_win + 1
            if str(player_answer) == 'stone' and machine_answer == 'paper':
                print('you lose, machine answer is '+ machine_answer)
                index = index + 1
                machine_win = machine_win + 1
            if str(player_answer) == 'stone' and machine_answer == 'scissor':
                print('you win, machine answer is '+ machine_answer)
                index = index + 1
                player_win = player_win + 1
        print('Sore: player: ' + str(player_win) + ' machine: ' + str(machine_win))
    if player_win <= machine_win:
        print('Machine Win more')
    else:
        print('player win more')        
        
if str(game_choice) == 'thief':
    import random
    people_line = list(range(100))
    people_line2 = people_line
    thief = random.choice(people_line)
    thief = int(thief)
    number_of_guesses = 0
    answer = input('Which one is the thief? answer should between 0-99: ')
    answer = int(answer)
    while not answer == thief:
        if answer in people_line2:
            if answer < thief:
                del people_line2[:answer]
                print('the thief # is larger than your choice, give a larger answer')
                number_of_guesses = number_of_guesses + 1
            if answer > thief:
                del people_line2[answer:]
                print('the thief # is smaller than your choice, give a smaller answer')
                number_of_guesses = number_of_guesses + 1            
        else:
            print('You need to give a answer >=' + str(min(people_line2)) + ' and <=' + str(max(people_line2)))
        answer = input('It is not. Which one is the thief? ')
        answer = int(answer)
    if answer == thief:
        print('Good Luck! You caught the thief! The theif is #' + str(thief))
        number_of_guesses = number_of_guesses + 1
        print('Total number of Guesses: ' + str(number_of_guesses))     