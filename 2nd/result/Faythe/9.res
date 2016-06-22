=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Faythe
Instances:    7
Attributes:   9
              term1
              term2
              term3
              term4
              term5
              term6
              term7
              term8
              class
Test mode:evaluate on training data

=== Classifier model (full training set) ===

Bayes Network Classifier
not using ADTree
#attributes=9 #classindex=8
Network structure (nodes followed by parents)
term1(3): class 
term2(3): class 
term3(3): class 
term4(3): class 
term5(2): class 
term6(1): class 
term7(1): class 
term8(3): class 
class(3): 
LogScore Bayes: -36.266539648224246
LogScore BDeu: -95.36833885163065
LogScore MDL: -88.99688845898659
LogScore ENTROPY: -54.94346085051861
LogScore AIC: -89.94346085051862


Time taken to build model: 0 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances           7              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0.0002
Root mean squared error                  0.0003
Relative absolute error                  0.0533 %
Root relative squared error              0.0584 %
Total Number of Instances                7     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        study
                 1         0          1         1         1          1        Dinner
                 1         0          1         1         1          1        Driving
Weighted Avg.    1         0          1         1         1          1    

=== Confusion Matrix ===

 a b c   <-- classified as
 4 0 0 | a = study
 0 2 0 | b = Dinner
 0 0 1 | c = Driving

