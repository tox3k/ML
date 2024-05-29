import preprocessing
import albumentations_data
import model
import matplotlib.pyplot as plt
import torch


def main(path_nii):

    im = preprocessing.get_slices_nii(path_nii) 
    im = preprocessing.preprocessing_nii(im)

    im_transformed = albumentations_data.preprocessing_data(im)
    out = model.interference(im_transformed)

    plt.figure()
    plt.imshow(torch.sigmoid(out.squeeze(0).squeeze(0)) > 0.5, cmap='gray',alpha=1)
    plt.axis('off')
    plt.savefig('tumor.png',transparent=True)

    plt.figure()
    plt.imshow(im_transformed.squeeze(0).squeeze(0), cmap='gray',alpha=1)
    plt.imshow(torch.sigmoid(out.squeeze(0).squeeze(0)) > 0.5, cmap='gray',alpha=0.55)
    plt.axis('off')
    plt.savefig('liver.png',transparent=True)

if __name__ == '__main__':
    main()