=== Run information ===

Scheme:weka.classifiers.bayes.BayesNet -D -Q weka.classifiers.bayes.net.search.local.K2 -- -P 1 -S BAYES -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 0.5
Relation:     Faythe
Instances:    66
Attributes:   21
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
              class
Test mode:evaluate on training data

=== Classifier model (full training set) ===

Bayes Network Classifier
not using ADTree
#attributes=21 #classindex=20
Network structure (nodes followed by parents)
term1(3): class 
term2(2): class 
term3(2): class 
term4(2): class 
term5(6): class 
term6(1): class 
term7(1): class 
term8(5): class 
term9(1): class 
term10(1): class 
term11(4): class 
term12(1): class 
term13(1): class 
term14(1): class 
term15(1): class 
term16(1): class 
term17(1): class 
term18(2): class 
term19(1): class 
term20(1): class 
class(17): 
LogScore Bayes: -575.6201124231745
LogScore BDeu: -1815.513031351127
LogScore MDL: -1450.3887720848797
LogScore ENTROPY: -775.8543586186252
LogScore AIC: -1097.854358618625


Time taken to build model: 0.01 seconds

=== Evaluation on training set ===
=== Summary ===

Correctly Classified Instances          42               63.6364 %
Incorrectly Classified Instances        24               36.3636 %
Kappa statistic                          0.5849
Mean absolute error                      0.0465
Root mean squared error                  0.1506
Relative absolute error                 43.5263 %
Root relative squared error             65.3903 %
Total Number of Instances               66     

=== Detailed Accuracy By Class ===

               TP Rate   FP Rate   Precision   Recall  F-Measure   ROC Area  Class
                 1         0          1         1         1          1        Bathroom
                 0         0          0         0         0          0.977    LivingRoom
                 0         0          0         0         0          0.992    Driving
                 0.833     0.033      0.714     0.833     0.769      0.996    Gettingup
                 0         0          0         0         0          1        Midnightsnack
                 0.818     0.255      0.391     0.818     0.529      0.916    study
                 1         0          1         1         1          1        Dinner
                 1         0          1         1         1          1        VisitFriend
                 0.5       0.017      0.75      0.5       0.6        0.978    fb
                 0         0          0         0         0          0.961    Nap
                 0         0          0         0         0          0.985    Music
                 1         0          1         1         1          1        chat
                 0.75      0.093      0.643     0.75      0.692      0.968    vocabulary
                 0.286     0          1         0.286     0.444      0.952    DiningRoom
                 1         0.016      0.75      1         0.857      0.992    WorkingonPCathome
                 0         0          0         0         0          0.992    Faythehouse
                 1         0.016      0.667     1         0.8        1        WorkingonPC
Weighted Avg.    0.636     0.065      0.612     0.636     0.585      0.97 

=== Confusion Matrix ===

 a b c d e f g h i j k l m n o p q   <-- classified as
 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | a = Bathroom
 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 | b = LivingRoom
 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 | c = Driving
 0 0 0 5 0 1 0 0 0 0 0 0 0 0 0 0 0 | d = Gettingup
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 | e = Midnightsnack
 0 0 0 1 0 9 0 0 0 0 0 0 0 0 0 0 1 | f = study
 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 | g = Dinner
 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 | h = VisitFriend
 0 0 0 0 0 2 0 0 3 0 0 0 1 0 0 0 0 | i = fb
 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 | j = Nap
 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 | k = Music
 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 | l = chat
 0 0 0 0 0 3 0 0 0 0 0 0 9 0 0 0 0 | m = vocabulary
 0 0 0 1 0 2 0 0 0 0 0 0 2 2 0 0 0 | n = DiningRoom
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 | o = WorkingonPCathome
 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 | p = Faythehouse
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 | q = WorkingonPC

ps: x means remove this type.
 b = f i
>> I sometimes study and use fb in the living room.
 x Driving -2 
>> c, f : maybe this is because I try to study in the car.
 d = f -1
>> this two action happens in the same room.
 e = m audio
>> might because I study and eat cookie at the same time.
 f = d  f = q
>> study and getting up are in the same room, so as working on PC
 i = f  i = m 
>> vocabulary and study are similar, and I might browse fb when rest.
 j = m  j = o
>> when working at PC and vocabulary happen in the bedroom, I might take a nap.
 k = f
>> Could be study while listening to music.
 m = f
>> They are actually pretty similar.
 n = d f m -2-3
>> f, m are pretty similar. And I sometimes study on the dining table. For getting up, might be because the dining area is near my bedroom.
 x p  -2

Q: Did d, f, n, m happen in the same room (area)?
>>In term of area, yes, they are like just a wall between. I don't know if this is the answer you want to ask?
>>Getting up definitely in the bedroom. Study and vocabulary can happen anywhere in her house. Mostly in bedroom though. 
I also studied at the table in the dining room.

>>d definitely in the bedroom. f and m can happen anywhere in her house. Mostly in bedroom though. 
I also studied at the table in the n.

Q: How did you usually browse facebook, by phone or pc? Where? 
>> it can also happen anywhere. I think mostly in bedroom or living room. I use both, and if it's pc it must be in bedroom.
>>Mostly by phone during winter break I think.
-3

correct rate  =  62/66 = 83.33%
in terms of area: 65/66 = 98.4%
