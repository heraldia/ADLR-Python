=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue15
Instances:    12
Attributes:   15
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
              class
Test mode:evaluate on training data

=== Classifier model (full training set) ===

Bayes Network Classifier
not using ADTree
#attributes=15 #classindex=14
Network structure (nodes followed by parents)
term1(5): class 
term2(2): class 
term3(2): class 
term4(5): class 
term5(4): class 
term6(2): class 
term7(2): class 
term8(4): class 
term9(2): class 
term10(2): class 
term11(4): class 
term12(4): class 
term13(1): class 
term14(3): class 
class(8): 
LogScore Bayes: -166.29068936254285
LogScore BDeu: -859.629802623327
LogScore MDL: -614.441551074695
LogScore ENTROPY: -327.43483302418156
LogScore AIC: -558.4348330241809


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          12              100      %
Incorrectly Classified Instances         0                0      %
Kappa statistic                          1     
Mean absolute error                      0.0072
Root mean squared error                  0.024 
Relative absolute error                  3.3613 %
Root relative squared error              7.3649 %
Total Number of Instances               12     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        WorkingonPC
                 1         0          1         1         1          1        Gettingup
                 1         0          1         1         1          1        vocabulary
                 1         0          1         1         1          1        Studying
                 1         0          1         1         1          1        Dinner
                 1         0          1         1         1          1        Sleep
                 1         0          1         1         1          1        chat
                 1         0          1         1         1          1        PlayingGo
Weighted Avg.    1         0          1         1         1          1    

=== Confusion Matrix ===

 a b c d e f g h   <-- classified as
 1 0 0 0 0 0 0 0 | a = WorkingonPC
 0 2 0 0 0 0 0 0 | b = Gettingup
 0 0 2 0 0 0 0 0 | c = vocabulary
 0 0 0 1 0 0 0 0 | d = Studying
 0 0 0 0 1 0 0 0 | e = Dinner
 0 0 0 0 0 3 0 0 | f = Sleep
 0 0 0 0 0 0 1 0 | g = chat
 0 0 0 0 0 0 0 1 | h = PlayingGo

