'''
NOTES:

Prisoners_Dilemma.py allows hard-coding of different strategies
for the Iterative Prisoners Dilemma, the classic game of game-theory.
Each strategy plays 100 to 200 rounds against each other's strategy.
The results of all previous rounds within a 100-200 round stretch are known
to both players.

Pressing the green arrow button will allow you to run the tournament and
store the output in tournament.txt

Teams should each code their strategies in their assigned section of code.
'''

import random
def play_round(player1, player2, history1, history2, score1, score2):
    '''
    Calls the get_action() function which will get the characters
    'c' or 'b' for collude or betray for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 4-tuple with updated histories and scores
    (history1, history2, score1, score2)
    '''

    RELEASE = 0  # (R) when both players collude
    TREAT = 100  # (T) when you betray your partner
    SEVERE_PUNISHMENT = -500 # (S) when your partner betrays you
    PUNISHMENT = -250  # (P) when both players betray each other
    # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma

    #Get the two players' actions and remember them.
    action1 = get_action(player1, history1, history2, score1, score2)
    action2 = get_action(player2, history2, history1, score2, score1)
    if type(action1) != str:
        action1=' '
    if type(action2) != str:
        action2=' '
    #Append the actions to the previous histories, to return
    new_history1 = history1 + action1
    new_history2 = history2 + action2

    #Change scores based upon player actions
    if action1 not in ('c','b') or action2 not in ('c','b'):
    # Do nothing if someone's code returns an improper action
        new_score1 = score1
        new_score2 = score2

    else:
    #Both players' code provided proper actions
        if action1 == 'c':
            if action2 == 'c':
                # both players collude; get reward
                new_score1 = score1 + RELEASE
                new_score2 = score2 + RELEASE
            else:
                # players 1,2 collude, betray; get sucker, tempation
                new_score1 = score1 + SEVERE_PUNISHMENT
                new_score2 = score2 + TREAT
        else:
            if action2 == 'c':
                # players 1,2 betray, collude; get tempation, sucker
                new_score1 = score1 + TREAT
                new_score2 = score2 + SEVERE_PUNISHMENT
            else:
                # both players betray; get punishment
                new_score1 = score1 + PUNISHMENT
                new_score2 = score2 + PUNISHMENT

    #send back the updated histories and scores
    return (new_history1, new_history2, new_score1, new_score2)

def play_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds)
    of the iterative prisoners' dilemma between two strategies.
    identified in the parameters as integers.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600)
    but with much longer strings
    '''
    number_of_rounds = random.randint(100,200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        moves1, moves2, score1, score2 = \
            play_round(player1, player2, moves1, moves2, score1, score2)
    return (moves1, moves2, score1, score2)

def get_action(player, history, opponent_history, score, opponent_score, getting_team_name=False):
    '''Gets the strategy for the player, given their own history and that of
    their opponent, as well as the current scores within this pairing.
    The parameters history and opponent history are strings with one letter
    per round that has been played so far: either an 'c' for collude or a 'b' for
    betray. The function should return one character, 'c' or 'b'.
    The history strings have the first round between these two players
    as the first character and the most recent round as the last character.'''

    #TEAMS 0-2 ARE EXAMPLE TEAMS


    #Team0: Loyal
    # This example player always colludes
    #######################################


    if player == 0:
        if getting_team_name:
            return 'Loyal'
        else:
            return 'c'



    #Team1: Backstabber
    # This example player always betrays
    #######################################


    elif player == 1:
        if getting_team_name:
            return 'Backstabber'
        else:
            return 'b'



    #Team2: Loyal Vengeful
    #This example player is silent at first and then only betrays if they were a sucker last round.
    #######################################


    elif player == 2:
        if getting_team_name:
            return 'Loyal Vengeful'
        else:
            if len(opponent_history)== 0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b'  # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude


    # EACH STUDENT TEAM CAN CHANGE ONE OF THESE elif SEGMENTS OF CODE BELOW
    #######################################################################





    #Team3: Aaron Caltrider
    #######################################


    elif player == 3:
        if getting_team_name:
            return 'Aaron Caltrider'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif len(opponent_history)>=2 and opponent_history[-2]=='b': # If they keep betraying, betray also
                return 'b'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude
















    #Team4: Tom Dau
    #######################################


    elif player == 4:
        if getting_team_name:
            return 'Tom Dau'
        else:
            if len(opponent_history)==0:  #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b'  # betray if they were severely punished last time
            elif history[-1]=='b':
                return 'b'
            elif history[-1]=='b' and opponent_history[-1]=='b':
                return 'c'
            else:
                return 'c'  #otherwise collude















    #Team5: Bryce Getz
    #######################################


    elif player == 5:
        if getting_team_name:
            return 'Bryce Getz'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'c' # lets just be a good friend
            else:
                return 'c' #otherwise collude. we will try to get a good score like this















    #Team6: Ethan Januszewski
    #######################################


    elif player == 6:
        if getting_team_name:
            return 'Ethan Januszewski'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            elif history[-1]=='b':
                return 'b'
            elif history[-1]=='c' and opponent_history[-1]=='c':
                return 'c'
            elif len(opponent_history)==1:
                return 'b'
            else:
                return 'c' #otherwise collude















    #Team7: Gerardo Lopez Santiago
    #######################################


    elif player == 7:
        if getting_team_name:
            return 'Gerardo Lopez Santiago'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'c' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team8: Alex Mears
    #######################################


    elif player == 8:
        if getting_team_name:
            return 'Alex Mears'
        else:
            avgopp = 0
            sumopp = 0
            for i in range(len(opponent_history)):
                sumopp += ord(opponent_history[i])
                avgopp = sumopp / len(opponent_history)
            print(avgopp)
            if len(opponent_history) == 0:                      # It's the first round: collude
                return 'c'
            elif avgopp <= ord("b") + 0.5:
                return 'b'                                      # if opponent on average betrays, then collude
            else:
                return 'c'                                      # otherwise betray









    #Team9: Daniel Mitchell
    #######################################


    elif player == 9:

        if getting_team_name:
            return 'Daniel Mitchell'
        else:
            logic_mode = 1
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1] == 'c' and opponent_history[-1] == 'b': #If I collude and they betray, just go into betrayal mode
                logic_mode = 0
            if logic_mode == 1: #Looks for the ave and colludes if they have more often then not.
                countc = 0
                countb = 0
                for i in opponent_history:
                    if i == "c":
                        countc = countc + 1
                    if i == "b":
                        countb = countb + 1
                if countc >= countb:
                    return 'c' # betray if they were severely punished last time
                elif countb > countc:
                    return 'b' # betray if they were severely punished last time
                else:
                    return 'c' #otherwise collude
            if logic_mode == 0:
                return "b"















    #Team10: Ryan Mullins
    #######################################


    elif player == 10:
        if getting_team_name:
            return 'Ryan Mullins'
        else:
            if len(opponent_history) == 0:
                return 'b'
            elif len(opponent_history) == 1:
                return 'c'
            elif len(opponent_history) == 2:
                return 'c'
            else:
                if opponent_history[-1] == 'c':
                    return 'c'
                else:
                    return 'b'















    #Team11: Ian Neyens
    #######################################


    elif player == 11:
        if getting_team_name:
            return 'Ian Neyens'
        else:
            if len(opponent_history) == 0:  # It's the first round: collude
                return 'c'
            elif opponent_history[-1] == 'b':
                return 'b'
            elif opponent_history[-1] == 'b':
                x = random.randint(1, 2)
                if x == 1:
                    return 'c'
                else:
                    return 'b'
            else:
                return 'c'  # otherwise collude









    #Team12: Jake Perman
    #######################################


    elif player == 12:
        if getting_team_name:
            return 'Jake Perman'

        else:
            # calculate the level of trust with your partner
            def calc_trust():
                # you've known your partner for a while so your base level of trust is pretty good
                t = 70
                # re-evaluate your level of trust each round
                if len(history) <= 7:
                    f = len(history)
                else:
                    f = 7
                for r in range(f):
                    x = r * -1
                    # build trust if you and your partner colluded last round
                    if opponent_history[x] == 'c' and history[x] == 'c':
                        t += 15
                    # your partners betrayal last round shattered your trust
                    elif opponent_history[x] == 'b' and history[x] == 'c':
                        t -= 35
                    # you guys both betrayed each other, no trust is lost or gained
                    elif opponent_history[x] == 'b' and history[x] == 'b':
                        t -= 0
                    # prevent trust from going above 100 or below 0
                if t < 0:
                    t = 0
                elif t > 100:
                    t = 100
                return t

            # calculate the consistency and tendencies of your partner
            def calc_cons():
                c_total = 0  # counter for c's
                b_total = 0  # counter for b's
                consist = 0
                # calculate your partners behavioral tendency towards either collusion or betrayal thus far
                for each in opponent_history:
                    if each == 'c':
                        c_total += 1
                    else:
                        b_total += 1
                if b_total > c_total:  # set the behavioral tendency to whichever has greater count
                    tend = 'b'
                else:
                    tend = 'c'

                # if several rounds have passed, check your partner's recent behavior compared to overall tendency
                if len(history) >= 2:
                    c_total = 0
                    b_total = 0
                    # calculate the recent (last 5 moves) behavioral tendency of your partner
                    for each in opponent_history[-6:-1]:
                        if each == 'c':
                            c_total += 1
                        else:
                            b_total += 1

                    # one set of recency trends is used in early rounds, the other in late
                    if b_total > c_total:
                        if len(history) >= 20:
                            lat_tend = 'b'
                            e_trend = None
                        else:
                            e_trend = 'b'
                            lat_tend = None
                    else:
                        if len(history) >= 20:
                            lat_tend = 'c'
                            e_trend = None
                        else:
                            e_trend = 'c'
                            lat_tend = None
                else:
                    lat_tend = None
                    e_trend = None
                # calculate how consistent your partner is based on recent behavior
                hist = 0
                if len(opponent_history) <= 8:  # set the value testing range based on total length of the list
                    e = len(opponent_history) - 1
                    s = 0
                elif len(opponent_history) > 8:
                    e = (len(opponent_history) - len(opponent_history)) + 8 - 1
                    s = 0
                for i in range(s, e):
                    m = -i
                    n = -i - 1
                    if opponent_history[m] == opponent_history[n]:  # compare adjacent values to each other
                        hist += 1
                if hist >= 5:  # if partner has made the same move 5+ times, they are consistent
                    consist = 100
                elif 5 > hist > 2:  # if partner has made the same move 3 or 4 times, they're somewhat consistent
                    consist = 60
                elif hist == 2:  # if the same move has been made only twice, only slightly consistent
                    consist = 30
                else:  # otherwise they are not consistent at all
                    consist = 0
                # return all the values
                return consist, tend, lat_tend, hist, e_trend

            # keep track of your own tendencies so you can predict your partners reaction
            def my_tend():
                c_tend = 0
                b_tend = 0
                # calculate your own overall tendency towards collusion or betrayal
                for h in history:
                    if h == 'c':
                        c_tend += 1
                    else:
                        b_tend += 1

                if c_tend > b_tend:
                    tend = 'c'
                else:
                    tend = 'b'

                z = 0
                v = []
                # check whether you've fallen into a consistent behavioral pattern
                if len(history) > 6:
                    for x in range(1, 7):
                        if history[-x] == history[-x - 1]:
                            z += 1
                            v.append(history[-x])
                        else:
                            break
                if z >= 4:
                    pattern = True
                else:
                    z = 0
                    pattern = False
                # if you've developed a pattern, which way does it tend towards?
                if pattern:
                    lett = v[0]
                else:
                    lett = 'n'
                return tend, pattern, lett, z

            # once a few rounds have passed, base your decisions off analysis rather than whimsy
            if len(opponent_history) >= 2:
                cons = calc_cons()[0]  # consistency of partner
                en_tend = calc_cons()[1]  # the tendency of your partner
                trust = calc_trust()  # the trust you have with your partner
                if len(history) > 2:
                    m_tend = my_tend()[0]  # overall behavioral tendency of yourself
                    m_patt = my_tend()[1]  # whether you've developed a pattern [T/F]
                    p_trend = calc_cons()[2]  # recent tendencies of your partner
                    let_cons = my_tend()[2]  # if you've developed a pattern, what is it
                    times = my_tend()[3]  # how many times in a row you have made the same move
                    p_hist = calc_cons()[3]  # how many times in a row your partner has made the same move
                    early_trend = calc_cons()[4]  # trend used only in the first 10 or so moves

            if len(
                    opponent_history) <= 2: # No need to betray your partner on your first foray into the world of crime
                if len(history) > 0 and opponent_history[-1] == 'b':
                    return 'b'
                else:
                    return 'c'
            elif 2 < len(history) < 5:  # Run on turns 2 and 3
                # if your partner colluded the first time around, collude with them again
                if opponent_history[0] == 'b':
                    return 'b'
                elif opponent_history[-1] == 'c':
                    return 'c'
                elif opponent_history[-1] == 'b':
                    return 'b'
                else:
                    return 'c'
            # elif len(history) == 7 and history[4] == 'b':
            #     return 'b'
            zed = len(history)
            # if 6 rounds have passed and your partner has trended towards betrayal for five rounds, run this
            if 9 > len(history) >= 6 and p_hist >= 5 and p_trend == 'b':
                if m_patt is True and let_cons == 'c':  # if you've developed a pattern of collusion
                    return 'b'
                else:  # if your partner and you have been betraying each other, try colluding
                    return 'c'
            # if in the first few rounds you betray; make ammends and collude
            elif 5 >= len(history) > 3 and history[-2] == 'b' and opponent_history[-1] != 'b':
                return 'c'
            elif p_trend == 'b' and let_cons == 'c':
                return 'b'
            # between rounds 20 and 35, develop sporadic behavior to throw your partner off your trail and gather info
            if 35 > len(history) > 20 and cons != 100:
                if en_tend == 'c' and trust >= 80:  # you've built up good trust, and your partner tended to collusion
                    if opponent_history[-1] != 'b':
                        return 'c'  # 25% chance of betrayal, 75% chance of collusion
                    else:
                        return 'b'
                elif en_tend == 'c' and 50 < trust < 80:  # overall tendency towards collusion, but trust isn't high
                    if opponent_history[-1] != 'b':  # if your partner didn't betray you last round
                        if times <= 3:  # if you haven't developed a behavioral pattern, collude with your partner
                            return 'c'
                        else:  # betray your partner if you've become too predictable
                            return 'b'
                    else:
                        return 'b'
                else:  # if your partner has been trending towards betrayal, betray them back
                    return 'b'
            # run if partners consistency is only 30
            elif cons == 30 and len(history) > 5:
                if en_tend == 'c':  # partner has tended towards collusion, but is inconsistent overall
                    num = random.randint(1, 3)  # randomly pick a number, if 2 collude, otherwise betray
                    if num == 2:
                        return 'c'
                    else:
                        return 'b'
                # if your partner has been inconsistent and trended towards betrayal; betray them
                else:
                    return 'b'
            # run if partner's consistency is 60
            elif cons == 60:
                if en_tend == 'b':  # if your partner has been somewhat consistently betraying you; betray them back
                    if history[-1] == 'b' and opponent_history[-1] == 'c':
                        return 'b'
                    elif history[-1] == 'c' and opponent_history[-1] == 'c':
                        return 'c'
                    else:
                        return 'b'
                # if your partner has been somewhat consistent with collusion
                elif en_tend == 'c':  # collude only if you haven't became too predictable
                    if history[-1] == 'b' and opponent_history[-1] == 'c':
                        return 'b'
                    elif p_trend == 'c' or early_trend == 'c':  # their recent trend has been to collude; betray them
                        if opponent_history[-1] == 'c':
                            return 'c'
                        else:
                            return 'b'
                    elif p_hist > 3 and opponent_history[-1] == 'b':
                        return 'b'
                    elif let_cons == 'c':  # you've developed a pattern of collusion, your partner has not; betray them
                        return 'b'
                    else:
                        return 'c'
                # will probably never run, but just in case, collude with them
                else:
                    return 'c'
            # if the partner has 100 consistency; run this
            elif cons == 100:
                if opponent_history[-1] == 'c' and history[-1] == 'b':
                    for each in history:
                        if each == 'b' and opponent_history[history.index(each)] == 'c' and len(
                                history) - 1 != history.index(each):
                            if opponent_history[history.index(each) + 1] == 'b':
                                return 'b'
                            else:
                                return 'c'
                    return 'b'
                # if you and your partner haven't betrayed each other in a while; betray them and make a quick buck
                elif p_trend == 'c' and times == 6 or early_trend == 'c' and times == 6:  # don't be too predictable
                    if opponent_history[-1] != 'b':
                        for each in history:
                            x = history.index(each)
                            if each == 'b' and opponent_history[x] == 'c' and len(history) - 1 != x:
                                if opponent_history[x + 1] == 'b':
                                    return 'b'
                                else:
                                    return 'c'
                        return 'c'
                    else:
                        return 'b'
                elif early_trend == 'b' and len(
                        history) == 6:  # if your partners early game trend has been betrayal; try colluding
                    return 'c'
                # if your partner hasn't betrayed you too recently, but you have  betrayed them; consider gaining trust
                elif opponent_history[-1] == 'c' and opponent_history[-2] == 'c' and history[-1] == 'b':
                    return 'b'
                # if enemy has consistently tended towards collusion; continue to collude
                elif en_tend == 'c' and p_trend == 'c' or early_trend == 'c':
                    if opponent_history[-1] != 'b':
                        return 'c'
                    else:
                        return 'b'
                elif m_patt is True and let_cons == 'b' and opponent_history[
                    0] != 'b':  # if you've developed a patter of betrayal; try colluding
                    return 'b'
                # if your partner has consistently betrayed you; betray them back
                else:
                    return 'b'
            # if your partner hasn't been consistent, but you have some trust, maybe give them a chance to build trust
            elif cons == 0:
                if opponent_history[-1] == 'c' and history[-1] == 'b':
                    for each in history:
                        if each == 'b' and opponent_history[history.index(each)] == 'c' and len(
                                history) - 1 != history.index(each):
                            if opponent_history[history.index(each) + 1] == 'b':
                                return 'b'
                            else:
                                return 'c'
                    return 'b'
                if opponent_history[-1] == 'b' and history[-2] == 'b':
                    return 'c'
                elif trust >= 50:
                    ch = random.choices(['c', 'b'], [2, 4], k=1)[
                        0]  # twice the odds of betrayal rather than collusion
                    zed += 0
                    return ch
                # if there's been low consistency and trust, betray your partner
                elif trust < 30:
                    return 'b'
                else:  # when all else fails, randomly decide whether to betray or collude
                    zed += 0
                    return 'c'
            else:
                return 'c'















    #Team13: Joe Schmidt
    #######################################


    elif player == 13:
        if getting_team_name:
            return 'Joe Schmidt'
        else:
            ctotal = 0
            if len(opponent_history) == 0:  # It's the first round: collude
                return 'c'
            else:
                sanity = True
                if opponent_history[-1] == 'b' and random.randint(0, 20) == 0:
                        sanity = False   # This bitter betrayal has shown me how worthless and petty humanity truly is
                for i in opponent_history:      # tests if psychopathic tendencies have been enabled
                    if i == 'C' or i == 'B':
                        sanity = False
                if sanity:
                    total = len(opponent_history)
                    for i in opponent_history:          # calculates trust level based on average opponent action
                        if i == "c":
                            ctotal += 1
                    trust = (ctotal / total) * 100
                    if trust > 80:                      # makes a decision based on level of trust
                        return 'c'
                    elif trust > 70:
                        if opponent_history[-1] == 'b':
                            if random.randint(0, 4) == 0:
                                return 'b'
                            else:
                                return 'c'
                        else:
                            return 'c'
                    elif trust > 40:
                        if opponent_history[-1] == 'b':
                            return 'b'
                        else:
                            return 'c'
                    elif trust > 20:
                        if opponent_history[-1] == 'c':
                            if random.randint(0, 2) == 0:
                                return 'b'
                            else:
                                return 'c'
                        else:
                            return 'b'
                    elif trust > 10:
                        if opponent_history[-1] == 'c':
                            if random.randint(0, 4) == 1:
                                return 'c'
                            else:
                                return 'b'
                        else:
                            return 'b'
                    else:
                        if opponent_history[-1] == 'c':
                            if random.randint(0, 10) == 0:
                                return 'c'
                            else:
                                return 'b'
                        else:
                            return 'b'
                else:
                    if random.randint(0, 2) == 1:           # humanity is not worth the effort of a calculated decision
                        return 'C'
                    else:
                        return 'B'














    #Team14: Bawi Thawng
    #######################################


    elif player == 14:
        if getting_team_name:
            return 'Bawi Thawng'
        else:
            if len(opponent_history) == 0:  #It's the first round: collude
                return 'c'
            elif history[-1] == 'c' and opponent_history[-1]=='b':
                return 'b'  # betray if they were severely punished last time
            elif history[-1] == 'b' and opponent_history[-1] == 'b':
                return 'b'
            elif opponent_history[-1] == 'c':
                return 'b'
            else:
                return 'b'  #otherwise collude















    #Team15: Jacob Walters
    #######################################


    elif player == 15:
        if getting_team_name:
            return 'Jacob Walters'
        else:
            if len(opponent_history)==0:
                return 'c'
            elif opponent_history[-1]=='b':
                return 'b'
            else:
                return 'c'















    #Team16: Ryan Muetzel
    #######################################


    elif player == 16:
        if getting_team_name:
            return 'Ryan Muetzel'
        else:
            if len(opponent_history) == 4:      # if it is still the first few rounds then do vengeance thingy
                if len(opponent_history) == 0:        # It's the first round: collude
                    return 'c'
                elif opponent_history[-1] == 'b':
                    return 'b'          # betray if they were severely punished last time
                else:
                    return 'c'          # otherwise collude
            else:
                count_c = 0
                for i in range(len(opponent_history)):  # find how many times opponent back stabbed
                    if opponent_history[i] == 'c':
                        count_c += 1
                if (count_c + 1) / (len(opponent_history) + 1) > .65:
                    return 'c'
                else:
                    return 'b'





    #Team17: Geni Williams
    #######################################


    elif player == 17:
        if getting_team_name:
            return 'Geni Williams'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif opponent_history[-1]=='b':
                return 'b' # betray if they betrayed
            elif history[-1]=='c' and opponent_history[-1]=='c':
                return 'c' # collude if we both collude
            else:
                return 'c' #otherwise collude















    #Team18: Enter Team Name Here
    #######################################


    elif player == 18:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history) == 0:  #It's the first round: collude
                return 'c'
            elif history[-1] == 'c' and opponent_history[-1] == 'b':
                return 'b'  # betray if they were severely punished last time
            elif history[-1] == 'c' and opponent_history[-1] == 'c':
                return 'b'
            elif opponent_history[-1] == 'b' and history[-1] == 'b':
                return 'b'
            else:
                return 'c'  #otherwise collude















    #Team19: Enter Team Name Here
    #######################################


    elif player == 19:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude















    #Team20: Enter Team Name Here
    #######################################


    elif player == 20:
        if getting_team_name:
            return 'Enter Team Name Here'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray if they were severely punished last time
            else:
                return 'c' #otherwise collude












def play_tournament(num_players):
    #create a list of zeros, one per player
    scores = []
    for i in range(num_players):
        scores += [0]


    ''' Get the team name from each team algorithm'''
    #create a list of the right length
    team_names = list(range(num_players))
    for player in range(num_players):
        team_names[player] = get_action(player,'','',0,0,getting_team_name=True)

    # each element will become a column for each player
    # range is just to get list of correct size
    result_table=list(range(num_players))
    moves_table=list(range(num_players))


    for player1 in range(num_players):
        # create the column for each player
        # range just to get list of correct size
        result_table[player1]=list(range(num_players))
        result_table[player1][player1]=0 # initialize unused diagonal to 0
        moves_table[player1]=list(range(num_players))
        # play a game between with every other player of lower number
        for player2 in range(player1):
            moves1, moves2, score1, score2 = \
                play_iterative_rounds(player1, player2)

            rounds = len(moves1)
            score1_per_round = score1/rounds
            score2_per_round = score2/rounds

            result_table[player1][player2]=score1_per_round
            result_table[player2][player1]=score2_per_round

            moves_table[player1][player2] = moves1
            moves_table[player2][player1] = moves2

            #accumulate the results for the two players
            scores[player1] += score1*1.0/len(moves1)#ends up same as column sum
            scores[player2] += score2*1.0/len(moves2)#ends up same as column sum

    '''report round-level results in a data file'''
    use_datafile=True
    if use_datafile:
        # use the same directory as the python script
        import os.path
        directory = os.path.dirname(os.path.abspath(__file__))

        #name the file tournament.txt
        filename = os.path.join(directory, 'tournament.txt')
        #create the file for the round-by-round results
        results = open(filename,'w')
        for player1 in range(num_players):
            for player2 in range(player1):
                # store the results in the file
                #title by team numbers
                results.write('team ' + str(player1) +
                              ' vs. ' + 'team ' + str(player2) +'\n')
                #title by player-on-player average score
                results.write(str(result_table[player1][player2]) +
                              ' vs. ' + str(result_table[player2][player1])+'\n')
                #title by team names
                results.write(team_names[player1] +
                             ' vs. ' + team_names[player2] + '\n')
                #show the moves, aligned vertically
                results.write(moves_table[player1][player2] +'\n')
                results.write(moves_table[player2][player1] +'\n')
                #blank line between each pair's results
                results.write('\n')

        #at the bottom repeat the output that was sent to the screen
        #print a title for the table
        results.write('\n\n\n\tEach column shows score earned per round against each other player.\n\n\n')
        #print header line
        results.write('\t') #skip 1st column
        for player1 in range(num_players):
            results.write('P'+str(player1)+'\t') # label each additional column
        results.write('\n')

        #print each player's scores
        for player2 in range(num_players):
            results.write('P'+str(player2)+'\t') #label the player's row
            for player1 in range(num_players):
                #print score against each other player
                results.write(str(result_table[player1][player2])+'\t')
            results.write('\n')
        results.write('Total:\t')
        for player1 in range(num_players):
            results.write(str(int(scores[player1]))+'\t')
        results.write('\n\n\n Average per round, with team strategy names:\n\n')

        #print team ids, total scores, and names
        for player in range(num_players):
            results.write('player ' + str(player) + ': ' + \
                    str(int(scores[player])/num_players) + ' points: '+\
                    team_names[player]+'\n')


        #append the file showing algorithms
        results.write('\n\n' + '-'*79 + '\n' + \
                    'Here is the code that produced this data:\n\n')
        this_code_file = open(__file__, 'r')
        for line in this_code_file:
            results.write(line)

    '''report the results on screen'''
    #print a title for the table
    print('\n\n\tEach column shows score earned per round against each other player.\n\n')

    #print header line
    print('\t', end='') #skip 1st column
    for player1 in range(num_players):
        print('P',player1, end='\t') # label each additional column
    print()

    #print each player's scores
    for player2 in range(num_players):
        print('P',player2, end='\t') #label the player's row
        for player1 in range(num_players):
            #print score against each other player
            print("{:.2f}".format(result_table[player1][player2]), end='\t')
        print()
    #print row of total scores
    print('Total:\t',end='')
    for player1 in range(num_players):
        print(str("{:.2f}".format(scores[player1])),end='\t')

    print('\n\n\n Average per round, with team strategy names:\n\n')
    #print team ids, total scores, and names
    for player in range(num_players):
        print('player ' + str(player) , ': ' ,
               str("{:.2f}".format((scores[player])/num_players)) , ' points: ',
               team_names[player])
def main():
    howmanyteams=int(input("How many teams do you want to run in this tournament? Max:20  "))
    howmanyteams+=1
    if howmanyteams>21:
        play_tournament(21)
    else:
        play_tournament(howmanyteams)

if __name__=="__main__":
    main()
