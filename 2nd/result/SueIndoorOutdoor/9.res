=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue9
Instances:    26
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
term1(1): class 
term2(1): class 
term3(1): class 
term4(1): class 
term5(1): class 
term6(2): class 
term7(1): class 
term8(2): class 
class(14): 
LogScore Bayes: -100.67084526959846
LogScore BDeu: -216.26493741376635
LogScore MDL: -185.66933419810377
LogScore ENTROPY: -118.8783551686634
LogScore AIC: -159.8783551686634


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          13               50      %
Incorrectly Classified Instances        13               50      %
Kappa statistic                          0.4028
Mean absolute error                      0.1033
Root mean squared error                  0.2189
Relative absolute error                 80.6775 %
Root relative squared error             87.0547 %
Total Number of Instances               26     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0.158      0.7       1         0.824      0.921    Walkingoutside
                 1         0.217      0.375     1         0.545      0.891    WorkingonPC
                 0         0          0         0         0          0.86     Pearson
                 0         0          0         0         0          0.9      Mackay
                 0         0          0         0         0          0.82     Coover
                 1         0.167      0.333     1         0.5        0.917    science
                 0         0          0         0         0          0.86     NewChina
                 0         0          0         0         0          0.82     mu
                 0.5       0.042      0.5       0.5       0.5        0.896    Durham
                 0         0          0         0         0          0.9      Sleep
                 0         0          0         0         0          0.875    Bedroom
                 0         0          0         0         0          0.9      physicsforwomen
                 0         0          0         0         0          0.9      Bus
                 0         0          0         0         0          0.875    WaitingBus
Weighted Avg.    0.5       0.084      0.296     0.5       0.362      0.893

=== Confusion Matrix ===

 a b c d e f g h i j k l m n   <-- classified as
 7 0 0 0 0 0 0 0 0 0 0 0 0 0 | a = Walkingoutside
 0 3 0 0 0 0 0 0 0 0 0 0 0 0 | b = WorkingonPC
 0 1 0 0 0 0 0 0 0 0 0 0 0 0 | c = Pearson
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 | d = Mackay
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 | e = Coover
 0 0 0 0 0 2 0 0 0 0 0 0 0 0 | f = science
 0 1 0 0 0 0 0 0 0 0 0 0 0 0 | g = NewChina
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 | h = mu
 0 1 0 0 0 0 0 0 1 0 0 0 0 0 | i = Durham
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 | j = Sleep
 0 2 0 0 0 0 0 0 0 0 0 0 0 0 | k = Bedroom
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 | l = physicsforwomen
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 | m = Bus
 1 0 0 0 0 0 0 0 1 0 0 0 0 0 | n = WaitingBus


ps: no wifi info
