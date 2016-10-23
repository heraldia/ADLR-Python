'fb' is browsing Facebook.
'chat' is chatting with friends using online app or face to face.
'vocabulary' is memorizing vocabulary.

'class' should see the timing. Might be the 228 data structure class. If so it was in Carver Hall.

================ Sue and Faythe/ ======================{
*.res files are model of your ADL record. 
15.res: 100% correct, w/o audio
18.res: 100% correct, w/o audio
9.res: 100% correct, w/o audio


21.res{{{2
If the date is 12/22~1/10 then I was in Faythe's house in Wisconsin.
Correctly Classified Instances          42               63.6364 %
Incorrectly Classified Instances        24               36.3636 %

we consider:
    'Music' can be recognized by audio tech.
    'Faythehouse' can be recognized by GPS.

and leave out outdoor ADL:
Driving
Faythehouse

Task1: Sue needs elaborate according to Confusion Matrix in 21.res:
Did you have 'Midnightsnack' in the same room with 'vocabulary'?
I don't remember, probably. If it is not 12/22~1/10, then yes.
probably 
they are both in bedroom or dining room in Faythe's house.
-1

Did you 'study' in the same room with 'Gettingup' and 'WorkingonPC'?
yes >>Correct.
-2

Open 21.res and answer 
Did you 'fb'    in the same room with 'study' and 'vocabulary'?
Probably. I am not sure.
-3

i == f ? 
>>hmmm, no. But they can happen at the same place, using phone.
i == m ?  
>>No. It's like the previous question. In addition, vocabulary and study sometimes are quite the same.

please answer
j == m, o ?    -2
>>hmm, m,o are definitely NOT the same. I think this is because my PC location and me are pretty close. 
Oh when I was in the bedroom and use your app, I will put my phone on the same chair many times. Nap 
of course taken in the bedroom.
m == f? -3
>>yeah they are pretty much the same type.

24.res{{{2

we consider:
'WaitingBus' == 'Bus'

Task2:
Open '24matrix.csv' with any editor or Excel,
and provide details as Task1.

>>Bedroom bj, study bc,fb bd, MidnightSnack af,nap x i, and WorkingOnPC a are prettly likely happen in the bedroom.

}
========================= Sue =====non sense================={
9.res no sense, cuz no wifi info

1 a = WorkingonPC
2 b = Snack
3 c = Gilman
4 d = Bathroom
5 e = hyvee
6 f = VisitFriend
7 g = TJtea
8 h = Nap
9 i = durham
10 j = Music
11 k = dryclothes
12 l = ParksLibrary
13 m = Bar
14 n = Coover
15 o = bake
16 p = Eating
17 q = Driving
18 r = Gettingup
19 s = Boiling
20 t = thinking
21 u = Bus
22 v = Sweeney
23 w = Lunch
24 x = nap
25 y = music
26 z = WalkingAtHome
27 aa = dry
28 ab = Pearson
29 ac = laundry
30 ad = blackengineering
31 ae = Midnightsnack
32 af = Science
33 ag = mogoliangrill
34 ah = lib
35 ai = NewChina
36 aj = Dinner
37 ak = WorkingonPCatcoover
38 al = Howe
39 am = cook
40 an = WorkingonPCathome
41 ao = class
42 ap = Walkingoutside
43 aq = design
44 ar = pearson
45 as = Mackay
46 at = Hub
47 au = Lied
48 av = Bathroomflushing
49 aw = ScienceII
50 ax = study
51 ay = Newchina
52 az = mu
53 ba = MusicHall
54 bb = Sleep
55 bc = neighbor
56 bd = Bedroom
57 be = Speech
58 bf = Atanasoff
59 bg = LebaronHall
60 bh = WaitingBus
61 
}
============================ Faythe ======================{
I analyzed the data generated in Faythe's house, 'cau they are mostly indoor.

Question, see 21.res
 Did d, f, n, m happen in the same room (area)?
 How did you usually browse facebook, by phone or pc? Where? 

Please check all *.res, the ADL recognition performance is highly satisfactory. 

(7*1.0+12*1.0+7*1.0+34*1.0+65*0.984) / (7+12+7+34+65) = 99.17%

}
=====2016-02-04 20:25:55 SueIndoor ======= {
a == m 
-1
same room? d, f, m, o  
g b 
h = k -3

}
email{{{2{ 
2016-02-08 23:24:37 {
Please always be careful on what I am asking.
SueIndoor:
adl record in predictOutput24.arff
Answer misclassifications in 24errorMatrix.csv 
same room? d, f, m, o  
>> d, f, m correct. o will be on the hallway.
where do you usually do laundry?
same room? j = m ?
same room? l = m?

SueOutdoor:
see Confusion Matrix in 24.res
37-16

}
2016-02-14 20:07:04{
Dear Dr. Chang,

That is a good news from Dr. Su.
1. Dataset can be shared.
2. New processing algorithm is welcome.

In my opinion, the main task of this paper is only to show the novel idea of ADL data collection by phone and good performance of analysis, proving its feasibility.

If their team wants to join, I need to reveal some mechanism and meaning of data. I believe that their new algorithm can gain better performance with some effort. Actually I have already gained highly accurate result by Bayes Network, but I just marked J48 pruned tree algorithm in paper.

I think they can join and run for next paper, main aim of which is to apply new algorithm on the ADL data and do comparison. 

To sum up, this paper is to show the framework design, and next paper is to show the data analysis, because no extra pages for description of data analysis this time.
I can maintain this project and source code for new researchers.

What do you think?

Phil

Dear Dr. Su,

Thanks for your comment,
As for the manuscript, I have some comments on it (in red). 
1. It seems that there is no concrete performance reported for experiment part two and three.
We could post concrete performance in part 2 and 3, but not necessary.
Well, we have many new upcoming ADL recognition processes up to now.
a. The recognition could get results from part 1, 2, 3, then part 4 recognizes those results together to infer ADL.
b. ADL result could be directly derived from part 1, 2, and 3.
c. Some new algorithm is coming.

2. The confusion matrix in Experiment four looks strange.
The Docx version reformat the original image in PDF. Please refer to 2016-02-14_210215.png


}

1-(8+1+1+8+2+1+4+9+20+3+4+5+6+1+2)/980 = 92.34%

