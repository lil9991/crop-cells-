# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:57:33 2021

@author: Linda7lll
"""

# %%

# .ini

import configparser
from PIL import Image
import glob
import os.path  

# %%
config = configparser.ConfigParser()


# %%

# save images
def save(category,num,datasets):
    
     if(datasets == 'Comparison Detector'):
    
        if ((category == "NIL") or (category == "ACTINOMYCES") or (category == "HERPS") or (category == "FLORA") or (category == "CANDIDA") or (category == "TRICHOMONAS")or (category == "Metaplastic") or (category == "Parabasal") or (category == "Superficial-Intermediate")):
         crop.save("./Train/0/"+datasets+"_N_"+str(num)+"_"+category+".bmp")

        else :
         crop.save("./Train/1/"+datasets+"_P_"+str(num)+"_"+category+".bmp")

    

#%%

z_file = 0
total_file =0
total_cell = 0  # total cell
num = 0  # index cell

#%%
  

for filename in glob.glob('./train-bmp/*.bmp'):
    
    im = Image.open(filename)    
    inifile_name = os.path.splitext(filename)[0] + '.ini'
    total_file +=1
    #print(inifile_name)
    
   
    #read ini file
    read_s = config.read(inifile_name) 
    
    
    # category, cell_num
    datasets = config.get("main", "dataset")
    cell_number = config.get("main", "cell_number")
    cell_num = int(cell_number)
    print("\nfile_num: {}, Cell_num: {}, file_dataset: {}".format(total_file,cell_num,datasets))
    
    total_cell += + cell_num
    

    if cell_num == 0:
       category1 = config.get("main", "category")
       z_file += 1


   #cell_number, coordinate
    for a in range(1, cell_num+1):

        print("\nCell_"+str(a)+" Coordinate: ")
        left = config.get('cell_'+str(a), 'left')
        l = float(left)

        top = config.get('cell_'+str(a), 'top')
        t = float(top)

        right = config.get('cell_'+str(a), 'right')
        r = float(right)

        bottom = config.get('cell_'+str(a), 'bottom')
        b = float(bottom)

        print("left:", l, ", top:", t, ", right:", r, ", bottom:", b)

        
        # print cell_category, cell_num
        num = num+1
        print("Cell_Last_num:", num)
        
        category = config.get('cell_'+str(a), 'category')
        print("Cell_Category: ", category)
        print("dataset: ",datasets)
    

        # crop and save      
        area = (l, t, r, b)
        crop = im.crop(area)
        save(category, num, datasets)
        

print("\n\nnumber of file: ", total_file)  # toplam dosya sayısı
print("Total cells: ", total_cell)  # toplam hücre sayısı
print("number of zero_file:", z_file)  # içinde hücre olmayan dosya sayısı

# %%

