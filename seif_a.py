import random
import sys
import tkinter as tk

import numpy as np


# INPUT L P
class InputWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Please Insert the Next Values")
        self.geometry("400x300")

        self.p_label = tk.Label(self, text="P:")
        self.p_label.pack()

        self.p_entry = tk.Entry(self)
        self.p_entry.pack()

        self.l_label = tk.Label(self, text="L:")
        self.l_label.pack()

        self.l_entry = tk.Entry(self)
        self.l_entry.pack()

        self.s1_label = tk.Label(self, text="S1:")
        self.s1_label.pack()

        self.s1_entry = tk.Entry(self)
        self.s1_entry.pack()

        self.s2_label = tk.Label(self, text="S2:")
        self.s2_label.pack()

        self.s2_entry = tk.Entry(self)
        self.s2_entry.pack()

        self.s3_label = tk.Label(self, text="S3:")
        self.s3_label.pack()

        self.s3_entry = tk.Entry(self)
        self.s3_entry.pack()

        self.s4_label = tk.Label(self, text="S4:")
        self.s4_label.pack()

        self.s4_entry = tk.Entry(self)
        self.s4_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.p = None
        self.l = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.s4 = None

    def submit(self):
        self.p = float(self.p_entry.get())
        self.l = int(self.l_entry.get())
        self.s1 = float(self.s1_entry.get())
        self.s2 = float(self.s2_entry.get())
        self.s3 = float(self.s3_entry.get())
        self.s4 = float(self.s4_entry.get())
        self.quit()


if __name__ == "__main__":
    input_window = InputWindow()
    input_window.mainloop()


# create a class that contains the cell
class cell():
    def __init__(self, x, y, cell_class, is_person=False, bit=0):
        self.x = x
        self.y = y
        self.cell_class = cell_class
        self.is_person = False
        self.bit = 0

    def get_cell_class(self):
        return self.cell_class

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_bit(self, bit):
        self.bit = bit

    def get_bit(self):
        return self.bit

    def get_is_person(self):
        return self.is_person

    def set_is_person(self, is_person):
        self.is_person = is_person


#  the function determines the cells randomly in the grid
def initialize_grid(width, height, cell_types):
    grid = []
    cell_type = "s1"
    # define the probabilities of the classes from the input window
    for i in range(height):
        row = []
        for j in range(width):
            # assign a class by the probabilities
            class_prob_sum = 0
            rand_num = random.random()
            # go over the keys of the dictionary cell_types
            for class_name in cell_types:
                # assign a class by the probabilities
                class_prob_sum += cell_types[class_name]
                if rand_num < class_prob_sum:
                    cell_type = class_name
                    break
            # create a new cell and append it to the row
            new_cell = cell(i, j, cell_type)
            row.append(new_cell)
        grid.append(row)
    return grid


#  the function determines the cells randomly to be 1 in the initial grid
# if the cell is labeled 1, that means the cell is colored
def randomize_grid():
    # initiation of the grid that will contain a 2D of cells
    class_probs = {"S1": input_window.s1, "S2": input_window.s2, "S3": input_window.s3, "S4": input_window.s4}
    grid = initialize_grid(GRID_SIZE, GRID_SIZE, class_probs)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if random.random() < input_window.p:
                grid[x][y].set_is_person(True)
            else:
                grid[x][y].set_is_person(False)

    # pick a random cell to start spreading the rumor and make shore it is a person!
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y].get_is_person():
            grid[x][y].set_bit(1)
            break
    return grid


# Set up the size of the grid
GRID_SIZE = 100


# Define the rules of the cellular automaton
def update_cells(grid, spread_grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if not grid[x][y].get_is_person:
                continue
            if grid[x][y].get_bit == 1:
                grid[x][y].set_bit(1)
                continue
            # get the neighbors of the cell
            neighbors = get_neighbors(grid, x, y)
            if len(neighbors) == 0:
                continue

            cell_class = grid[x][y].get_cell_class()
            # if the cell is s1 it will spread the rumor
            if cell_class == "S1":
                for n in neighbors:
                    # if one neighbor is 1,and it has never spread a rumor  than the cell will be 1
                    if n.get_bit() == 1 and spread_grid[x][y] == 0:
                        # update the spread grid
                        spread_grid[x][y] = 1
                        grid[x][y].set_bit(1)
            # s2 will spread the rumor with a 67% chance
            elif cell_class == "S2":
                counter = 0
                if random.random() < 0.67:
                    for n in neighbors:
                        if n.get_bit() == 1 and spread_grid[x][y] == 0:
                            counter += 1
                    # it behaves like s1 if the rumor is from 2 different neighbors
                    if counter == 2 or counter == 1:
                        spread_grid[x][y] = 1
                        grid[x][y].set_bit(1)
                else:
                    if grid[x][y].get_bit() == 0:
                        grid[x][y].set_bit(0)
                # s3 will spread the rumor with a 33% chance
            elif cell_class == "S3":
                counter = 0
                if random.random() < 0.33:
                    for n in neighbors:
                        if n.get_bit() == 1 and spread_grid[x][y] == 0:
                            counter += 1
                            # it behaves like s2 if the rumor is from 2 different neighbors
                            if counter == 2:
                                if random.random() < 0.67:
                                    spread_grid[x][y] = 1
                                    grid[x][y].set_bit(1)
                    if counter == 1:
                        spread_grid[x][y] = 1
                        grid[x][y].set_bit(1)
                else:
                    if grid[x][y].get_bit() == 0:
                        grid[x][y].set_bit(0)
            # s4 will never spread the rumor
            elif cell_class == "S4":
                counter = 0
                for n in neighbors:
                    if n.get_bit() == 1 and spread_grid[x][y] == 0:
                        counter += 1
                if counter == 2:
                    # it behaves like s3 if the rumor is from 2 different neighbors
                    if random.random() < 0.33:
                        spread_grid[x][y] = 1
                        grid[x][y].set_bit(1)
                if counter == 1 and grid[x][y].get_bit() == 0:
                    grid[x][y].set_bit(0)
    return grid


#  get the class of the cell
def get_cell_class(cell_types, x, y):
    return cell_types[(x, y)]


#  get the neighbors of the cell
def get_neighbors(grid, x, y):
    neighbors = []
    nrows = len(grid)
    ncols = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Skip the cell at (x, y)
            if i == 0 and j == 0:
                continue
            nx = x + i
            ny = y + j
            # Wrap around the edges of the grid
            if nx < 0:
                nx += nrows
            elif nx >= nrows:
                nx -= nrows
            if ny < 0:
                ny += ncols
            elif ny >= ncols:
                ny -= ncols
            # Add the neighbor to the list
            if grid[x][y].get_is_person() and grid[nx][ny].get_is_person():
                neighbors.append(grid[nx][ny])
    return neighbors


def update_spread_grid(spread_grid, rumor_spread_time_grid):
    # go through the grid and update the spread grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if spread_grid[i][j] == 1:
                # if the cell is already colored, then the rumor_spread_time_grid will be updated
                rumor_spread_time_grid[i][j] += 1
            # if the rumor_spread_time_grid is greater than the input window, then the cell will be able to spread
            # the rumor again
            if rumor_spread_time_grid[i][j] >= input_window.l:
                spread_grid[i][j] == 0
                rumor_spread_time_grid[i][j] = 0
    return spread_grid, rumor_spread_time_grid


import matplotlib.pyplot as plt


def create_png(generations, infected_cells):
    """
    Creates a PNG image with a line plot of the number of infected cells over time (generations).

    :param generations: A list of integers representing the number of generations that have passed.
    :param infected_cells: A list of integers representing the number of infected cells at each generation.
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    ax.plot(generations, infected_cells)
    ax.set_xlabel("Generations")
    ax.set_ylabel("Number of Cells that received the rumor")
    ax.set_title("Number of Cells that received the rumor Over Time")
    plt.savefig("infected_cells_over_time.png")


def run_program(grid, infected_cells_over_time):
    # Create the GUI window
    window = tk.Tk()
    window.title("Cellular Automaton")

    # Create the canvas to draw the grid
    canvas = tk.Canvas(window, width=1000, height=1000, borderwidth=0, highlightthickness=0, bg='white')
    canvas.pack(side="top", fill="both", expand="true")

    # Create the initial grid with random cells
    spread_grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    rumor_spread_time_grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

    # Define the function to update the grid and redraw it on the canvas
    def update():
        nonlocal grid
        nonlocal spread_grid
        nonlocal rumor_spread_time_grid
        nonlocal generation
        infected_cells = 0

        # We would like to update the grid as many times as the variable "generations" is set to
        if generation >= 300:
            print("done")
            return

        # Update the grid by the spreading of the rumor rules
        # change the new grid to be the updated grid according to the new bits of the cells
        new_grid = update_cells(grid, spread_grid)
        grid = new_grid

        # loop through the grid and update each cell based on its class and its neighbors
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grid[x][y].get_bit() == 1:
                    infected_cells += 1

        print("The number of cells that are infected is: ", infected_cells)
        #  a function that updates the spread grid due to the number of generations that passed
        new_spread_grid, new_rumor_spread_time_grid = update_spread_grid(spread_grid, rumor_spread_time_grid)
        spread_grid = new_spread_grid
        rumor_spread_time_grid = new_rumor_spread_time_grid
        # reset the grid
        canvas.delete("rect")
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grid[x][y].is_person and grid[x][y].get_bit() == 0:
                    canvas.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="green", outline="white",
                                            tags="rect")
                elif grid[x][y].is_person and grid[x][y].get_bit() == 1:
                    canvas.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="red", outline="white",
                                            tags="rect")
                else:
                    canvas.create_rectangle(x * 10, y * 10, x * 10 + 10, y * 10 + 10, fill="gray", outline="white",
                                            tags="rect")
        generation += 1

        # Draw grid lines
        for x in range(0, 1000, 10):
            canvas.create_line(x, 0, x, 1000, fill="#f0f0f0")
        for y in range(0, 1000, 10):
            canvas.create_line(0, y, 1000, y, fill="#f0f0f0")
        # Call the update function again after 100 milliseconds
        window.after(100, update)
        # update the infected_cells_over_time dictionary
        infected_cells_over_time[generation] = infected_cells

    # Start the update loop
    generation = 0
    update()
    # close the input window
    input_window.destroy()

    # Start the main loop of the GUI
    window.mainloop()

    return infected_cells_over_time


def main():
    grid = randomize_grid()
    # creat a dictionary that will hold the number of generations and the number of infected cells
    generations = []
    infected_cells = []
    # combine the two lists into a dictionary
    infected_cells_over_time = dict(zip(generations, infected_cells))
    new_infected_cells_over_time = run_program(grid, infected_cells_over_time)
    create_png(list(new_infected_cells_over_time.keys()), list(new_infected_cells_over_time.values()))
    sys.exit()


# Call the main function to start the program
if __name__ == "__main__":
    main()
