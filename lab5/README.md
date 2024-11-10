# Support-Vector Machines
Using ```sklearn.svm```, study the principle of the method. Focus on setting up the parameters of the algorithm and their connection with the theoretical part of the algorithm and its impact on its operation

# Method description
Support vector machine (SVM) is a popular algorithm for classification and regression tasks that searches for a hyperplane that maximally separates classes in the feature space. In nonlinear cases, different kernels are used to find the optimal hyperplane, which transforms the original feature space into a higher-dimensional space where the data can be separated.
# Research parameters
The following parameters were chosen for the analysis:
1) ```C``` - A regularisation parameter that determines the trade-off between the maximum distance to the separating hyperplane and the number of misclassified points. Low values of C allow for more errors, which can improve the generalisability of the model, while high values of C promote a tight separation of the data.

2) ```Kernel``` The kernel that defines the type of function to transform the feature space. Kernels explored:
- ```linear``` - A linear kernel suitable for linearly separated data;
- ```Radial-basis function``` - a radial-basis function that allows you to create nonlinear boundaries;
- ```poly``` is a polynomial kernel that takes into account the degree of the polynomial function in the construction of the separation boundary.

3) ```gamma``` - A parameter that controls the distance of influence of individual data points for the ```rbf``` and ```poly``` kernels. The gamma value determines how far the points will affect the hyperplane:
- ```scale``` is a standard setting that automatically calculates the value depending on the data;
- ```auto``` - the value is inversely proportional to the number of features, which may be better suited for high-dimensional data.

![image](https://github.com/user-attachments/assets/e9aadb16-1a3a-4842-8819-2bbfd83f2968)

```bash
C=0.1, kernel=linear, gamma=scale -> Accuracy: 1.00
C=0.1, kernel=linear, gamma=auto -> Accuracy: 1.00
C=0.1, kernel=rbf, gamma=scale -> Accuracy: 0.98
C=0.1, kernel=rbf, gamma=auto -> Accuracy: 1.00
C=0.1, kernel=poly, gamma=scale -> Accuracy: 1.00
C=0.1, kernel=poly, gamma=auto -> Accuracy: 1.00
C=1, kernel=linear, gamma=scale -> Accuracy: 1.00
C=1, kernel=linear, gamma=auto -> Accuracy: 1.00
C=1, kernel=rbf, gamma=scale -> Accuracy: 1.00
C=1, kernel=rbf, gamma=auto -> Accuracy: 1.00
C=1, kernel=poly, gamma=scale -> Accuracy: 0.98
C=1, kernel=poly, gamma=auto -> Accuracy: 1.00
C=10, kernel=linear, gamma=scale -> Accuracy: 0.98
C=10, kernel=linear, gamma=auto -> Accuracy: 0.98
C=10, kernel=rbf, gamma=scale -> Accuracy: 1.00
C=10, kernel=rbf, gamma=auto -> Accuracy: 1.00
C=10, kernel=poly, gamma=scale -> Accuracy: 1.00
C=10, kernel=poly, gamma=auto -> Accuracy: 1.00
```

# Analysis of the results
- Influence of the parameter ```C```: As the value of C increased, there was a tendency for classification errors to decrease, but this can lead to overtraining of the model when it remembers individual points, which reduces its generalisability.
- ```Kernel``` impact: The linear kernel performed well for linearly separated data, but for more complex data distributions, the radial basis function (rbf) proved to be more effective, providing flexible separation limits.
- The influence of ```gamma```: When varying the gamma parameter for nonlinear kernels, it was observed that high gamma values resulted in more localised boundaries, which may help for well-separated classes, but not for noisy data where it causes overfitting.

# Conclusions.
The SVM algorithm is flexible and efficient for classification, but tuning its parameters has a significant impact on performance. Selecting optimal values of the ```C```, ```kernel```, and ```gamma``` parameters allows for better generalisation of the model, which is confirmed by changes in the uncertainty and accuracy matrix.

