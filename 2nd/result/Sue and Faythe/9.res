=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue9
Instances:    33
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
term1(2): class 
term2(1): class 
term3(1): class 
term4(1): class 
term5(1): class 
term6(3): class 
term7(2): class 
term8(2): class 
class(17): 
LogScore Bayes: -179.42967018466175
LogScore BDeu: -504.7107694235992
LogScore MDL: -405.1276414640486
LogScore ENTROPY: -228.5540096099911
LogScore AIC: -329.55400960999134


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          22               66.6667 %
Incorrectly Classified Instances        11               33.3333 %
Kappa statistic                          0.6219
Mean absolute error                      0.0701
Root mean squared error                  0.1762
Relative absolute error                 64.9045 %
Root relative squared error             76.1655 %
Total Number of Instances               33     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0.115      0.7       1         0.824      0.953    Walkingoutside
                 1         0.033      0.75      1         0.857      0.983    WorkingonPC
                 0         0          0         0         0          0.953    Pearson
                 1         0.031      0.5       1         0.667      0.984    Mackay
                 0         0          0         0         0          0.859    Coover
                 1         0          1         1         1          1        Driving
                 1         0.069      0.667     1         0.8        0.983    Studying
                 1         0.065      0.5       1         0.667      0.968    Bedroom
                 0         0          0         0         0          0.953    NewChina
                 0         0          0         0         0          0.984    mu
                 0         0          0         0         0          0.968    Dinner
                 0.5       0          1         0.5       0.667      0.976    Durham
                 0         0          0         0         0          0.984    Sleep
                 1         0.065      0.5       1         0.667      0.968    science
                 0         0          0         0         0          0.953    physicsforwomen
                 0         0          0         0         0          0.953    Bus
                 0.5       0          1         0.5       0.667      0.879    WaitingBus
Weighted Avg.    0.667     0.045      0.525     0.667     0.562      0.96 

=== Confusion Matrix ===

 a b c d e f g h i j k l m n o p q   <-- classified as
 7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | a = Walkingoutside
 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | b = WorkingonPC
 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 | c = Pearson
 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 | d = Mackay
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | e = Coover
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 | f = Driving
 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 | g = Studying
 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 | h = Bedroom
 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | i = NewChina
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | j = mu
 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 | k = Dinner
 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 | l = Durham
 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 | m = Sleep
 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 | n = science
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 | o = physicsforwomen
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 | p = Bus
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 | q = WaitingBus

