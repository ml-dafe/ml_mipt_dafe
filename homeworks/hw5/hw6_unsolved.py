import math
import pickle
import random
from typing import List, Tuple

import numpy as np
import torch
from catboost.datasets import msrank_10k
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from tqdm.auto import tqdm


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


class Solution:
    def __init__(self, n_estimators: int = 100, lr: float = 0.5, ndcg_top_k: int = 10,
                 subsample: float = 0.6, colsample_bytree: float = 0.9,
                 max_depth: int = 5, min_samples_leaf: int = 8):
        self.X_train = None
        self.ys_train = None
        self.X_test = None
        self.ys_test = None
        self._prepare_data()

        self.ndcg_top_k = ndcg_top_k
        self.n_estimators = n_estimators  # количество деревьев
        self.lr = lr  # Learning Rate, коэффициент, на который умножаются предсказания каждого нового дерева
        self.max_depth = max_depth  # максимальная глубина
        self.min_samples_leaf = min_samples_leaf  # минимальное количество термальных листьев

        self.subsample = subsample  # доля объектов от выборки
        self.colsample_bytree = colsample_bytree  # доля признаков от выборки

        self.trees: List[DecisionTreeRegressor] = []  # все деревья
        self.all_ndcg: List[float] = []
        self.best_ndcg = float(0.0)

    def _get_data(self) -> List[np.ndarray]:
        train_df, test_df = msrank_10k()

        X_train = train_df.drop([0, 1], axis=1).values
        y_train = train_df[0].values
        query_ids_train = train_df[1].values.astype(int)

        X_test = test_df.drop([0, 1], axis=1).values
        y_test = test_df[0].values
        query_ids_test = test_df[1].values.astype(int)

        return [X_train, y_train, query_ids_train, X_test, y_test, query_ids_test]

    def _prepare_data(self) -> None:
        (X_train, y_train, self.query_ids_train,
            X_test, y_test, self.query_ids_test) = self._get_data()
        # допишите ваш код здесь
        pass

    def _scale_features_in_query_groups(self, inp_feat_array: np.ndarray,
                                        inp_query_ids: np.ndarray) -> np.ndarray:
        # допишите ваш код здесь 
        pass

    def _train_one_tree(self, cur_tree_idx: int,
                        train_preds: torch.FloatTensor
                        ) -> Tuple[DecisionTreeRegressor, np.ndarray]:
        """
        Метод для тренировки одного дерева.

        @cur_tree_idx: номер текущего дерева, который предлагается использовать в качестве random_seed для того,
        чтобы алгоритм был детерминирован.
        @train_preds: суммарные предсказания всех предыдущих деревьев (для расчёта лямбд).
        @return: это само дерево и индексы признаков, на которых обучалось дерево
        """
        # допишите ваш код здесь
        pass

    def _calc_data_ndcg(self, queries_list: np.ndarray,
                        true_labels: torch.FloatTensor, preds: torch.FloatTensor) -> float:
        """ Расчёт метрики по набору данных """
        # допишите ваш код здесь
        pass

    def fit(self):
        """
        генеральный метод обучения K деревьев, каждое из которых тренируется
        с использованием метода _train_one_tree
        """
        set_seed(0)
        # допишите ваш код здесь
        pass

    def predict(self, data: torch.FloatTensor) -> torch.FloatTensor:
        # допишите ваш код здесь
        pass

    def _compute_lambdas(self, y_true: torch.FloatTensor, y_pred: torch.FloatTensor) -> torch.FloatTensor:
        # допишите ваш код здесь
        pass

    def _ndcg_k(self, ys_true, ys_pred, ndcg_top_k) -> float:
        # допишите ваш код здесь
        pass

    def save_model(self, path: str):
        # допишите ваш код здесь
        pass

    def load_model(self, path: str):
        # допишите ваш код здесь
        pass
