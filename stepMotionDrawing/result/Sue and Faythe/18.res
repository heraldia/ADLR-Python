=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue18
Instances:    7
Attributes:   18
              term1
              term2
              term3
              term4
              term5
              term6
              term7
              term8
              term9
              term10
              term11
              term12
              term13
              term14
              term15
              term16
              term17
              class
Test mode:evaluate on training data

=== Classifier model (full training set) ===

Bayes Network Classifier
not using ADTree
#attributes=18 #classindex=17
Network structure (nodes followed by parents)
term1(4): class 
term2(3): class 
term3(3): class 
term4(4): class 
term5(3): class 
term6(1): class 
term7(2): class 
term8(3): class 
term9(2): class 
term10(2): class 
term11(3): class 
term12(2): class 
term13(2): class 
term14(3): class 
term15(2): class 
term16(1): class 
term17(3): class 
class(4): 
LogScore Bayes: -90.71232609234296
LogScore BDeu: -308.79711884833773
LogScore MDL: -255.8575512859983
LogScore ENTROPY: -151.75135831153912
LogScore AIC: -258.7513583115391


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances           7              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0.002 
Root mean squared error                  0.0069
Relative absolute error                  0.5282 %
Root relative squared error              1.6132 %
Total Number of Instances                7     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        study
                 1         0          1         1         1          1        Sleep
                 1         0          1         1         1          1        WorkingonPC
                 1         0          1         1         1          1        church
Weighted Avg.    1         0          1         1         1          1    

=== Confusion Matrix ===

 a b c d   <-- classified as
 2 0 0 0 | a = study
 0 2 0 0 | b = Sleep
 0 0 2 0 | c = WorkingonPC
 0 0 0 1 | d = church

