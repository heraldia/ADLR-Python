=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Sue24Outdoor
Instances:    185
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
term4(7): class 
term5(2): class 
term6(1): class 
term7(4): class 
term8(8): class 
term9(1): class 
term10(1): class 
term11(9): class 
term12(1): class 
term13(1): class 
term14(3): class 
term15(1): class 
term16(17): class 
term17(11): class 
term18(3): class 
term19(1): class 
term20(3): class 
term21(1): class 
term22(1): class 
term23(5): class 
class(27): 
LogScore Bayes: -2782.1271374701673
LogScore BDeu: -11736.2028307593
LogScore MDL: -8839.01627137537
LogScore ENTROPY: -4472.188623697343
LogScore AIC: -6145.188623697351


Time taken to build model: 0.02 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances         148               80      %
Incorrectly Classified Instances        37               20      %
Kappa statistic                          0.7737
Mean absolute error                      0.018 
Root mean squared error                  0.1125
Relative absolute error                 26.9648 %
Root relative squared error             61.745  %
Total Number of Instances              185     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        Gilman
                 1         0          1         1         1          1        hyvee
                 0.8       0          1         0.8       0.889      0.988    TJtea
                 1         0          1         1         1          1        durham
                 0.737     0          1         0.737     0.848      0.96     ParksLibrary
                 0.625     0.017      0.625     0.625     0.625      0.983    Coover
                 1         0          1         1         1          1        lib
                 0.844     0.15       0.644     0.844     0.731      0.926    Bus
                 1         0          1         1         1          1        Sweeney
                 1         0.017      0.8       1         0.889      0.996    Pearson
                 1         0          1         1         1          1        Bar
                 0.875     0          1         0.875     0.933      0.934    Science
                 1         0          1         1         1          1        VisitFriend
                 1         0          1         1         1          1        NewChina
                 1         0          1         1         1          1        Howe
                 0.5       0          1         0.5       0.667      1        Mackay
                 0.667     0.017      0.571     0.667     0.615      0.992    Hub
                 1         0          1         1         1          1        Lied
                 1         0          1         1         1          1        ScienceII
                 1         0          1         1         1          1        mu
                 1         0          1         1         1          1        MusicHall
                 1         0          1         1         1          1        Sleep
                 1         0          1         1         1          1        blackengineering
                 0         0          0         0         0          1        mogoliangrill
                 0.923     0          1         0.923     0.96       0.98     Atanasoff
                 1         0          1         1         1          1        LebaronHall
                 0.417     0.043      0.588     0.417     0.488      0.924    WaitingBus
Weighted Avg.    0.8       0.045      0.812     0.8       0.795      0.962

=== Confusion Matrix ===

  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z aa   <-- classified as
  2  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  a = Gilman
  0  2  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  b = hyvee
  0  0  4  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  c = TJtea
  0  0  0  2  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  d = durham
  0  0  0  0 14  1  0  4  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  e = ParksLibrary
  0  0  0  0  0  5  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  2 |  f = Coover
  0  0  0  0  0  0  3  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  g = lib
  0  0  0  0  0  0  0 38  0  1  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  5 |  h = Bus
  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  i = Sweeney
  0  0  0  0  0  0  0  0  0 12  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  j = Pearson
  0  0  0  0  0  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  k = Bar
  0  0  0  0  0  0  0  1  0  0  0  7  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  l = Science
  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  m = VisitFriend
  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0 |  n = NewChina
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0  0  0  0  0  0  0 |  o = Howe
  0  0  0  0  0  0  0  2  0  0  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0  0  0 |  p = Mackay
  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0  0  4  0  0  0  0  0  0  0  0  0  0 |  q = Hub
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0 |  r = Lied
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0  0  0 |  s = ScienceII
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0  0 |  t = mu
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  3  0  0  0  0  0  0 |  u = MusicHall
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  6  0  0  0  0  0 |  v = Sleep
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0 |  w = blackengineering
  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 |  x = mogoliangrill
  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 12  0  0 |  y = Atanasoff
  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  2  0 |  z = LebaronHall
  0  0  0  0  0  0  0 11  0  1  0  0  0  0  0  0  2  0  0  0  0  0  0  0  0  0 10 | aa = WaitingBus

