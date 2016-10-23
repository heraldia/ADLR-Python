=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue24
Instances:    93
Attributes:   24
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
              term18
              term19
              term20
              term21
              term22
              term23
              class
Test mode:evaluate on training data

=== Classifier model (full training set) ===

Bayes Network Classifier
not using ADTree
#attributes=24 #classindex=23
Network structure (nodes followed by parents)
term1(1): class 
term2(1): class 
term3(1): class 
term4(1): class 
term5(5): class 
term6(3): class 
term7(2): class 
term8(2): class 
term9(3): class 
term10(1): class 
term11(2): class 
term12(1): class 
term13(1): class 
term14(2): class 
term15(2): class 
term16(1): class 
term17(1): class 
term18(2): class 
term19(1): class 
term20(1): class 
term21(1): class 
term22(1): class 
term23(1): class 
class(15): 
LogScore Bayes: -674.9654437730076
LogScore BDeu: -1429.962653824496
LogScore MDL: -1262.4085983778418
LogScore ENTROPY: -754.7574551446753
LogScore AIC: -978.7574551446766


Time taken to build model: 0.04 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          50               53.7634 %
Incorrectly Classified Instances        43               46.2366 %
Kappa statistic                          0.4617
Mean absolute error                      0.0741
Root mean squared error                  0.1942
Relative absolute error                 61.6505 %
Root relative squared error             79.4232 %
Total Number of Instances               93     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 0.875     0          1         0.875     0.933      0.952    WorkingonPC
                 0.6       0.034      0.5       0.6       0.545      0.855    laundry
                 1         0.057      0.5       1         0.667      0.966    Gettingup
                 0         0          0         0         0          0.914    Midnightsnack
                 0.5       0          1         0.5       0.667      0.945    Bathroomflushing
                 0.167     0.025      0.5       0.167     0.25       0.873    study
                 0         0          0         0         0          0.974    Bathroom
                 0.571     0.012      0.8       0.571     0.667      0.98     Boiling
                 0.333     0          1         0.333     0.5        0.969    Nap
                 0         0          0         0         0          0.966    Sleep
                 1         0.044      0.429     1         0.6        0.978    cook
                 0         0          0         0         0          0.883    Eating
                 0.905     0.361      0.422     0.905     0.576      0.817    WorkingonPCathome
                 1         0.011      0.75      1         0.857      0.994    bake
                 0.333     0.011      0.667     0.333     0.444      0.847    WalkingAtHome
Weighted Avg.    0.538     0.093      0.495     0.538     0.464      0.903

=== Confusion Matrix ===

  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o   <-- classified as
  7  0  0  0  0  0  0  0  0  0  0  0  1  0  0 |  a = WorkingonPC
  0  3  0  0  0  0  0  0  0  0  0  0  1  1  0 |  b = laundry
  0  0  5  0  0  0  0  0  0  0  0  0  0  0  0 |  c = Gettingup
  0  0  0  0  0  1  0  0  0  0  0  0  2  0  1 |  d = Midnightsnack
  0  0  0  0  1  1  0  0  0  0  0  0  0  0  0 |  e = Bathroomflushing
  0  1  0  0  0  2  0  0  0  0  0  0  9  0  0 |  f = study
  0  1  4  0  0  0  0  0  0  0  0  0  0  0  0 |  g = Bathroom
  0  0  0  0  0  0  0  4  0  0  3  0  0  0  0 |  h = Boiling
  0  0  0  0  0  0  0  0  1  0  0  0  2  0  0 |  i = Nap
  0  0  0  0  0  0  0  0  0  0  0  0  6  0  0 |  j = Sleep
  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0 |  k = cook
  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0 |  l = Eating
  0  1  1  0  0  0  0  0  0  0  0  0 19  0  0 |  m = WorkingonPCathome
  0  0  0  0  0  0  0  0  0  0  0  0  0  3  0 |  n = bake
  0  0  0  0  0  0  0  1  0  0  1  0  2  0  2 |  o = WalkingAtHome

  43-1-2-1-2-1-1-1-9-5-3-2-6-3-1 = 5 / 93 = 5.37 % location mcr
  by audio recognition 1/93 = 98.9%
1+1 +1+2 4+1 +1

