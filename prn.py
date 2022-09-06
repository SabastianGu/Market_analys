bin_data = open ('multicoin_dataset.csv', 'r')
lines = bin_data.readlines()
bin_data.close()

result = ""
for line in lines :
    if len(line) > 72:
        result += line

bin_data = open('multicoin_dataset.csv', 'w')
bin_data.write(result)