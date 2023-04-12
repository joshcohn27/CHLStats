import sys, csv

FILENAME = "stats.csv"

def read_file():
    with open(FILENAME) as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)
    
data = read_file()

def write():
    with open(FILENAME, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def update(name, goal = False):
    for row in data:
        if row[0] == name:
            if goal:
                row[1] = int(row[1]) + 1
            else:
                row[2] = int(row[2]) + 1
            row[3] = int(row[3]) + 1

def reset():
    for row in data:
        if row[0] == "Camper":
            continue
        row[1] = 0
        row[2] = 0
        row[3] = 0
    write()
    print("Successfully reset")
    
def sort_by_points(row):
    return int(row[3])

def print_stats():
    sorted_data = sorted(data[1:], key=sort_by_points, reverse=True)
    print(data[0][0], data[0][1], data[0][2], data[0][3], sep='\t\t|\t', end='\t|\n')
    print("--------------------------------------------------------------------------------")
    
    for row in sorted_data:
        print(row[0], row[1], row[2], row[3], sep='\t\t|\t', end='\t|\n')
        print("--------------------------------------------------------------------------------")
    
def run():
    if (len(sys.argv) < 2):
        print_stats()
        return
    
    update(sys.argv[1], True)
    
    if (len(sys.argv) >= 3):
        update(sys.argv[2])
        
    if (len(sys.argv) >= 4):
        update(sys.argv[3])
        
    write()
    print("Sheet Updated")

def main():
    # reset()
    run()
    
    
    
if __name__ == '__main__':
    main()