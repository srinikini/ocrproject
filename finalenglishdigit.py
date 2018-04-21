def final_englishdigit():
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
    filename=r'C:\Users\Roopal\Desktop\Project\English digit\englishdigitclass.pkl'
    classifier = joblib.load(filename)
    data_test=np.zeros((1,196))
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
    for i in range(0,26,2):
        for j in range(0,26,2):
            data_test[0,count]=im[i,j]+im[i+1,j]+im[i,j+1]+im[i+1,j+1];
            count=count+1;
    count=0;
    output=classifier.predict(data_test);
    document.add_paragraph(str(output))
    document.save('English.docx')
    plt.subplot(2,1,1)
    plt.imshow(im)
    plt.subplot(2,1,2)
    path2=r'C:\Users\Roopal\Desktop\Project\English digit\training\%d\(1).png'%(output)
    im1=mimage.imread(path2)
    plt.imshow(im1)
    plt.show()
