import os
import yaml
import torch
import torch.optim as optim
from torch.optim.lr_scheduler import LambdaLR, StepLR

from utils_word2vec.model import CBOW_Model, SkipGram_Model


def get_model_class(model_name: str):
    if model_name == "cbow":
        return CBOW_Model
    elif model_name == "skipgram":
        return SkipGram_Model
    else:
        raise ValueError("Choose model_name from: cbow, skipgram")
        return


def get_optimizer_class(name: str):
    if name == "Adam":
        return optim.Adam
    else:
        raise ValueError("Choose optimizer from: Adam")
        return
    

def get_lr_scheduler(name, optimizer, total_epochs: int):
    """
    Scheduler to linearly decrease learning rate, 
    so thatlearning rate after the last epoch is 0.
    """
    if name == 'LambdaLR':
        lr_lambda = lambda epoch: (total_epochs - epoch) / total_epochs
        lr_scheduler = LambdaLR(optimizer, lr_lambda=lr_lambda)
    elif name == 'StepLR':
        lr_scheduler = StepLR(optimizer, step_size=3, gamma=0.5)
    else:
        print("Wrong Lr Scheduler name, using default StepLR")
        lr_scheduler = StepLR(optimizer, step_size=3, gamma=0.5)
    return lr_scheduler


def save_config(config: dict, model_dir: str):
    """Save config file to `model_dir` directory"""
    config_path = os.path.join(model_dir, "config.yaml")
    with open(config_path, "w") as stream:
        yaml.dump(config, stream)
        
        
def save_vocab(vocab, model_dir: str):
    """Save vocab file to `model_dir` directory"""
    vocab_path = os.path.join(model_dir, "vocab.pt")
    torch.save(vocab, vocab_path)


def upload_trained_params(model, optimizer, lr_scheduler, path, device):
    print(f"==> loading checkpoint '{path}'")

    checkpoint = torch.load(path, map_location=device)
    current_epoch = checkpoint['epoch']
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    for state in optimizer.state.values():
        for k, v in state.items():
            if isinstance(v, torch.Tensor):
                state[k] = v.to(device)

    lr_scheduler.load_state_dict(checkpoint['lr_scheduler_state_dict'])
    print(f"==> loaded checkpoint {current_epoch}\n")
    return current_epoch, model, optimizer, lr_scheduler


def get_device(
):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('Using device:', device)
    print()

    # Additional Info when using cuda
    if device.type == 'cuda':
        print(torch.cuda.get_device_name(0))
        print('Memory Usage:')
        print('Allocated:', round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1), 'GB')
        print('Cached:   ', round(torch.cuda.memory_reserved(0) / 1024 ** 3, 1), 'GB', '\n')
    return device
    