#!pip install tensorflow==2.0.0
import tensorflow as tf
import keras
from keras import backend as K
from keras.callbacks import ModelCheckpoint
from keras.metrics import categorical_crossentropy, binary_crossentropy, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, mean_squared_logarithmic_error, squared_hinge, hinge, categorical_hinge, logcosh, sparse_categorical_crossentropy, kullback_leibler_divergence, poisson, cosine_proximity
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, Sequential, model_from_json, load_model
from keras.layers import Dense, GlobalAveragePooling2D, Dropout, SeparableConv2D, BatchNormalization, Activation, Conv2D, MaxPooling2D, Flatten, Input
from keras.backend.tensorflow_backend import set_session
from keras.backend.tensorflow_backend import clear_session
from keras.backend.tensorflow_backend import get_session
import gc
import os
import random
import numpy as np
import skimage.io as io
from skimage import color
from skimage.transform import resize
import matplotlib.pyplot as plt
import time
from sklearn.metrics import confusion_matrix
import itertools

classes = []
original_folds = []
folds = []
mdls = []
tsts = []
tstlbl = []
input_size = 3
dc = 7  # :Virgülden sonra kaç basamağın gösterileceği

def info():
    print("\n##############################    INFO    ####################################\n")
    print("Tensorflow version: ", tf.__version__,
        "\nKeras version: ", keras.__version__)
    print("Num GPUs Available: ", len(
        tf.config.experimental.list_physical_devices('GPU')))
    print("\n##############################################################################\n")

def reset_keras():
    print("Start reset keras")
    sess = get_session()
    clear_session()
    sess.close()
    sess = get_session()
    print("********ZeroGPU**********")
    # if it's done something you should see a number being outputted
    print(gc.collect())
    print("*************************")
    # use the same config as you used to create the session
    config = tensorflow.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = 1
    config.gpu_options.visible_device_list = "0"
    set_session(tensorflow.Session(config=config))

def one_hot_encode(labels,numberOfFiles):
        try:
            encoded = np.zeros((len(labels), numberOfFiles))
            for idx, val in enumerate(labels):
                encoded[idx][val] = 1
            return encoded
        except Exception as err:
            print(str(err)+"\nFault in one_hot_encode.")
            pass

def data_prep(v, type,numberOfFiles):  # type Train/Test # v fold1-fold2-fold3-fold4-fold5
    try:
        train_labels = []
        image_dataset = []
        print(classes)
        for j, k in enumerate(classes):
            directory = mainPath+'/'+v+'/'+type+'/'+k
            class_names = next(os.walk(directory))
            print(directory+" -> " +
                    str(len(class_names[2]))+" files found.")
            for cs in class_names[2]:
                path = ''+directory+'/'+cs
                # print(path)
                img = io.imread(path)
                img = resize(img, (img_size, img_size, input_size),
                                anti_aliasing=True)
                image_dataset.append(img)
                train_labels.append(j)
        image_dataset = np.asarray(image_dataset)
        encoded = one_hot_encode(train_labels,numberOfFiles)
        print(type+' data read.')
        return image_dataset, encoded
    except Exception as err:
        print(str(err)+"\nFault in data_prep.")
        pass

def original_or_folded_structure(fileStructure,mainPath,original_k,convert_rgb,img_size,original_percent):
    try:
        os.chdir(mainPath)
        global folds
        global classes
        global numberOfFiles
        if(fileStructure):  # Filestructure value is true=folded structure
            folds = sorted(os.listdir())
            print(folds)
            os.chdir(folds[0]+'/train')
            classes = sorted(os.listdir())
            numberOfFiles = len(classes)
        else:  # Original file structure
            classes = []
            classes = sorted(os.listdir())
            print(classes)
            numberOfFiles = len(classes)
            # Original data is reading
            foldedDataset = []
            for j, k in enumerate(classes):
                directory = mainPath+'/'+k
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
                        img2 = resize(img, (img_size, img_size, input_size),
                                    anti_aliasing=True)
                    imgLbl.append(img2)
                    imgLbl.append(cs)
                    imgLbl.append(j)
                    tmpClass.append(imgLbl)
                foldedDataset.append(tmpClass)

            # Original dataset is split into file structure

            folds = []
            for f in range(original_k):  # fold1-fold2-fold3
                fold = []
                trainClasses = []
                testClasses = []
                for i in range(len(classes)):  # shuffle for everyclass
                    random.shuffle(foldedDataset[i])
                    tmpTrain = []
                    tmpTest = []
                    # print(len(foldedDataset[i]))
                    for j in range(len(foldedDataset[i])):
                        if(j < int(len(foldedDataset[i])*(1-original_percent/100))):
                            tmpTrain.append(foldedDataset[i][j])
                        else:
                            tmpTest.append(foldedDataset[i][j])
                    trainClasses.append(tmpTrain)
                    testClasses.append(tmpTest)

                fold.append(trainClasses)
                fold.append(testClasses)
                folds.append(fold)
        global original_folds
        original_folds = folds
    except Exception as err:
        print(str(err)+"\nFault in original_or_folded_structure.")
        pass
def original_data_prep(v,numberOfFiles):
    global train_labels
    global test_image_dataset
    train_image_dataset = []
    test_image_dataset = []
    train_labels = []
    test_labels = []
    for j, tmpcls in enumerate(v[0]):  # train
        for k, tmpimglbl in enumerate(tmpcls):
            img = tmpimglbl[0]
            train_image_dataset.append(img)
            label = tmpimglbl[2]
            train_labels.append(label)
    for j, tmpcls in enumerate(v[1]):  # test
        for k, tmpimglbl in enumerate(tmpcls):
            img = tmpimglbl[0]
            test_image_dataset.append(img)
            label = tmpimglbl[2]
            test_labels.append(label)
    train_image_dataset = np.asarray(train_image_dataset)
    encoded_train = one_hot_encode(train_labels,numberOfFiles)
    test_image_dataset = np.asarray(test_image_dataset)
    encoded_test = one_hot_encode(test_labels,numberOfFiles)
    return train_image_dataset, encoded_train, test_image_dataset, encoded_test

def rate_opt(opt, lr):
    try:
        if(opt == 'SGD'):
            from keras.optimizers import SGD
            optim = SGD(learning_rate=lr)
        elif(opt == 'RMSprop'):
            from keras.optimizers import RMSprop
            optim = RMSprop(learning_rate=lr)
        elif(opt == 'Adagrad'):
            from keras.optimizers import Adagrad
            optim = Adagrad(learning_rate=lr)
        elif(opt == 'Nadam'):
            from keras.optimizers import Nadam
            optim = Nadam(learning_rate=lr)
        elif(opt == 'Adadelta'):
            from keras.optimizers import Adadelta
            optim = Adadelta(learning_rate=lr)
        elif(opt == 'Adamax'):
            from keras.optimizers import Adamax
            optim = Adamax(learning_rate=lr)
        else:
            from keras.optimizers import Adam
            optim = Adam(learning_rate=lr)
        return optim
        pass
    except Exception as err:
        print(
            str(err)+"\nFault in rate_opt. Please your input like 0.1--0.01--0.0001")
        pass

def datagen(r_r,z_r,w_s_r,h_s_r,s_r,h_f,f_m):
    try:
        datagen = ImageDataGenerator(
            rotation_range=r_r,
            zoom_range=z_r,
            width_shift_range=w_s_r,
            height_shift_range=h_s_r,
            shear_range=s_r,
            horizontal_flip=h_f,
            fill_mode=f_m)
        return datagen
    except Exception as err:
        print(str(err)+"\nFault in datagen")
        pass

def mdlcmp(mdl,opt, act,lr,img_size,numberOfFiles,weight,loss):
    try:
        if(mdl == 'Xception'):
            from keras.applications.xception import Xception
            from keras.applications.xception import preprocess_input
            base_model = Xception(weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("Xception model is uploading... ")
        elif(mdl == 'VGG16'):
            from keras.applications.vgg16 import VGG16
            from keras.applications.vgg16 import preprocess_input
            base_model = VGG16(weights=weight, include_top=False,input_shape=(img_size, img_size, 3))
            print("VGG16 model is uploading... ")
        elif(mdl == 'VGG19'):
            from keras.applications.vgg19 import VGG19
            from keras.applications.vgg19 import preprocess_input
            base_model = VGG19(weights=weight, include_top=False,input_shape=(img_size, img_size, 3))
        elif(mdl == 'ResNet50'):
            from keras.applications.resnet import ResNet50
            from keras.applications.resnet import preprocess_input
            base_model = ResNet50(weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet50 model is uploading... ")
        elif(mdl == 'ResNet50V2'):
            from keras.applications.resnet_v2 import ResNet50V2
            from keras.applications.resnet_v2 import preprocess_input
            base_model = ResNet50V2(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet50V2 model is uploading... ")
        elif(mdl == 'ResNet101'):
            from keras.applications.resnet import ResNet101
            from keras.applications.resnet import preprocess_input
            base_model = ResNet101(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet50V2 model is uploading... ")
        elif(mdl == 'ResNet101V2'):
            from keras.applications.resnet_v2 import ResNet101V2
            from keras.applications.resnet_v2 import preprocess_input
            base_model = ResNet101V2(weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet101V2 model is uploading... ")
        elif(mdl == 'ResNet152'):
            from keras.applications.resnet import ResNet152
            from keras.applications.resnet import preprocess_input
            base_model = ResNet152(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet152 model is uploading... ")
        elif(mdl == 'ResNet152V2'):
            from keras.applications.resnet_v2 import ResNet152V2
            from keras.applications.resnet_v2 import preprocess_input
            base_model = ResNet152V2(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("ResNet152V2 model is uploading... ")
        elif(mdl == 'InceptionV3'):
            from keras.applications.inception_v3 import InceptionV3
            from keras.applications.inception_v3 import preprocess_input
            base_model = InceptionV3(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("InceptionV3 model is uploading... ")
        elif(mdl == 'InceptionResNetV2'):
            from keras.applications.inception_resnet_v2 import InceptionResNetV2
            from keras.applications.inception_resnet_v2 import preprocess_input
            base_model = InceptionResNetV2(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("InceptionResNetV2 model is uploading... ")
        elif(mdl == 'MobileNet'):
            from keras.applications.mobilenet import MobileNet
            from keras.applications.mobilenet import preprocess_input
            base_model = MobileNet(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("MobileNet model is uploading... ")
        elif(mdl == 'MobileNetV2'):
            from keras.applications.mobilenet_v2 import MobileNetV2
            from keras.applications.mobilenet_v2 import preprocess_input
            base_model = MobileNetV2(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("MobileNetV2 model is uploading... ")
        elif(mdl == 'DenseNet121'):
            from keras.applications.densenet import DenseNet121
            from keras.applications.densenet import preprocess_input
            base_model = DenseNet121(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("DenseNet121 model is uploading... ")
        elif(mdl == 'DenseNet169'):
            from keras.applications.densenet import DenseNet169
            from keras.applications.densenet import preprocess_input
            base_model = DenseNet169(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3))
            print("DenseNet169 model is uploading... ")
        elif(mdl == 'DenseNet201'):
            from keras.applications.densenet import DenseNet201
            from keras.applications.densenet import preprocess_input
            base_model = DenseNet201(
                weights=weight, include_top=False, input_shape=(img_size, img_size, 3)) 
            print("DenseNet201 model is uploading... ")                  
        elif(mdl == 'NASNetMobile'):
            from keras.applications.nasnet import NASNetMobile
            from keras.applications.nasnet import preprocess_input
            base_model = NASNetMobile(weights=weight, include_top=False,input_shape=(img_size, img_size, 3))
            print("NASNetMobile model is uploading... ")
        else:
            from keras.applications.nasnet import NASNetLarge
            from keras.applications.nasnet import preprocess_input
            base_model = NASNetLarge(weights=weight, include_top=False,input_shape=(img_size, img_size, 3))    
            print("NASNetLarge model is uploading... ")  
        # Last layers flatten and activation
        x = base_model.output
        x = Flatten()(x)
        predictions = Dense(numberOfFiles, activation=act)(x)
        model = Model(inputs=base_model.input, outputs=predictions)
        # Model Compile
        model.compile(optimizer=rate_opt(opt, lr),
                        loss=loss,
                        metrics=['accuracy'])
        # callbacks_list = [keras.callbacks.EarlyStopping(monitor='acc', mode='max', patience=3, verbose=1)]
        return model
    except Exception as err:
        print(str(err)+"\nFault in mdlcmp.")
        pass

def baseModel(self, mdl, a, o, loss, imagenet, lr, img_size, batch_size, epochs, convert_rgb, augment, r_r, h_s_r, w_s_r, z_r, s_r, h_f, f_m, mainPath, fileStructure, original_k, original_percent):
    info()
    os.chdir(mainPath)
    if(imagenet):
        weight = 'imagenet'
    else:
        weight = None
    original_or_folded_structure(fileStructure,mainPath,original_k,convert_rgb,img_size,original_percent)
    try:
        scoreses = ""
        t = 0 #Ortalama score için her foldda toplanan değer.
        totalScore = 0
        global mdls
        global tsts
        global tstlbl
        mdls.clear()
        tsts.clear()
        tstlbl.clear()
        self.allModels.clear()
        # fold fold data okunuyor ['fold1', 'fold2', 'fold3','fold4','fold5']
        for i, v in enumerate(folds):  # folds
            # Activasion ve optimizerlar
            reset_keras()
            start_time = time.time()
            print("!!!!!!!!!!!!!!! ", mdl, a, o,
                    "fold"+str(i+1)+" training !!!!!!!!!!!!!!!!!!!")
            # Data hazırlanıyor
            
            if(fileStructure):                    
                train, train_label = data_prep(v, 'train')
                test, test_label = data_prep(v, 'test')
            else:
                train, train_label, test, test_label = original_data_prep(v,numberOfFiles)
            # Model compile ediliyor
            model = mdlcmp(mdl,o, a,lr,img_size,numberOfFiles,weight,loss)
            # Data augmentation yapılıyor
            if(augment > 0):
                aug = datagen(r_r,z_r,w_s_r,h_s_r,s_r,h_f,f_m)
                epoch_step = ((len(train) * (augment)) // batch_size) + 1
                print('Steps per epoch:', epoch_step,
                        ' Train length:', len(train))

                # Model EĞİTİLİYOR
                model.fit_generator(aug.flow(train, train_label, batch_size=batch_size),
                                    steps_per_epoch=epoch_step,
                                    epochs=epochs)
            else:
                model.fit(train, train_label,batch_size=batch_size, epochs=epochs,
                            validation_data=None, verbose=1)
            end_time = time.time()
            # Model sonuçları test ediliyor
            print("\n*********",a, o, 'TestFold {', i+1, '}',"*********")

            scores = model.evaluate(test, test_label,batch_size=batch_size, verbose=1)#batch_size=len(test)
            pred = model.predict(test,batch_size=batch_size, verbose=0)#batch_size=len(test)

            train_time=str(round((end_time-start_time),dc))
            print('Train Time: ',train_time)
            print('Test Loss: ', scores[0])
            print('Test Accuracy: ', scores[1], '\n')
            totalScore += scores[1]
            mdls.append(model)
            tsts.append(pred)
            tstlbl.append(test_label)
            t += 1
            # Sonuçlar kaydediliyor
            sc = "{Fold " + str(i+1)+"} Accuracy: " + str(
                round(scores[1],dc)) + " Loss: " + str(round(scores[0],dc)) + " Time: "+train_time + "\n"
            self.allModels.addItem("Fold"+str(i+1))
            scoreses += sc
            del model
        self.scores_screen.setText(self.scores_screen.toPlainText()+scoreses)
        self.progressBar.setValue(int(totalScore*100)/t)
        pass

    except Exception as err:
        print(str(err)+"\nFault in train_base_model")
        pass

def preTrainedModel(self, _h5, activation, optimizer, loss, _json, optimizerLr, batch_size, epoch, augment, r_r, h_s_r, w_s_r, z_r, s_r, h_f, f_m, mainPath, fileStructure, original_k, original_percent):
    info()
    #Json dosyasının okunması
    json_filename = _json.split("/")[-1]
    _json_path = _json.replace("/"+json_filename, "")
    os.chdir(_json_path)
    json_file = open(json_filename, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    #Json içeriğinden yeni modelin oluşturulması
    loaded_model_1 = model_from_json(loaded_model_json)
    #H5 dosyasının yüklenmesi
    h5_filename = _h5.split("/")[-1]
    _h5_path = _h5.replace("/"+h5_filename, "")
    os.chdir(_h5_path)
    loaded_model_1.load_weights(h5_filename)
    #Önceden eğitilen modelin eğitimi için son 2 katmanının kaldırılması
    loaded_model_1.layers.pop()
    loaded_model_1.layers.pop()
    #Önceden eğitilen modelin input_sizeına göre girilen verisetinin çevrilmesi
    img_size = loaded_model_1.input.shape.dims[2].value
    if(loaded_model_1.input.shape.dims[3].value == 3):
        convert_rgb = True
    else:
        global input_size
        input_size = 1
    #Orjinal veya dosyalanmış veri setinin okunması
    original_or_folded_structure(fileStructure,mainPath,original_k,convert_rgb,img_size,original_percent)
    ##################
    x = Flatten()(loaded_model_1.layers[-1].output)
    predictions = Dense(numberOfFiles, activation=activation)(x)
    model = Model(input=loaded_model_1.input, output=predictions)
    # Yeni model compile ediliyor
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])
    scoreses = ""
    t = 0
    totalScore = 0
    global mdls
    global tsts
    global tstlbl
    mdls.clear()
    tsts.clear()
    tstlbl.clear()
    self.allModels.clear()
    # fold fold data okunuyor, ['fold1', 'fold2', 'fold3','fold4','fold5']
    for i, v in enumerate(folds):
        reset_keras()
        start_time = time.time()
        print("!!!!!!!!!!!!!!! Load model ", activation, optimizer,
            "fold"+str(i+1)+" training !!!!!!!!!!!!!!!!!!!")
        loaded_model=model
        # Data hazırlanıyor
        if(fileStructure):
            train, train_label = data_prep(v, 'train',numberOfFiles)
            test, test_label = data_prep(v, 'test',numberOfFiles)
        else:
            train, train_label, test, test_label = original_data_prep(v,numberOfFiles)
        # Data augmentation yapılıyor
        aug = datagen(r_r,z_r,w_s_r,h_s_r,s_r,h_f,f_m)
        epoch_step = ((len(train) * augment) // batch_size) + 1
        print('Steps per epoch:', epoch_step, ' Train length:', len(train))

        # Model eğitiliyor
        loaded_model.fit_generator(aug.flow(train, train_label, batch_size=batch_size),
                                steps_per_epoch=epoch_step,
                                epochs=epoch)

        # Model sonuçları test ediliyor
        print(activation, optimizer, 'TestFold {', i+1, '}')
        scores = loaded_model.evaluate(test, test_label, verbose=1)
        end_time = time.time()
        train_time=str(round((end_time-start_time),dc))
        print('Train Time: ' ,train_time)
        print('Test Loss: ', scores[0])
        print('Test Accuracy: ', scores[1], '\n')
        totalScore += scores[1]
        mdls.append(loaded_model)
        pred = loaded_model.predict(test, verbose=0)
        tsts.append(pred)
        tstlbl.append(test_label)
        t += 1
        # Sonuçlar kaydediliyor
        sc = "{Fold " + str(i+1)+"}Accuracy: " + str(round(scores[1],dc)) + " Loss: " + str(round(scores[0],dc)) +" Time: "+train_time+ "\n"
        scoreses += sc
        self.allModels.addItem("Fold"+str(i+1))
        del loaded_model
    self.scores_screen.setText(self.scores_screen.toPlainText()+"\n"+scoreses)
    self.progressBar.setValue(int(totalScore*100)/t)

def savetodisk(self, fileStructure, datasetPath, newModelPath):
    # Áself.scores_screen.setText(val)
    # save data
    try:
        if(len(self.output_dataset_path.text()) > 0 and fileStructure):
            # Dataset save to disk
            savePath = datasetPath  # datanın kaydedileceği yer
            datasetname = self.output_data_name.text()
            os.chdir(savePath)
            os.mkdir(datasetname)
            os.chdir(savePath+'/'+datasetname)
            for i, tmpFold in enumerate(original_folds):  # fold1-fold2-fold3
                os.chdir(savePath+'/'+datasetname)
                os.mkdir("fold"+str(i+1))
                os.chdir(savePath+'/'+datasetname+'/'+"fold"+str(i+1))
                os.mkdir("train")
                os.mkdir("test")
                for j, tmpcls in enumerate(tmpFold[0]):  # train
                    os.chdir(savePath+'/'+datasetname +
                             '/'+"fold"+str(i+1)+'/train')
                    os.mkdir(classes[j])
                    os.chdir(savePath+'/'+datasetname+'/' +
                             "fold"+str(i+1)+'/train/'+classes[j])
                    for k, tmpimglbl in enumerate(tmpcls):
                        io.imsave(tmpimglbl[1], tmpimglbl[0])
                for j, tmpcls in enumerate(tmpFold[1]):  # test
                    os.chdir(savePath+'/'+datasetname +
                             '/'+"fold"+str(i+1)+'/test')
                    os.mkdir(classes[j])
                    os.chdir(savePath+'/'+datasetname+'/' +
                             "fold"+str(i+1)+'/test/'+classes[j])
                    for k, tmpimglbl in enumerate(tmpcls):
                        io.imsave(tmpimglbl[1], tmpimglbl[0])
            print("Dataset saved...")
        else:
            print(
                "If you wanna save dataset, you should check original file structure and dataset path input!!!")
        pass
    except Exception as err:
        print(str(err)+"\nDataset can't be saved!!")
        pass
    # save model weigts
    try:
        newFileName = self.output_model_name.text()
        os.chdir(newModelPath)
        os.mkdir(newFileName)
        os.chdir(newModelPath+'/'+newFileName)
        selectMdl = int(self.allModels.currentText().replace("Fold", ""))-1
        if(len(self.output_model_path.text()) > 0):
            model_json = mdls[selectMdl].to_json()
            with open(newFileName+'.json', 'w') as json_file:
                json_file.write(model_json)
            
            print(len(mdls))
            print(mdls[selectMdl].summary())
            mdls[selectMdl].save_weights(newFileName+'.h5')
            print("Model saved...")
            # mdls[selectMdl].save(newFileName)
            # print("Model saved...")
        pass
    except Exception as err:
        print(str(err)+"\nThe model weigths could not be saved!!!")
        pass
    # save confusion matrix

def plot_confusion_matrix(cm, classes,
                            normalize=False,
                            title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
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

def confMat(self):
    selectMdl = int(self.allModels.currentText().replace("Fold", ""))-1
    pred = tsts[selectMdl]
    y_pred = np.argmax(pred, axis=1)
    y_test = np.argmax(tstlbl[selectMdl], axis=1)
    cnf_matrix = confusion_matrix(y_test, y_pred)
    plot_confusion_matrix(cnf_matrix, classes=classes,
                            normalize=False,
                            title='Confusion matrix', cmap=plt.cm.Blues)

def allConfMat(self):
    print("All models")