I've attached everything I could find.

1. All my implementations were greedy and slow. 
You'll either find the greedy pseudocode in Julia's survey on 
diverse sampling methods or papers cited within the survey. 
The basic idea of greedy is that we start from a random data point and 
keep picking next data points that maximize the diversity objective. 
In distance based diversity, my implementations need to be supplied with a NxN pairwise distance matrix, 
i.e., matrix[i][j] = distance between data point i and j. I had computed this matrix beforehand and saved it. 
This is the part that's super slow. (I did not implement faster approximations because it didn't 
matter much for a user-study, sorry!)

2. div_sampling.txt has maxmin, maxsum, set selection with coverage based diversity, DisC. 

3. I could not make fair-DPP work, so I've only worked with vanilla DPP. 

4. fair_maxsum_maxmin.txt is the fair version of maxmin and maxsum. 
Again, it's a greedy implementation. In my data, fairness was only gender based. 
The unfair greedy implementation picks the next data point to be whatever maximizes the objective. 
In this case, I first compute how many males/females should be in my sample 
(e.g., if equal representation is required in a sample size of 100, then I'm only allowed to pick 50 males at most). 
In the sampling method, I kept track of how many male/female I had already picked to be in the sample. 
If I have already picked the maximum amount of males I'm allowed and my best choice to maximize the objective 
is a male, then I skip until I find the next-best female. 

5. The dataset is filled with inactive users, i.e., people have no activity. So I filtered them out. 
You can choose however you want to filter. I just did what made sense to me. I also did some pre-processing because 
there were too many nationalities of people in the data and I needed to reduce them in order to make meaningful 
data analytic tasks. I included some example in the filter.txt.