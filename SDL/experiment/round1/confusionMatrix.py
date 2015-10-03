# confusionMatrix.py
'''

0 . cookingDishes.mp3
1 . cooking.mp3
2 . cooking2.mp3
3 . cooking3.mp3
4 . cooking4.mp3

5 . washingDishes.mp3

6 . eating.mp3
7 . eatingSuck.mp3
8 . eatingDishes.mp3

9  . bathroomWashing.mp3
10 . bathroomWashing2.mp3
11 . bathroom.mp3
12 . bathroom1.mp3
13 . bathroom2.mp3
14 . bathroomPee.mp3
15 . bashroomTowel.mp3
16 . bathroomUtensil.mp3
17 . bathroomTankFueling.mp3

18 . washing.mp3
19 . washing1.mp3
'''
total_number = 414

#initialization
bathroom_list = [0]*20
breakfast_list = [0]*20
lunch_list = [0]*20
dinner_list = [0]*20
night_list = [0]*20
washDishes_list = [0]*20
washBathroom_list = [0]*20
#            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

bathroom_number = 33
bathroom_number = 33
bathroom_list[1 ]= 2
bathroom_list[2 ] = 1
bathroom_list[10] = 1
bathroom_list[11] = 4
bathroom_list[12 ] = 5
bathroom_list[13 ] = 5
bathroom_list[14 ] = 3
bathroom_list[17 ] = 5
bathroom_list[18 ] = 4
bathroom_list[19 ] = 1


breakfast_number = 10
lunch_number = 43
dinner_number = 46
night_number = 22

breakfast_list[1] = 2
breakfast_list[2] = 1
breakfast_list[6] = 1
breakfast_list[10] = 1
breakfast_list[11] = 1
breakfast_list[14] = 1
breakfast_list[19] = 2

lunch_list[1] = 4
lunch_list[2] = 6
lunch_list[3] = 1
lunch_list[5] = 5
lunch_list[6] = 4
lunch_list[10] = 2
lunch_list[11] = 1
lunch_list[12] = 1
lunch_list[13] = 2
lunch_list[14] = 4
lunch_list[15] = 1
lunch_list[17] = 5
lunch_list[19] = 7

dinner_list[1] = 5
dinner_list[2] = 4
dinner_list[3] = 3
dinner_list[5] = 6
dinner_list[6] = 2
dinner_list[9] = 3
dinner_list[10] = 2
dinner_list[11] = 1
dinner_list[12] = 1
dinner_list[13] = 11
dinner_list[14] = 3
dinner_list[17] = 2
dinner_list[18] = 1
dinner_list[19] = 2

night_list[1] = 1
night_list[2] = 3
night_list[3] = 1
night_list[5] = 1
night_list[6] = 1
night_list[9] = 1
night_list[10] = 4
night_list[11] = 1
night_list[12] = 1
night_list[13] = 2
night_list[14] = 2
night_list[15] = 1
night_list[17] = 1
night_list[19] = 2

washingDishes_number = 61
washBathroom_number = 57

washDishes_list[1] = 4
washDishes_list[2] = 6
washDishes_list[3] = 6
washDishes_list[5] = 5
washDishes_list[6] = 3
washDishes_list[9] = 9
washDishes_list[10] = 6
washDishes_list[11] = 1
washDishes_list[12] = 7
washDishes_list[13] = 8
washDishes_list[14] = 4
washDishes_list[16] = 1
washDishes_list[17] = 3
washDishes_list[18] = 1
washDishes_list[19] = 3

washBathroom_list[1] = 6
washBathroom_list[2] = 1
washBathroom_list[4] = 2
washBathroom_list[5] = 5
washBathroom_list[6] = 1
washBathroom_list[9] = 2
washBathroom_list[10] = 7
washBathroom_list[11] = 3
washBathroom_list[12] = 3
washBathroom_list[13] = 5
washBathroom_list[14] = 7
washBathroom_list[15] = 2
washBathroom_list[16] = 3
washBathroom_list[17] = 2
washBathroom_list[18] = 1
washBathroom_list[19] = 2

#print bathroom_list

all_list = [bathroom_list, breakfast_list, lunch_list, dinner_list, night_list, washDishes_list, washBathroom_list]
conf_arr = all_list
'''
conf_arr = [ [33 , 2  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 1  , 3]    ,
             [3  , 31 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]    ,
             [0  , 4  , 41 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 1]    ,
             [0  , 1  , 0  , 30 , 0  , 6  , 0  , 0  , 0  , 0  , 1]    ,
             [0  , 0  , 0  , 0  , 38 , 10 , 0  , 0  , 0  , 0  , 0]    ,
             [0  , 0  , 0  , 3  , 1  , 39 , 0  , 0  , 0  , 0  , 4]    ,
             [0  , 2  , 2  , 0  , 4  , 1  , 31 , 0  , 0  , 0  , 2]    ,
             [0  , 1  , 0  , 0  , 0  , 0  , 0  , 36 , 0  , 2  , 0]    ,
             [0  , 0  , 0  , 0  , 0  , 0  , 1  , 5  , 37 , 5  , 1]    ,
             [3  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 39 , 0]    ,
             [0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 38] ]
             '''

print conf_arr

