import torch
from torchvision import transforms
from fastai.vision import create_cnn_model, models

class Evaluator():
    def __init__(self, model, transforms=None, device="cpu", confidence=1.5):
        self.model = model
        self.transforms = transforms
        self.device = device

    def __call__(self, inputs):
        # No need to update gradients
        with torch.no_grad():
            # Put on device and eval mode
            self.model.to(self.device)
            self.model.eval()

            # Evaluate
            if isinstance(inputs, list):
                return self._evaluate_list(inputs)
            else:
                return self._evaluate_one(inputs)

        return out

    def _evaluate_one(self, x):
        # Do transforms
        if self.transforms:
            x = self.transforms(x)

        # Run through model
        x = torch.unsqueeze(x, 0).to(self.device)
        out = self.model(x)
        out = torch.squeeze(out, 0).to("cpu")

        # Interpret results
        return self._interpret(out)

    def _evaluate_list(self, xs):
        # Do transforms
        if self.transforms:
            xs = [self.transforms(x) for x in xs]

        # Run through model
        xs = torch.stack(xs).to(self.device)
        outs = self.model(xs)
        outs = outs.to("cpu")

        # Interpret results
        return [self._interpret(out) for out in outs]

    def _interpret(self, out):
        # Find which class is highest
        value, idx = out.max(0)

        # If model is not confident, don't make a prediction
        if value < 1.5:
            return "Not Sure"

        # Return class name
        if idx == 0:
            return "Parasitized"

        return "Uninfected"

# Load model
model = create_cnn_model(models.resnet18, 2)
checkpoint = torch.load("./malaria.pth")
model.load_state_dict(checkpoint['model'])

# Define transforms
tfms = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Define evaluator
malaria_evaluator = Evaluator(model, transforms=tfms)