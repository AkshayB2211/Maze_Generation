
import pygame
import random

# game constants
WIDTH = 480
HEIGHT = 480
FPS = 1

size = 48
cols = WIDTH//size
rows = WIDTH//size

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.visited = False
		self.walls = {'top':True, 'right':True, 'bottom':True, 'left':True}

	def break_walls(self, other):
		if other.x < self.x :
			self.walls['left'] = False
			other.walls['right'] = False

		if other.x > self.x :
			self.walls['right'] = False
			other.walls['left'] = False

		if other.y < self.y :
			self.walls['top'] = False
			other.walls['bottom'] = False

		if other.y > self.y :
			self.walls['bottom'] = False
			other.walls['top'] = False


	def draw(self, screen):
		if self.visited:
			pygame.draw.rect(screen, PINK, (self.x, self.y, size, size))

		t = 4		# thickness of line
		if self.walls['top']:
			pygame.draw.line(screen, BLACK, (self.x, self.y),(self.x+size, self.y), t)
		if self.walls['right']:
			pygame.draw.line(screen, BLACK, (self.x+size, self.y),(self.x+size, self.y+size), t)
		if self.walls['bottom']:
			pygame.draw.line(screen, BLACK, (self.x+size, self.y+size),(self.x, self.y+size), t)
		if self.walls['left']:
			pygame.draw.line(screen, BLACK, (self.x, self.y+size),(self.x, self.y), t)


# return a valid neighbor cell
def next_cell(current, grid):
	i = current.x//size
	j = current.y//size

	opt = []
	# add to the list if cell is not visited
	# and also taking care of edge cases
	if i < rows-1 and not grid[i+1][j].visited:
		opt.append(grid[i+1][j])

	if i > 0 and not grid[i-1][j].visited:
		opt.append(grid[i-1][j])

	if j < cols-1 and not grid[i][j+1].visited:
		opt.append(grid[i][j+1])

	if j > 0 and not grid[i][j-1].visited:
		opt.append(grid[i][j-1])

	try:
		return random.choice(opt)
	except:
		return None



def main():
	# initialize pygame and create window
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Maze Generator")
	clock = pygame.time.Clock()

	grid = []
	for i in range(rows):
		grid.append([])
		for j in range(cols):
			grid[i].append(Cell(i*size, j*size))

	current = grid[0][0]			# grid[col][row]
	current.visited = True
	# current = grid[5][5]
	# next_ = grid[5][4]
	# current.break_walls(next_)

	# Game loop
	running = True
	while running:
		# Process input (events)
		for event in pygame.event.get():
			# check for closing window
			if event.type == pygame.QUIT:
				running = False

		# Update
		next_ = next_cell(current, grid)
		if next_:
			print(current.x, current.y)
			print(next_.x, next_.y)
			current.break_walls(next_)
			current = next_
			current.visited = True

		# Draw / render
		screen.fill(WHITE)
		for i in range(rows):
			for j in range(cols):
				grid[i][j].draw(screen)
		pygame.display.flip()
		clock.tick(FPS)

	pygame.quit()

if __name__ == '__main__':
	main()
