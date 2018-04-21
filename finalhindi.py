def final_predict():
    from sklearn .externals import joblib
    import matplotlib.image as  mimage
    import numpy as np
    import matplotlib.pyplot as plt
    import random
    import cv2
    from skimage import util
    from sklearn import metrics
    from collections import Counter
    from PIL import Image
    from docx import Document
    a=['0',u'\u0915',u'\u0916',u'\u0917',u'\u0918',u'\u0919',u'\u091A',u'\u091B',u'\u091C',u'\u091D',u'\u091E',u'\u091F',u'\u0920',u'\u0921',u'\u0922',u'\u0923',u'\u0924',u'\u0925',u'\u0926',u'\u0927',u'\u0928',u'\u092A',u'\u092B',u'\u092C',u'\u092D',u'\u092E',u'\u092F',u'\u0930',u'\u0932',u'\u0935',u'\u0936',u'\u0937',u'\u0938',u'\u0939','ksha','tra','jya']
    filename=r'C:\Users\Roopal\Desktop\Project\Hindi alphabets\hindialphabetsclass.pkl'
    classifier = joblib.load(filename)
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
    im = util.invert(im)
    im=im[:,:,0]
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
    path2=r'C:\Users\Roopal\Desktop\Project\Hindi alphabets/Train1/character (%d)/(1).png'%(output)
    im1=mimage.imread(path2)
    plt.imshow(im1)
    plt.show()
