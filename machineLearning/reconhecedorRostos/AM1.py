from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.decomposition import PCA

import pandas as pd
import numpy as np
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.preprocessing import image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#*********************************
# Preprocessamento - Início

# Carregar as anotações do dataset CelebA
attributes = pd.read_csv('caminho/da/pasta/arquivo/list_attr_celeba.csv')
images_path = 'caminho/da/pasta/arquivo/img_align_celeba/img_align_celeba/'

# Visualizar algumas amostras de atributos
print(attributes.head())

# Escolher o atributo para classificação, por exemplo, "Smiling"
attributes['Smiling'] = attributes['Smiling'].apply(lambda x: 1 if x == 1 else 0)

# Carregar e processar as imagens
def load_and_preprocess_images(image_paths, target_size=(224, 224)):
    images = []
    for img_path in image_paths:
        img = image.load_img(images_path + img_path, target_size=target_size)
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalização
        images.append(img)
    return np.vstack(images)

# Exemplo de carregamento de um subset de dados
image_paths = attributes['image_id'].head(1000)
X = load_and_preprocess_images(image_paths)
y = attributes['Smiling'].head(1000)

# Divisão em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessamento - Fim
#*********************************


#*********************************
# AM1 - Início

# Feature Extraction com PCA
X_train_flat = X_train.reshape((X_train.shape[0], -1))
X_test_flat = X_test.reshape((X_test.shape[0], -1))

pca = PCA(n_components=150)
X_train_pca = pca.fit_transform(X_train_flat)
X_test_pca = pca.transform(X_test_flat)

# Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train_pca, y_train)
rf_predictions = rf.predict(X_test_pca)

# SVM
svm = SVC(probability=True, random_state=42)
svm.fit(X_train_pca, y_train)
svm_predictions = svm.predict(X_test_pca)

# Avaliação dos Modelos
def evaluate_model(predictions, y_test):
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    return accuracy, precision, recall, f1

rf_evaluation = evaluate_model(rf_predictions, y_test)
svm_evaluation = evaluate_model(svm_predictions, y_test)

print('Random Forest Evaluation:', rf_evaluation)
print('SVM Evaluation:', svm_evaluation)

# AM1 - Fim
#*********************************



#*********************************
#AM2 - Inicio

import tensorflow as tf

VGG16 = tf.keras.applications.VGG16



# Modelo CNN (VGG16)
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Adicionar camadas finais
x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
predictions = tf.keras.layers.Dense(len(np.unique(y)), activation='softmax')(x)

# Modelo final
model = tf.keras.Model(inputs=base_model.input, outputs=predictions)

# Congelar as camadas base do VGG16
for layer in base_model.layers:
    layer.trainable = False

# Compilar o modelo
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinamento
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Avaliação
cnn_predictions = model.predict(X_test)
cnn_predictions = np.argmax(cnn_predictions, axis=1)

cnn_evaluation = evaluate_model(cnn_predictions, y_test)
print('CNN Evaluation:', cnn_evaluation)

# AM2 - Fim
#*********************************

#*********************************
# Plotagem de Gráficos - Início

# Configurar o layout para gráficos lado a lado
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Função para adicionar anotações aos gráficos
def add_annotations(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval, round(yval, 2), va='bottom') 

# Plotar o gráfico de acurácia
bars = axs[0, 0].bar(['Random Forest', 'SVM', 'CNN'], [rf_evaluation[0], svm_evaluation[0], cnn_evaluation[0]], color=['blue', 'green', 'red'])
add_annotations(axs[0, 0], bars)
axs[0, 0].set_ylabel('Acurácia')
axs[0, 0].set_title('Acurácia dos Modelos')

# Plotar o gráfico de precisão
bars = axs[0, 1].bar(['Random Forest', 'SVM', 'CNN'], [rf_evaluation[1], svm_evaluation[1], cnn_evaluation[1]], color=['blue', 'green', 'red'])
add_annotations(axs[0, 1], bars)
axs[0, 1].set_ylabel('Precisão')
axs[0, 1].set_title('Precisão dos Modelos')

# Plotar o gráfico de recall
bars = axs[1, 0].bar(['Random Forest', 'SVM', 'CNN'], [rf_evaluation[2], svm_evaluation[2], cnn_evaluation[2]], color=['blue', 'green', 'red'])
add_annotations(axs[1, 0], bars)
axs[1, 0].set_ylabel('Recall')
axs[1, 0].set_title('Recall dos Modelos')

# Plotar o gráfico de f1
bars = axs[1, 1].bar(['Random Forest', 'SVM', 'CNN'], [rf_evaluation[3], svm_evaluation[3], cnn_evaluation[3]], color=['blue', 'green', 'red'])
add_annotations(axs[1, 1], bars)
axs[1, 1].set_ylabel('F1')
axs[1, 1].set_title('F1 dos Modelos')

plt.tight_layout()
plt.show()

# Visualização de algumas imagens
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(X_test[i])
    plt.title('Smiling' if y_test.iloc[i] == 1 else 'Not Smiling')
    plt.axis('off')
plt.suptitle('Exemplos de Imagens de Teste e suas Classes')
plt.show()

# Plotagem de Gráficos - Fim
#*********************************