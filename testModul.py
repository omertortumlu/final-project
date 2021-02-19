import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import keras
from keras.metrics import categorical_crossentropy, binary_crossentropy, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, mean_squared_logarithmic_error, squared_hinge, hinge, categorical_hinge, logcosh, sparse_categorical_crossentropy, kullback_leibler_divergence, poisson, cosine_proximity
from keras.optimizers import SGD, Adam, Adamax, Adagrad, RMSprop, Adadelta, Nadam
from keras.models import Model, model_from_json, load_model

import skimage.io as io
from skimage.transform import resize
from skimage import color
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools


def one_hot_encode(labels,numberOfFiles):
    try:
        encoded = np.zeros((len(labels), numberOfFiles))
        for idx, val in enumerate(labels):
            encoded[idx][val] = 1
        return encoded
    except Exception as err:
        self.test_screen.setStyleSheet("background-color: red")
        self.test_screen.setText("Error in one hot encoded function. "+str(err))
        pass

def original_data_prep(v,numberOfFiles):
    try:
        test_image_dataset = []
        test_labels = []
        for j, tmpcls in enumerate(v):  # test
            for k, tmpimglbl in enumerate(tmpcls):
                img = tmpimglbl[0]
                test_image_dataset.append(img)
                label = tmpimglbl[2]
                test_labels.append(label)

        test_image_dataset = np.asarray(test_image_dataset)
        encoded_test = one_hot_encode(test_labels,numberOfFiles)
        return test_image_dataset, encoded_test
    except Exception as err:
        self.test_screen.setStyleSheet("background-color: red")
        self.test_screen.setText("Error in original_data_prep function "+str(err))
        pass

def test(self):
    try:
        optimizer = self.test_optimizer.currentText()
        loss = self.test_modelLoss.currentText()
        datasetPath = self.test_dataset_path.text()

        _json = self.test_path_json.text()
        json_filename = _json.split("/")[-1]
        _json_path = _json.replace("/"+json_filename, "")

        os.chdir(_json_path)

        json_file = open(json_filename, 'r')

        loaded_model_json = json_file.read()

        json_file.close()

        #
        global test_model
        test_model = model_from_json(loaded_model_json)
        #

        _h5 = self.test_path_h5.text()
        h5_filename = _h5.split("/")[-1]
        _h5_path = _h5.replace("/"+h5_filename, "")

        os.chdir(_h5_path)
        test_model.load_weights(h5_filename)
        test_model.compile(loss=loss,
                           optimizer=optimizer, metrics=['accuracy'])

        img_size = test_model.input.shape.dims[2].value
        if(test_model.input.shape.dims[3].value == 3):
            global convert_rgb
            convert_rgb = True
        input_size = test_model.input.shape.dims[3].value

        os.chdir(datasetPath)
        global classes
        classes = sorted(os.listdir())
        print(classes)
        global numberOfFiles
        numberOfFiles = len(classes)
        global foldedDataset
        foldedDataset = []
        #Imageset is reading
        for j, k in enumerate(classes):
            directory = datasetPath+'/'+k
            img_names = next(os.walk(directory))
            print(directory+" -> " +
                  str(len(img_names[2]))+" images found.")
            tmpClass = []
            for cs in img_names[2]:
                imgLbl = []
                tmpPath = ''+directory+'/'+cs
                img = io.imread(tmpPath)
                if convert_rgb == True:
                    img2 = color.gray2rgb(img, alpha=None)
                    img2 = resize(img2, (img_size, img_size, input_size),
                                  anti_aliasing=True)
                else:
                    img2 = color.rgb2gray(img)
                    img2 = resize(img, (img_size, img_size, input_size),
                                  anti_aliasing=True)
                imgLbl.append(img2)
                imgLbl.append(cs)
                imgLbl.append(j)
                tmpClass.append(imgLbl)
            foldedDataset.append(tmpClass)

        global test, test_label
        test, test_label = original_data_prep(foldedDataset,numberOfFiles)
        scores = test_model.evaluate(test, test_label, verbose=1)
        sc = "{Test Fold"+"} Accuracy: " + str(
            scores[1]) + " Loss: " + str(scores[0]) + "\n"
        pred = test_model.predict(test, verbose=1)
        self.test_screen.setText(sc+str(pred))
    except Exception as err:
        self.test_screen.setStyleSheet("background-color: red")
        self.test_screen.setText("1 "+str(err))
        pass

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    try:
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.tight_layout()
        plt.show()
    except Exception as err:
        self.test_screen.setStyleSheet("background-color: red")
        self.test_screen.setText("2.1 "+str(err))
        pass

def confMat(self):
    try:
        pred = test_model.predict(test, verbose=0)
        y_pred = np.argmax(pred, axis=1)
        y_test = np.argmax(test_label, axis=1)
        cnf_matrix = confusion_matrix(y_test, y_pred)
        plot_confusion_matrix(cnf_matrix, classes=classes,
                              normalize=False,
                              title='Confusion matrix', cmap=plt.cm.Blues)
        pass
    except Exception as err:
        self.test_screen.setStyleSheet("background-color: red")
        self.test_screen.setText("2 "+str(err))
        pass
