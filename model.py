import torch
from torchvision.models.segmentation import deeplabv3_resnet50
import torch.nn as nn
import torch.optim as optim

def interference(im):
    model = deeplabv3_resnet50(num_classes=1,weights=None)
    model.backbone.conv1 = torch.nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3)

    model.load_state_dict(torch.load('best_model_DeepLabV3.pth',map_location='cpu'))

    model.eval()

    with torch.no_grad():
        out = model(im)['out'].detach().cpu()
    
    return out


