# CS_pickem_simulator

In the game Counter Strike, there is a fantasy betting called pick-em on major tournaments. The tournament is a swiss tournament in the group stage, where 16 teams face off against each other. Teams with the same score (wins-losses) are paired against each other in rounds. Three wins gets you through to the next stage, and three losses leads you out of the tournament. In pickems you are to choose the two teams to go 3-0, and the other 6 teams to go through to the next stage*. You also choose the two teams that go 0-3, but this is not interesting. Each correct pick yields 1 point. Question if, what is the best strategy?
(* This is old pickem. Currently picks to go through do not yield a point if the team goes 3-0, therefore the best strategy is to pick the two best teams to go 3-0)

The naive approach would be to pick 1st and 2nd best teams to go 3-0. It is fairly likely that one of them will lose at least one game denying you a point, whereas picking them to go through would have been practically a guaranteed point.

With this simulator I have simulated the swiss tournament format using ELO ranking for the teams, which determines the probability that team A wins over team B. I have simulated the tournament 1000 times for each pick, to see the average score.

For the first table we have consecutive teams separated by 10 elo points. This corresponds to the first team beating the last in a bo1 with a probability 70%. The table we get is :

Picks | #1 | #2 | #3 | #4 | #5 | #6 | #7
--- | --- | --- | --- |--- |--- |--- |---
#2 | 5,0772 |  |  |  |  |  | 
#3 | 5,0518 |	5,0987 | | | | |
#4 | 5,1039 |	5,0982 |	5,1017 | | | |
#5 | 5,1174 |	5,1298 |	5,1373 |	5,1465 | | |
#6 | 5,1652 |	5,1229 |	5,1428 |	5,1498 |	5,1801 | |
#7 | 5,2114 |	5,1855 |	5,1868 |	5,1826 |	5,2111 |	5,2434 |	
#8 | 5,2177 |	5,2344 |	5,243 |	5,2442 |	5,2266 |	5,2856 |	5,334

Then we have table with elo difference 15, and 1st team beats last with probability 79%:
 
Picks|1|2|3|4|5|6|7
:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:
2|5,788||||||
3|5,778|5,7377|||||
4|5,768|5,7532|5,7054||||
5|5,8041|5,7319|5,7267|5,7139|||
6|5,8229|5,7549|5,7607|5,7583|5,7789||
7|5,8648|5,8447|5,7871|5,8166|5,8071|5,8534|
8|5,9304|5,8906|5,8475|5,86|5,8662|5,9068|5,9512

Then the table with elo difference 20, and 1st team beats last in bo1 with probability 85%:

Picks|1|2|3|4|5|6|7
:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:
2|6,4009||||||
3|6,3168|6,2344|||||
4|6,318|6,2265|6,1395||||
5|6,2938|6,2291|6,159|6,1156|||
6|6,352|6,2492|6,1742|6,1498|6,1587||
7|6,4086|6,2907|6,23|6,2171|6,2241|6,2673|
8|6,475|6,3753|6,3266|6,2641|6,2762|6,3173|6,3961

Then the table with elo difference 25, and 1st team beats last in bo1 with probability 90%:

Picks|1|2|3|4|5|6|7
:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:
2|6,8555||||||
3|6,7547|6,6483|||||
4|6,7003|6,5601|6,475||||
5|6,6721|6,5529|6,4388|6,3923|||
6|6,6917|6,5789|6,4897|6,4113|6,412||
7|6,7915|6,6633|6,5452|6,489|6,4894|6,5096|
8|6,8951|6,755|6,6558|6,5954|6,5904|6,618|6,6798

Then finally the table with elo difference 30, and 1st team beats last in bo1 with probability 93%:

Picks|1|2|3|4|5|6|7
:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:
2|7,2134||||||
3|7,0974|6,9111|||||
4|7,0115|6,8434|6,694||||
5|6,9547|6,8045|6,6704|6,5817|||
6|6,9949|6,8103|6,7088|6,5665|6,583||
7|7,0547|6,8867|6,7456|6,6796|6,6457|6,6851|
8|7,1945|7,0401|6,903|6,8127|6,7753|6,7962|6,8859

Conclusion:
It seems that whenever the skill distribution is really narrow, and there is uncertainty, it is the best to pick the 7th and 8th best teams as 3-0. And conversely when the skill distribution is really wide, it is best to pick 1st and 2nd best teams as 3-0 picks. However there is a wide middle ground where picking 1st and 8th best teams is clearly best. This middle ground is also in a realistic area of skill distributions, and even with the other skill distributions picking 1st and 8th is a good result, if not the best. Given that there is quite a bit uncertainty in deciding the skill discrepancies of the teams and their rankings, it seems that the best pick is picking 1st and 8th best teams as 3-0.

Take these results with a grain of salt, because analyzing the expected values with singular skill distributions can be misleading, since the skill distribution is in itself an unknown. Also the distribution used is even, but maybe there is a more realistic distribution that I could've used. Further this yields the best EV for the score, but probably more desirable would be picks with the highest probability such that the score is at least 6 (as that is the passing score), but I am assuming that such a pick is likely to correspond with the one with highest EV.
