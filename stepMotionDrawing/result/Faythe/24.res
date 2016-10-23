=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Faythe
Instances:    35
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
term2(4): class 
term3(4): class 
term4(4): class 
term5(4): class 
term6(5): class 
term7(5): class 
term8(5): class 
term9(5): class 
term10(5): class 
term11(5): class 
term12(6): class 
term13(1): class 
term14(3): class 
term15(5): class 
term16(4): class 
term17(1): class 
term18(6): class 
term19(1): class 
term20(4): class 
term21(6): class 
term22(1): class 
term23(3): class 
class(14): 
LogScore Bayes: -761.6786938060382
LogScore BDeu: -4384.195450480371
LogScore MDL: -3147.067508560533
LogScore ENTROPY: -1506.2743781831718
LogScore AIC: -2429.2743781831737


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          34               97.1429 %
Incorrectly Classified Instances         1                2.8571 %
Kappa statistic                          0.9677
Mean absolute error                      0.0071
Root mean squared error                  0.0632
Relative absolute error                  5.5399 %
Root relative squared error             25.0085 %
Total Number of Instances               35     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        Eating
                 1         0          1         1         1          1        Driving
                 1         0.036      0.875     1         0.933      0.995    vocabulary
                 1         0          1         1         1          1        Midnightsnack
                 1         0          1         1         1          1        study
                 1         0          1         1         1          1        fb
                 1         0          1         1         1          1        Chop
                 1         0          1         1         1          1        Dinner
                 1         0          1         1         1          1        walmart
                 1         0          1         1         1          1        Sleep
                 1         0          1         1         1          1        church
                 1         0          1         1         1          1        cook
                 1         0          1         1         1          1        LivingRoom
                 0         0          0         0         0          1        readysledding
Weighted Avg.    0.971     0.007      0.946     0.971     0.958      0.999

=== Confusion Matrix ===

 a b c d e f g h i j k l m n   <-- classified as
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 | a = Eating
 0 2 0 0 0 0 0 0 0 0 0 0 0 0 | b = Driving
 0 0 7 0 0 0 0 0 0 0 0 0 0 0 | c = vocabulary
 0 0 0 1 0 0 0 0 0 0 0 0 0 0 | d = Midnightsnack
 0 0 0 0 2 0 0 0 0 0 0 0 0 0 | e = study
 0 0 0 0 0 2 0 0 0 0 0 0 0 0 | f = fb
 0 0 0 0 0 0 1 0 0 0 0 0 0 0 | g = Chop
 0 0 0 0 0 0 0 2 0 0 0 0 0 0 | h = Dinner
 0 0 0 0 0 0 0 0 2 0 0 0 0 0 | i = walmart
 0 0 0 0 0 0 0 0 0 3 0 0 0 0 | j = Sleep
 0 0 0 0 0 0 0 0 0 0 6 0 0 0 | k = church
 0 0 0 0 0 0 0 0 0 0 0 1 0 0 | l = cook
 0 0 0 0 0 0 0 0 0 0 0 0 4 0 | m = LivingRoom
 0 0 1 0 0 0 0 0 0 0 0 0 0 0 | n = readysledding


 more wifi info, better performance.
 x n
>> for n, I am outside. And possibly not in Faythe's house.

What application did you use for the layout drawing?
>> RoomSketcher(http://planner.roomsketcher.com/)

