# Question
In Olympics, the countries are ranked by the total number of medals won. You are given six integers G1, S1, B1, and G2, S2, B2, the number of gold, silver and bronze medals won by two different counties respectively. Determine which country is ranked better on the leaderboard. It is guaranteed that there will not be a tie between the two countries.

Input Format<br>
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.<br>

The first and only line of each test case contains six space-separated integers G1, S1, B1, and G2, S2, B2.
<br>
Output Format<br>
For each test case, print "1" if the first country is ranked better or "2" otherwise. Output the answer without quotes.
<br>
Constraints<br>
1≤T≤1000<br>
0≤G1,S1,B1,G2,S2,B2≤30<br>
Subtasks<br>
Subtask #1 (100 points): Original constraints<br>

Sample Input 1 <br>
3<br>
10 20 30 0 29 30<br>
0 0 0 0 0 1<br>
1 1 1 0 0 0<br>
Sample Output 1<br> 
1<br>
2<br>
1<br>
Explanation<br>
Test case 1: Total medals for the first country are 10+20+30=60 and that for the second country are 0+29+30=59. So the first country is ranked better than the second country.
<br>
Test case 2: Total medals for the first country are 0+0+0=0 and that for the second country are 0+0+1=1. So the second country is ranked better than the first country.<br>