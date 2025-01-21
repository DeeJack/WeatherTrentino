import os

def waste_matching():
    differentiated = "./Data/waste_differentiated.csv"
    undifferentiated = "./Data/waste_undifferentiated.csv"
    output = "./Data/waste.csv"

    with open(differentiated, "r") as d, open(undifferentiated, "r") as u, open(
        output, "w"
    ) as output:
        # Skip the header
        d.readline()
        u.readline()
        
        output.write(f'id,year,codEnte,differentiated,undifferentiated\n')

        for line in d.readlines():
            undifferentiated_value = u.readline().split(",")[-2]
            line = line.strip() + f"{undifferentiated_value}\n"
            output.write(line)
            
    print(f"Datasets merged to {output}")
    
waste_matching()