import albumentations as A
from albumentations.pytorch import ToTensorV2

def preprocessing_data(image):
    data_transforms = A.Compose([
        A.Resize(256, 256),  # Изменение размера до 256x256 пикселей
        ToTensorV2()  # Преобразование в тензор PyTorch
    ])

    # Применение аугментаций к изображению
    data_transformed = data_transforms(image=image)
    
    im_transformed = data_transformed['image']
        
    im_transformed = im_transformed.unsqueeze(0).float()
    
    return im_transformed