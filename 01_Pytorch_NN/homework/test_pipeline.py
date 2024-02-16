import pytest
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import CIFAR10


@pytest.fixture
def train_dataset():
    # note: реализуйте и протестируйте подготовку данных (скачиание и препроцессинг)
    pass


@pytest.mark.parametrize(["device"], [["cpu"], ["cuda"]])
def test_train_on_one_batch(device, train_dataset):
    # note: реализуйте и протестируйте один шаг обучения вместе с метрикой
    pass

def test_training():
    # note: реализуйте и протестируйте полный цикл обучения модели (обучение, валидацию, логирование, сохранение артефактов)
    pass