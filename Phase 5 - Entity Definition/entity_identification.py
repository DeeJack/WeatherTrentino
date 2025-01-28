def open_ape(ape_file, output_path):
    count = 0
    output = ""
    
    with open(ape_file, 'r', encoding="UTF-8") as ape:
        lines = ape.readlines()
        header = "id," + lines[0]
        output += header
        for line in lines[1:]:
            output += str(count) + ',' + line
            count += 1
    
    with open(output_path, 'w', encoding="UTF-8") as output_file:
        output_file.write(output)

open_ape_path = "../Phase 2 - Information Gathering/DataCleaning/open_ape_clean.csv"
open_ape(open_ape_path, './open_ape_id.csv')