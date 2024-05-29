import numpy as np
import nibabel as nib

def get_transpose(image,x=0,y=1,z=2):
    return image.transpose(x,y,z)

def get_slices_nii(image):
    
    image_nii = nib.load(image).get_fdata()    
    image_nii = get_transpose(image_nii,2,1,0)
    
    return image_nii[-1].astype('float32')
    
def preprocessing_nii(image):
    image[image < 0] = 0
    image = image/np.max(image)
    
    return image


