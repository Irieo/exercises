# Lists | Slices | Functions
# Built-in Functions
# https://docs.python.org/3/library/functions.html
# https://www.youtube.com/watch?v=8YbIwueDQx4

game = [[0,0,0],
		[0,0,0],
		[0,0,0]]


def game_board():
	print('   a  b  c')       
	for count, row in enumerate(game):
		print(count, row)
		#for item in row:


game_board()

game[0][1] = 'x'

game_board()