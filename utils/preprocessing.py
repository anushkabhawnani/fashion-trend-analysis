from torchvision import transforms

transform = transforms.Compose([

    # RESIZE ALL IMAGES TO 224X224
    transforms.Resize((224, 224)),

    # CONVERTS THE SHAPE OF THE TENSOR INTO A DEEP LEARNING FORMAT OF C X W X H INSTEAD OF W X H X C, IT ALSO THE IMAGES FROM 0-255 TO 0-1 BECAUSE MULTIPLE MODELS ARE TRAINED ON THIS NORMALIZATION DATA AND THE INPUT FORMATS NEED TO MATCH AS WELL
    # Converts a PIL Image or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]
    transforms.ToTensor(),

    # THESE EXACT VALUES COMES FROM THE MEAN AND STANDARD FROM IMAGENET MODEL THAT WE ARE USING HERE, IT IS NECESSARY TO USE THE SAME MEAN AND STANDARD VALUES OF THE RGB THAT YOUR MODEL WAS TRAINED ON
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
