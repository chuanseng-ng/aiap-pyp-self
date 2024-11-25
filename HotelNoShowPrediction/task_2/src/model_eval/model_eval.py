import pandas as pd

from sklearn.metrics import mean_squared_error, r2_score
from typing import Dict


# Evaluate selected models to determine which is more optimized for current dataset
def model_evaluation(
    X_test: pd.DataFrame, Y_test: pd.DataFrame, best_estimator_dict: Dict
):
    ## Initialize dictionary to store results
    eval_result_dict = {}

    for model_name, model in best_estimator_dict.items():
        ### Predict on test set
        Y_predict = model.predict(X_test)
        ### Calculate evaluation metrics
        mse = mean_squared_error(Y_test, Y_predict)
        r2 = r2_score(Y_test, Y_predict)
        ### Store results
        eval_result_dict[model_name] = {"Mean Squared Error": mse, "R^2 Score": r2}

    ## Info -
    ### Mean Squared Error - Measures average squared difference between predicted and actual values
    ### Lower vlaues -> Better performance

    ### R^2 scoore - Indicates proportion of varaince explained by model
    ### Score closer to 1 -> Better fit

    ## Display results
    results_df = pd.DataFrame(eval_result_dict).T
    print(results_df)