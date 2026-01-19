from enum import Enum


class PredictionModelType(str, Enum):
    LINEAR_REGRESSION = "linear_regression"
    RANDOM_FOREST = "random_forest"
    MULTILAYER_PERCEPTRON = "multilayer_perceptron"
    GRADIENT_BOOST_TREE = "gradient_boost_tree"

    @classmethod
    def get_default(cls) -> str:
        return cls.GRADIENT_BOOST_TREE.name.lower()
