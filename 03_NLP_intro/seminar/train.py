import argparse
import yaml
import os
import torch
import torch.nn as nn

from utils_word2vec.dataloader import get_dataloader_and_vocab
from utils_word2vec.trainer import Trainer
from utils_word2vec.helper import (
    get_model_class,
    get_optimizer_class,
    get_lr_scheduler,
    save_config,
    save_vocab,
    get_device,
    upload_trained_params,
)


def train(config):
    if not os.path.exists(config["model_dir"]):
        os.makedirs(config["model_dir"])

    device = get_device()

    vocab = None
    if config["continue_training"] and os.path.isfile(config["continue_training"]+'vocab.pt'):
        print(f"============ Using saved Vocab ============\n {config['continue_training']+'vocab.pt'},\n")
        vocab = torch.load(config["continue_training"]+'vocab.pt')

    train_dataloader, vocab = get_dataloader_and_vocab(
        model_name=config["model_name"],
        ds_name=config["dataset"],
        ds_type="train",
        data_dir=config["data_dir"],
        batch_size=config["train_batch_size"],
        shuffle=config["shuffle"],
        vocab=vocab,
    )

    val_dataloader, _ = get_dataloader_and_vocab(
        model_name=config["model_name"],
        ds_name=config["dataset"],
        ds_type="valid",
        data_dir=config["data_dir"],
        batch_size=config["val_batch_size"],
        shuffle=config["shuffle"],
        vocab=vocab,
    )

    vocab_size = len(vocab.get_stoi())
    print(f"Vocabulary size: {vocab_size}")

    model_class = get_model_class(config["model_name"])
    model = model_class(vocab_size=vocab_size)
    criterion = nn.CrossEntropyLoss()

    optimizer_class = get_optimizer_class(config["optimizer"])
    optimizer = optimizer_class(model.parameters(), lr=config["learning_rate"])
    lr_scheduler = get_lr_scheduler(config['lr_scheduler'], optimizer, config["epochs"])

    current_epoch = 0
    if config["continue_training"] and os.path.isfile(config["continue_training"] + 'last.pt'):
        print(f"============ Using pretrained params ============\n {config['continue_training'] + 'last.pt'}")
        current_epoch, model, optimizer, lr_scheduler = upload_trained_params(
            model,
            optimizer,
            lr_scheduler,
            path=config['continue_training'] + 'last.pt',
            device=device,
        )
        # print(print(next(model.parameters()).device),
        #       print(next(optimizer.parameters()).device))

    trainer = Trainer(
        model=model,
        epochs=config["epochs"],
        train_dataloader=train_dataloader,
        train_steps=config["train_steps"],
        val_dataloader=val_dataloader,
        val_steps=config["val_steps"],
        criterion=criterion,
        optimizer=optimizer,
        checkpoint_frequency=config["checkpoint_frequency"],
        lr_scheduler=lr_scheduler,
        device=device,
        model_dir=config["model_dir"],
        model_name=config["model_name"],
        current_epoch=current_epoch,
    )

    trainer.train()
    print("Training finished.")

    trainer.save_loss()
    save_vocab(vocab, config["model_dir"])
    save_config(config, config["model_dir"])
    print("Model artifacts saved to folder:", config["model_dir"])
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default="./config.yaml", type=str, help='path to yaml config')
    args = parser.parse_args()
    
    with open(args.config, 'r') as stream:
        config = yaml.safe_load(stream)
    train(config)