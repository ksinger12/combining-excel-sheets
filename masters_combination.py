import pandas as pd

NUMBER_OF_TEAMS = 2

dummy_frame = pd.read_excel('Team_0.xlsx')
real_frame = dummy_frame.drop(dummy_frame.columns[0], axis=1)
real_frame.index = ['Player 1', 'Player 2', 'Player 3',
                    'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8']

for i in range(1, NUMBER_OF_TEAMS):
    sheet = 'Team_'+str(i)+'.xlsx'

    dummy_frame = pd.read_excel(sheet)
    dummy_frame = dummy_frame.drop(dummy_frame.columns[0], axis=1)
    dummy_frame.index = ['Player 1', 'Player 2', 'Player 3',
                         'Player 4', 'Player 5', 'Player 6', 'Player 7', 'Player 8']

    frame = [real_frame, dummy_frame]
    real_frame = pd.concat(frame, axis=1)

real_frame.to_csv(r"./Masters_Sheet.csv")
