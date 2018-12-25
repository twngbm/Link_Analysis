# Link_Analysis
## 檔案介紹  
* 1_HITS_algo.py:HITS演算法實作程式  
* 2_Pagerank.py:Pagerank演算法實作程式  
* 3_Simrank.py:SimRank演算法實作程式  
* graph_1.txt\~graph_6.txt:示範之資料集  
* graph_1_c.txt\~graph_3_c.txt:更改後增進hub,authority和Pagerank之資料集  
## 實作  
HITS理論與實作參考  
1. 課堂講義  
2. [HITS algorithm](https://en.wikipedia.org/wiki/HITS_algorithm)  
3. [GITHUB](https://github.com/DevSinghSachan/HITS-Hyperlink-Induced-Topic-Search/blob/master/hits.py)    
Pagerank理論與實作參考  
1. 課堂講義  
2. [PageRank](https://zh.wikipedia.org/wiki/PageRank)  
3. [Github](https://gist.github.com/diogojc/1338222)  
4. [Blog](https://www.cnblogs.com/flippedkiki/p/6557114.html)  
Simrank理論與實作參考  
1. 課堂講義  
2. [SimRank](https://zh.wikipedia.org/wiki/SimRank)  
3. [StackOverflow](https://stackoverflow.com/questions/9767773/calculating-simrank-using-networkx)
## 結果分析  
### HITS_alog   
1. 在graph_1.txt中，因為是單向圖，所以我們可以看到node1的authority值為0，因為其未參考任何節點，同理，node6未被任何節點參考，所以其hub為0  
2. 在graph_2.txt中，因為所有節點均只有一個參考與一個被參考，且為循環圖，故其值皆相同  
3. 在graph_3.txt中，四個節點互相跟鄰近的節點參考，故在邊緣的節點，其authority值相同，hub值也相同，在中間的的兩個節點，因為被左右節點參考與被參考，故其authority值與hub值皆較高。  
### Pagerank  
1. 在graph_1.txt中，因為是單向圖，在數據結果中可以看到權重的累積，因此最後一個node的pagerank會最高  
2. 在graph_2.txt中，因為是循環圖，所以權重不會偏重於某一特定節點，而是在疊帶數次後趨近於穩定，最後所有節點會是相同的pagerank  
3. 在graph_3.txt中，原理同graph_2.txt，權重會循環的在所有節點中運算，最後使每個節點的pagerank相同  
### SimRank
1. 在graph_1.txt中，由於沒有任兩個不相同的節點，參考到同一節點，因此結果是6\*6的單位矩陣  
2. 在graph_2.txt中，由於沒有任兩個不相同的節點，參考到同一節點，因此結果是5\*5的單位矩陣  
3. 在graph_3.txt中，由於任兩個不相鄰的節點，會參考到彼此相夾的一個節點，因此結果在對角線與S(1,3)和S(2,4)處會出現SimRank，其餘為零。  

## 效能分析  
在執行效能上，明顯出現延遲的是計算大數據時的Simrank演算法，原因在於，前兩個演算法，是針對樹的節點做遍歷與，計算節點的值與收斂條件後，不符合則再進行一次遍歷，而SimRank演算法則是將樹的節點與所有其他剩餘節點做遍歷，再遞迴計算彼此的相依節點數目，因此在計算上會須要非常龐大的計算量。
## 討論  
本次作業讓我學習到，再做關聯性分析的時候，有許多不同種的方法可以實作，並且必須考慮演算法的時間複雜度與資料的數量，並透過助教提供的數據，讓我學習到再什麼樣的特定情況下會出現特定的數字(結果分析)。  

## Q1.Find a way (e.g., add/delete some links) to increase hub, authority,and PageRank of Node 1 in first 3 graphs respectively.  
Graph 1:  
1,2  
2,3  
3,4  
4,5  
5,6  
2,1  
3,1  
4,1  
5,1  
1,3  
1,4  
1,5  
1,6  
Hub increase from 0.4472136 to 0.70705751  
Auth increase from 0 to 0.53460939  
Pagerank increase from 0.02773825 to 0.3585528  

Graph 2:  
1,2  
2,3  
3,4  
4,5  
5,1  
2,4  
2,5  
3,5  
1,3  
1,4  
1,5  
2,1  
3,1  
4,1  
Hub increase from 0.4472136 to 0.49711279  
Auth increase from 0.4472136 to 0.49717426  
Pagerank increase from 0.4472136 to 0.46201128  

Graph 3:  
1,2  
2,1  
~~2,3~~  
~~3,2~~  
3,4  
~~4,3~~  
3,1  
4,1  
1,3  
1,4  
Hub increase from 0.37175742 to 0.63232892  
Auth increase from 0.37172346 to 0.632612  
Pagerank increase from 0.5 to 0.5150252  

## Q2.More limitations about link analysis algorithms  
在HITS中進行的運算是透過矩陣與反矩陣的乘法運算，來計算出H和A值，矩陣的乘法運算相對消耗電腦運算量。
在SimRank中必須進行大量的矩陣遍歷，在我實作的演算法中，時間複雜度為N^2\*log(n)，相當耗時。
## Q3.Can link analysis algorithms really find the “important” pages from Web?  
在PageRank演算法的情況下，新的頁面排名通常會比舊的頁面來的低，原因在於新的頁面往往外連數會比舊的頁面少，即使是新的高品質頁面，因此在PageRank的情況下，仍要考慮其他演算法配合，才能真正找到重要的網站。
## Q4.What are practical issues when implement these algorithms in a real Web?  
在使用SimRank時，即使只是400多個Link，計算上仍需花費將近一分鐘，因此考慮實際情況時，可能運算時間會大幅增加至難以接受的程度
## Q5.What do the result say for your actor/movie graph?  

## Q6.Any new idea about the link analysis algorithm?  

## Q7.What is the effect of “C” parameter in SimRank?  
C代表的阻尼係數，當C介於0和1之間時，可以保證所有計算出的SimRank分布於0與1之間，方便做數值的一般化，如果C>1，則權重會成指數成長，可以凸顯數值分布的差異性。
## Q8.Design a new link-based similarity measurement

