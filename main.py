import sys

def read_database_file(file_name):
    try:
        database_file = open(file_name,'r')
        row_list = []
        for row in database_file:
            row = row[:-1].split(',')
            row_list.append(row)
        database_file.close()
        return row_list
    except:
        sys.exit('Error, verify that the file exists')

def euclidean_distance(database_instance, test_data, number_of_attributes):
    distance = 0
    for i in range(number_of_attributes):
        distance += (float(database_instance[i]) - float(test_data[i])) ** 2
    return distance ** 0.5

#def knn(k, database, test_data):
    #for instance in database:


data = read_database_file('spambase/spambase.data')

dataSpam = data[0:1813] ##considerado spam
dataNotSpam = data[1813:3626] ##considerado não spam

dataTreinamento = dataSpam[0:1088] + dataNotSpam[0:1088] #60% da base
dataTeste = dataSpam[1088:1813] + dataNotSpam[1088:1813] #40% da base




#print(data[0][57])
#print(data[0])
#print('Instance 1:',data[0][0], data[0][1])
#print('Instance 2:',data[1][0], data[1][1])
#print('Distance:',euclidean_distance([0.9, 0.0, 0.5, 0.1], [0.0, 0.2, 0.2, 0.8], 4))