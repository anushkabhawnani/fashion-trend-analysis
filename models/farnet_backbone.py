import torch
import torch.nn as nn # BASE CLASS FOR ALL NEURAL NETWORKS
from torchvision import models

class FaRNetBackbone(nn.Module):

    def __init__(self):

        super().__init__()

        # LOADS PRETRAINED RESNET MODEL ON IMAGENET WHICH CAN ALREADY DETECT EDGES, TEXTURES, SHAPES, OBJECT PARTS
        resnet = models.resnet50(pretrained=True)

        # RESNET CHILDREN HAS MULTIPLE CNN LAYERS LIKE THE CONVOLUTIONAL LAYERS, RELU LAYERS AND MAX POOLING LAYERS
        # THIS CODE REMOVES THE LAST FULLY CONNECTED CLASSIFICATION LAYER
        # AN FCC EXPECTS THE IMAGE TO BE OF A CERTAIN SIZE WHEREAS THE OTHER LAYERS DO NOT SO THEY CAN BE USED ON IMAGES OF DIFFERENT SIZES
        self.backbone = nn.Sequential(*list(resnet.children())[:-1])

        # THIS IS WHERE YOU FREEZE THE BACKBONE AND TO TRAIN ONLY THE HEAD ON OUR SMALLER DATASET
        # DONT UPDATE THE WEIGHTS
        for param in self.backbone.parameters():
            param.requires_grad = False

    def forward(self, x):
        x = self.backbone(x) # FEATURE EXTRACTION
        return x.view(x.size(0), -1)  # (B, 2048) FROM (B, 2048, 1, 1)

# WHAT THIS NETWORK DOES
# ✅ Extracting high-level visual features
# ✅ Producing embeddings for:
# similarity learning
# ranking
# fashion recognition
# face / apparel / object retrieval
# downstream ML models
