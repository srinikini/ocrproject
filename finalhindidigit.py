def final_predict():
    from sklearn .externals import joblib
    import matplotlib.image as  mimage
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    from sklearn import metrics
    from collections import Counter
    from skimage import util
    import cv2
    from PIL import Image
    from docx import Document
    filename=r'C:\Users\Roopal\Desktop\Project\Hindi Digit\hindidigitclass.pkl'
    classifier = joblib.load(filename)
    a=[u'\u0966',u'\u0967',u'\u0968',u'\u0969',u'\u096A',u'\u096B',u'\u096C',u'\u096D',u'\u096E',u'\u096F']
    data_test=np.zeros((1,256))
    count=0;
    document=Document()
    path='image1.png'
    path2='Untitled'
    im = Image.open(path)
    im = im.resize((32, 32), Image.ANTIALIAS)
    ext = ".png"
    im.save(path2 + ext)
    im=mimage.imread(path2 + '.png')
    im=im[:,:,0]
    im = util.invert(im)
    for i in range(0,30,2):
     for j in range(0,30,2):
         data_test[0,count]=im[i,j]+im[i+1,j]+im[i,j+1]+im[i+1,j+1];
         count=count+1;
    count=0;
    output=classifier.predict(data_test);
    document.add_paragraph(a[int(output)])
    document.save('Hindi.docx')
    plt.subplot(2,1,1)
    plt.imshow(im)
    plt.subplot(2,1,2)
    path2=r'C:\Users\Roopal\Desktop\Project\Hindi Digit\TrainHDigit/digit_%d/(30).png'%(output)
    im1=mimage.imread(path2)
    plt.imshow(im1)
    plt.show()
