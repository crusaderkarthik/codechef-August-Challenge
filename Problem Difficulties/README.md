# Question
You have prepared four problems. The difficulty levels of the problems are A1,A2,A3,A4 respectively. A problem set comprises at least two problems and no two problems in a problem set should have the same difficulty level. A problem can belong to at most one problem set. Output the maximum number of problem sets you can create using the four problems.
<br/><br/>
<b>Input Format</b>
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.<br/>
The first and only line of each test case contains four space-separated integers A1, A2, A3, A4, difficulty levels of the four problems.
<br/><br/>
<b>Output Format</b><br>
For each test case, print a single line containing one integer - the maximum number of problem sets you can create using the four problems.
<br>
<b>Constraints</b>
1≤T≤1000
1≤A1,A2,A3,A4≤10 <br><br>
<b>Subtasks</b><br>
<b>Subtask #1</b> (100 points): Original constraints

<b>Sample Input 1 </b><br>
3<br>
1 4 3 2<br>
4 5 5 5<br>
2 2 2 2<br>
<br><br>
<b>Sample Output 1 </b><br>
2<br>
1<br>
0<br>
<br><br>
<b>Explanation</b><br>
<b>Test case 1:</b> You can prepare the first problem set using the first two problems and the second problem set using the next two problems. So the problem sets will be [1,4] and [3,2].
<br>
<b>Test case 2:</b> You can prepare one problem set using one problem having a difficulty level of 4 and the other having a difficulty level of 5. There is no way to prepare more than one problem set.
<br>
<b>Test case 3:</b> There is no way to prepare a problem set.