# Datadrifts

Despite being already adopted in this project for testing purposes, we adopeted **Deepchecks** to also monitor data drifts in our data.

## Deepchecks

The Deepchecks library is utilized in the [deepchecks_datadrift notebook](deepchecks_datadrift.ipynb) in which we monitored two type of drifts:

- **Univariate Drift**: a change in the distribution of individual features over time;

- **Multivariate Drift**: changes occurring simultaneously in multiple features, potentially impacting the relationships among those features that might be overlook by Univariate drift methods.

## Experiments

First of all, we wanted to check whether data drifts could be found if all the songs' features (Name, Artist, Loudness, Liveness, and Energy) were taken in account.

In the **Univariate Drift scenario**, Deepchecks was able to find drifts on all the features as can be seen in the below charts.

![plot](/figures/artist_univariate_feature_drift_full.png?raw=true)
![plot](/figures/loudness_univariate_feature_drift_full.png?raw=true)
![plot](/figures/liveness_univariate_feature_drift_full.png?raw=true)
![plot](/figures/energy_univariate_feature_drift_full.png?raw=true)

We explored feature contributions in the **Multivariate Drift scenario**, trying to understand which specific features drive the observed changes in relationships or correlations between multiple features. The results are shown in the below charts.

![plot](/figures/features_contribution_full.png?raw=true)
![plot](/figures/features_contribution_full_2.png?raw=true)

As shown in the first chart, the **Artist** feature has an **high contribution percentage**: in other words, it plays a significant role in driving the detected multivariate drift. The **Energy** feature, instead, has a **lower contribution percentage**.

We conducted identical checks on the dataset after removing the Name and Artist features. **Univariate drifts** report consistent results with the previous scenario. However, in terms of contribution (**Multivariate Drifts**), there are some differences.

![plot](/figures/features_contribution_numerical.png?raw=true)
![plot](/figures/features_contribution_numerical_2.png?raw=true)

As shown in the first chart, the **Loudness** feature exhibits a **notably high contribution percentage**. This suggests that, in the absence of categorical features, Loudness plays a crucial role in steering the detected multivariate drift. The **Energy** feature, instead, has a **very low contribution percentage** with respect to the case in which we keep all the features.

More information about this tool can be found [here](https://github.com/deepchecks/deepchecks/tree/main).
