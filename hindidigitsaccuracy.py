import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimage
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import cv2
data_train=np.zeros((17000,256))
label_train=np.zeros((1,17000),dtype=np.int8);
count=0
count1=0
for k in range(0,10):
    for l in range(1,1701):
        path=r'C:/Users/Naman/Desktop/DevanagariHandwrittenCharacterDataset/Train1/digit_%d/(%d).png'%(k,l);
        im=mimage.imread(path)
        im[im<0.9]=0
        im[im>0.9]=1
        for i in range(0,30,2):
            for j in range(0,30,2):
                data_train[count1,count]=im[i,j]+im[i+1,j]+im[i,j+1]+im[i+1,j+1];
                label_train[0,count1]=k;
                count=count+1;
        count1=count1+1;
        count=0;
data_test=np.zeros((3000,256))
label_test=np.zeros((1,3000),dtype=np.int8);
count=0;
count1=0;
for k in range(0,10):
    for l in range(1,301):
        path=r'C:/Users/Naman/Desktop/DevanagariHandwrittenCharacterDataset/Test1/digit_%d/(%d).png'%(k,l);
        im=mimage.imread(path)
        im[im<0.9]=0
        im[im>0.9]=1
        for i in range(0,30,2):
            for j in range(0,30,2):
                data_test[count1,count]=im[i,j]+im[i+1,j]+im[i,j+1]+im[i+1,j+1];
                label_test[0,count1]=k;
                count=count+1;
        count1=count1+1;
        count=0;
classifier_neural =MLPClassifier(hidden_layer_sizes=(250), activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='adaptive', learning_rate_init=0.001, power_t=0.5, max_iter=1000, shuffle=True, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)
classifier_neural.fit(data_train,label_train.ravel());
output=classifier_neural.predict(data_test);
print(metrics.accuracy_score(label_test.ravel(),output))
filename=r'C:\Users\Naman\Desktop\DevanagariHandwrittenCharacterDataset\First programs\hindidigitclass.pkl';
joblib.dump(classifier_neural,filename,compress=9);

