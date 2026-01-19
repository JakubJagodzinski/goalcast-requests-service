import random
from enum import Enum


class PredictionModelType(str, Enum):
    LINEAR_REGRESSION = "linear_regression"
    RANDOM_FOREST = "random_forest"
    MULTILAYER_PERCEPTRON = "multilayer_perceptron"
    GRADIENT_BOOST_TREE = "gradient_boost_tree"

    @classmethod
    def get_list(cls) -> list[str]:
        return [model.value for model in cls]

    @classmethod
    def get_random(cls) -> str:
        return random.choice(cls.get_list())
