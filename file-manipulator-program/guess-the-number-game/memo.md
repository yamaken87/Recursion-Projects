Guess the number game

- 課題：
ユーザーに2つの数字、最小数(n)と最大数(m)を入力してもらう
最小値が最大値以下であることを確認する

- 内容：
ユーザーは、この2つの数字を入力すると、プログラムがnからmの範囲内で乱数を生成する。
ユーザーは乱数を正しく推測するまで、ゲームループの中で繰り返し数字を入力することになる。
与えられた範囲内の乱数を生成するには、randomモジュールとrandint関数を使用する

難易度を上げるために、ユーザーが数字を推測するための試行回数を制限することができる、
for文で最大n回の試行を行うか、while文でユーザーが数字を正しく当てるまで繰り返し入力する必要がある。