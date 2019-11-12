import sys

def read_database_file(file_name):
    try:
        database_file = open(file_name,'r') # Abrindo arquivo em modo de leitura
        row_list = []
        database_file.readline() # Pulando a primeira linha
        for row in database_file:
            row = row[:-1].split(',')
            row = row[1:] # Retirando id
            row_list.append(row)
        database_file.close()
        return row_list
    except:
        sys.exit('Error, verify that the file exists')

# Calcula a distância euclidiana entre duas instâncias de n dimensões (atributos)
def euclidean_distance(training_instance, test_instance, number_of_attributes):
    distance = 0
    for i in range(number_of_attributes):
        distance += (float(training_instance[i]) - float(test_instance[i])) ** 2
    return distance ** 0.5

def knn(k, training_data, test_data):
    result_classification = []
    for test_instance in test_data:
        neighbours_distances = []
        for training_instance in training_data:
            # Guarda a distância euclidiana e a classe da instância de treinamento
            distance = euclidean_distance(training_instance,test_instance,4)
            neighbours_distances.append([distance,training_instance[4]])
        
        # Ordena as distâncias em ordem crescente
        neighbours_distances = sorted(neighbours_distances, key = lambda x: (x[0]))

        # Verifica as classes das k menores distâncias
        for neighbour in neighbours_distances[:k]:
            qnt_setosa = 0
            qnt_versicolor = 0
            qnt_virginica = 0
            
            if (neighbour[1] == 'Iris-setosa'):
                qnt_setosa += 1
            elif (neighbour[1] == 'Iris-versicolor'):
                qnt_versicolor += 1
            else:
                qnt_virginica += 1
        
        # PODE dar EMPATE QUANDO K = 3
        maior = qnt_setosa
        if (qnt_versicolor > maior):
            result_classification.append([test_instance[4],'Iris-versicolor'])
        elif (qnt_virginica > maior):
             result_classification.append([test_instance[4],'Iris-virginica'])
        else:
             result_classification.append([test_instance[4],'Iris-setosa'])
    return result_classification

# Matriz de confusão Setosa:0, Versicolor:1, Virginica:2
def confusion_matrix(result_classification):
    dic = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
    
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    ## formato instance: [Classe,Predição]
    ##instance_exemplo = ['Iris-virginica','Iris-versicolor']
    ##dic[instance_exemplo[0]][instance_exemplo[1]] retorna a linha e coluna que será alterada

    for instance in result_classification:
        matrix[dic[instance[0]]][dic[instance[1]]] += 1
    return matrix

##Acurácia
def accuracy(matrix):
    total_sum = 0
    diagonal_sum = 0
    for i in range(3):
        for j in range(3):
            if(i == j):
                diagonal_sum += matrix[i][j]
            total_sum += matrix[i][j]

    accuracy = diagonal_sum / total_sum

    return accuracy

##Recall
def recall(matrix):
    ssr = matrix[0][0] / (matrix[0][0] + matrix[0][1] + matrix[0][2])
    #sver = matrix[0][1] / (matrix[0][0] + matrix[0][1] + matrix[0][2])
    #svir = matrix[0][2] / (matrix[0][0] + matrix[0][1] + matrix[0][2])

    #vesr = matrix[1][0] / (matrix[1][0] + matrix[1][1] + matrix[1][2])
    vever = matrix[1][1] / (matrix[1][0] + matrix[1][1] + matrix[1][2])
    #vevir = matrix[1][2] / (matrix[1][0] + matrix[1][1] + matrix[1][2])

    #visr = matrix[2][0] / (matrix[2][0] + matrix[2][1] + matrix[2][2])
    #viver = matrix[2][1] / (matrix[2][0] + matrix[2][1] + matrix[2][2])
    vivir = matrix[2][2] / (matrix[2][0] + matrix[2][1] + matrix[2][2])

    return [ssr, vever, vivir]
    #return [ssr, sver, svir, vesr, vever, vevir, visr, viver, vivir]

##Precisão
def precision(matrix):
    precision_setosa = matrix[0][0]/ (matrix[0][0] + matrix[1][0] + matrix[2][0])
    precision_versicolor = matrix[1][1] / (matrix[0][1] + matrix[1][1] + matrix[2][1])
    precision_virginica = matrix[2][2] / (matrix[0][2] + matrix[1][2] + matrix[2][2])

    return [precision_setosa, precision_versicolor, precision_virginica]

##F1-score
def f1_score(recall, precision):
    f1_score_setosa = (2 * (recall[0] * precision[0])) / (recall[0] + precision[0])
    f1_score_versicolor = (2 * (recall[1] * precision[1])) / (recall[1] + precision[1])
    f1_score_virginica = (2 * (recall[2] * precision[2])) / (recall[2] + precision[2])

    return [f1_score_setosa, f1_score_versicolor, f1_score_virginica]

data = read_database_file(sys.argv[1])

# Base de treinamento
data_setosa = data[0:30]
data_versicolor = data[50:80]
data_virginica = data[100:130]
training_data = []
training_data += data_setosa + data_versicolor + data_virginica

# Base de teste
data_setosa = data[30:50]
data_versicolor = data[80:100]
data_virginica = data[130:150]
test_data = []
test_data += data_setosa + data_versicolor + data_virginica

result = knn(7, training_data, test_data)
matrix = confusion_matrix(result)

recall = recall(matrix)
precision = precision(matrix)



print(matrix[0])
print(matrix[1])
print(matrix[2])

print(f1_score(recall, precision))





'''
recall = recall(matrix)
print(recall[:3])
print(recall[3:6])
print(recall[6:])
print(accuracy(matrix))
'''