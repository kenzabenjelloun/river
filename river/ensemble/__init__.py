"""Ensemble learning.

Broadly speaking, there are two kinds of ensemble approaches. There are those that copy a single
model several times and aggregate the predictions of said copies. This includes bagging as well as
boosting. Then there are those that are composed of an arbitrary list of models, and can therefore
aggregate predictions from different kinds of models.

"""
<<<<<<< HEAD
from .adaptive_random_forest import AdaptiveRandomForestClassifier, AdaptiveRandomForestRegressor
from .aggregated_mondrian_forest import AMFClassifier, AMFRegressor
=======
>>>>>>> 78c1e4f116b4e2ca7956332bf3699acc795896bb
from .bagging import (
    ADWINBaggingClassifier,
    BaggingClassifier,
    BaggingRegressor,
    LeveragingBaggingClassifier,
)
from .boosting import AdaBoostClassifier, ADWINBoostingClassifier, BOLEClassifier
from .ewa import EWARegressor
from .stacking import StackingClassifier
from .streaming_random_patches import SRPClassifier, SRPRegressor
from .voting import VotingClassifier

__all__ = [
    "AdaBoostClassifier",
    "ADWINBaggingClassifier",
    "ADWINBoostingClassifier",
    "AMFClassifier",
    "AMFRegressor",
    "BaggingClassifier",
    "BaggingRegressor",
    "BOLEClassifier",
    "EWARegressor",
    "LeveragingBaggingClassifier",
    "SRPClassifier",
    "SRPRegressor",
    "StackingClassifier",
    "VotingClassifier",
]
