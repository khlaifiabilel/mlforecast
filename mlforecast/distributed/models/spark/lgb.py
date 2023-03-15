# AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../nbs/distributed.models.spark.lgb.ipynb.

# %% auto 0
__all__ = ['SparkLGBMForecast']

# %% ../../../../nbs/distributed.models.spark.lgb.ipynb 3
import lightgbm as lgb

try:
    from synapse.ml.lightgbm import LightGBMRegressor
except ModuleNotFoundError:
    import os

    if os.getenv("QUARTO_PREVIEW", "0") == "1" or os.getenv("IN_TEST", "0") == "1":
        LightGBMRegressor = object
    else:
        raise

# %% ../../../../nbs/distributed.models.spark.lgb.ipynb 4
class SparkLGBMForecast(LightGBMRegressor):
    def _pre_fit(self, target_col):
        return self.setLabelCol(target_col)

    def extract_local_model(self, trained_model):
        model_str = trained_model.getNativeModel()
        local_model = lgb.Booster(model_str=model_str)
        return local_model
