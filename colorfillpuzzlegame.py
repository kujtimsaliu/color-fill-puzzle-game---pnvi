import pygame
import random
import sys
from pygame import gfxdraw

pygame.init()

WINDOW_SIZE = 800  
GRID_SIZE = 5
CELL_SIZE = 80    
GRID_OFFSET_X = (WINDOW_SIZE - (GRID_SIZE * CELL_SIZE)) // 2
GRID_OFFSET_Y = 50  
COLORS = [(255, 0, 0),    # Red
          (0, 255, 0),    # Green
          (0, 0, 255),    # Blue
          (255, 255, 0)]  # Yellow
COLOR_NAMES = ["Red", "Green", "Blue", "Yellow"]

# Set up the display
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Color Fill Puzzle')

pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)
SMALL_FONT = pygame.font.SysFont('Arial', 18)

class ColorFillGame:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected_color = 0
        self.moves = 0
        self.start_time = pygame.time.get_ticks()
        self.game_complete = False
        self.hint_mode = False
        self.undo_stack = []
        self.score = 0
        self.best_score = float('inf')
    
    def reset_game(self):
        self.__init__()
    
    def undo_move(self):
        if self.undo_stack:
            row, col, prev_color = self.undo_stack.pop()
            self.grid[row][col] = prev_color
            self.moves -= 1
    
    def is_valid_move(self, row, col, color):
        if self.grid[row][col] == color:
            return False
            
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                if self.grid[new_row][new_col] == color:
                    return False
        return True
    
    def get_valid_colors(self, row, col):
        valid_colors = []
        for color in COLORS:
            if self.is_valid_move(row, col, color):
                valid_colors.append(color)
        return valid_colors
    
    def try_place_color(self, row, col):
        if not self.game_complete:
            current_color = self.grid[row][col]
            if self.is_valid_move(row, col, COLORS[self.selected_color]):
                self.undo_stack.append((row, col, current_color))
                self.grid[row][col] = COLORS[self.selected_color]
                self.moves += 1
                if self.is_complete():
                    self.game_complete = True
                    elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
                    self.score = self.moves + elapsed_time
                    self.best_score = min(self.best_score, self.score)
                return True
        return False
    
    def is_complete(self):
        return all(all(cell is not None for cell in row) for row in self.grid)
    
    def draw(self, screen):
        title = FONT.render("Color Fill Puzzle", True, (0, 0, 0))
        screen.blit(title, (WINDOW_SIZE//2 - title.get_width()//2, 10))
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = GRID_OFFSET_X + col * CELL_SIZE
                y = GRID_OFFSET_Y + row * CELL_SIZE
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                
                if self.grid[row][col]:
                    pygame.draw.rect(screen, self.grid[row][col], rect)
                else:
                    pygame.draw.rect(screen, (240, 240, 240), rect)
                
                if self.hint_mode and not self.grid[row][col]:
                    valid_colors = self.get_valid_colors(row, col)
                    hint_text = str(len(valid_colors))
                    hint_surface = SMALL_FONT.render(hint_text, True, (100, 100, 100))
                    screen.blit(hint_surface, (x + CELL_SIZE//2 - hint_surface.get_width()//2, 
                                            y + CELL_SIZE//2 - hint_surface.get_height()//2))
                
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
        
        palette_y = GRID_OFFSET_Y + GRID_SIZE * CELL_SIZE + 50
        for i, (color, name) in enumerate(zip(COLORS, COLOR_NAMES)):
            center_x = WINDOW_SIZE // 2 + (i - len(COLORS)/2 + 0.5) * 100
            
            # Draw color circle
            if i == self.selected_color:
                radius = 25
                pygame.draw.circle(screen, (0, 0, 0), (int(center_x), palette_y), radius + 2)
            else:
                radius = 20
            pygame.draw.circle(screen, color, (int(center_x), palette_y), radius)
            
            name_surface = SMALL_FONT.render(name, True, (0, 0, 0))
            screen.blit(name_surface, (center_x - name_surface.get_width()//2, palette_y + 30))
        
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        stats_y = palette_y + 80
        
        moves_text = f"Moves: {self.moves}"
        time_text = f"Time: {elapsed_time}s"
        moves_surface = FONT.render(moves_text, True, (0, 0, 0))
        time_surface = FONT.render(time_text, True, (0, 0, 0))
        
        screen.blit(moves_surface, (20, stats_y))
        screen.blit(time_surface, (20, stats_y + 30))
        
        button_y = stats_y
        buttons = [
            ("Toggle Hints (H)", self.hint_mode),
            ("Undo (U)", bool(self.undo_stack)),
            ("Reset (R)", True)
        ]
        
        for i, (text, active) in enumerate(buttons):
            color = (0, 0, 0) if active else (150, 150, 150)
            button_surface = FONT.render(text, True, color)
            screen.blit(button_surface, (WINDOW_SIZE - button_surface.get_width() - 20, 
                                       button_y + i * 30))
        
        if self.game_complete:
            complete_text = f"Puzzle Complete! Score: {self.score} (Best: {self.best_score})"
            complete_surface = FONT.render(complete_text, True, (0, 128, 0))
            screen.blit(complete_surface, 
                       (WINDOW_SIZE//2 - complete_surface.get_width()//2, 
                        WINDOW_SIZE - 50))

def main():
    game = ColorFillGame()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                palette_y = GRID_OFFSET_Y + GRID_SIZE * CELL_SIZE + 50
                if palette_y - 30 <= y <= palette_y + 30:
                    for i in range(len(COLORS)):
                        center_x = WINDOW_SIZE // 2 + (i - len(COLORS)/2 + 0.5) * 100
                        if center_x - 30 <= x <= center_x + 30:
                            game.selected_color = i
                
                grid_x = (x - GRID_OFFSET_X) // CELL_SIZE
                grid_y = (y - GRID_OFFSET_Y) // CELL_SIZE
                if (0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE and
                    GRID_OFFSET_X <= x <= GRID_OFFSET_X + GRID_SIZE * CELL_SIZE and
                    GRID_OFFSET_Y <= y <= GRID_OFFSET_Y + GRID_SIZE * CELL_SIZE):
                    game.try_place_color(grid_y, grid_x)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    game.hint_mode = not game.hint_mode
                elif event.key == pygame.K_u:
                    game.undo_move()
                elif event.key == pygame.K_r:
                    game.reset_game()
        
        screen.fill((255, 255, 255))
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()