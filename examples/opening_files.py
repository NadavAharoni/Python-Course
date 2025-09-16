import sys

#print(sys.argv)
if len(sys.argv) < 2:
    print("Error: missing argument")
    print(F"Usage: python {sys.argv[0]} filename")
    exit(-1)

filename = sys.argv[1]
# print(filename)
street_name_frequency = {}
try:
    with open(filename, "r", encoding="windows-1255") as file: 
        header = file.readline()
        headers = header.strip().split(",")
        street_name_index = headers.index("street_name")
        print(street_name_index)

        print("=============")
        i = 0
        for line in file:
            i += 1
            line = line.strip()
            # print(i, line)
            fields = line.split(",")
            street_name = fields[street_name_index].strip()
            # print(i, F"[{street_name}]")
            
            if street_name not in street_name_frequency:
                street_name_frequency[street_name] = 0
            street_name_frequency[street_name] += 1

            # if i>=500:
            #     break

    print(F"Read {i} rows")
    l = list( street_name_frequency.items() )
    names_by_frequency = sorted(street_name_frequency.items(),
                                key = lambda item: item[1],
                                reverse = True)
    for item in names_by_frequency[0:10]:
        print(item)

    print(street_name_frequency["אלי כהן"])

except FileNotFoundError:
    print(F"{filename} not found")

# except:
#     print("an error occured")

