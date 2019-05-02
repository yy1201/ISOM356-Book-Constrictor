**Github--
Final Project--
Introduction and Data Analysis
--Derick Yang**
=====

For this project, we used Python to parse through the classic novels listed on 
gutenberg.org and broke down the novels into words and sentences. By using data table, 
graph and frequency counting, we aim to visualize the character, emotion, tone, theme 
and plot of the novels through different Python packages. Two novels we picked were 
the Adventures of Tom Sawyer and the Adventures of Huckleberry Finn by Mark Twain. 
These two books are something that we have some familiarity with and also because 
many American students probably had it as assigned reading in high school. 
The Python packages we used for this project were listed below:

-Urllib.request
-Numpy
-Pandas
-Tokenizer 

First we used urllib.request to call the html website page where the digital novels locate
 and stored them into a variable. After we got the whole content of the novels, we split 
 the novels into chapters and built them into a dataframe. The tables above give us the 
 list of chapters in both Tom Sawyer and Huckleberry Finn. In each column, we have the 
 chapter number and the first sentence of each chapter. The Adventures of Tom Sawyer has 
 35 chapters and the Adventures of Huckleberry Finn has 43 chapters.

We further broke down each chapter into sentences. First, we counted the number of space 
in each chapter to obtain the approximate number of words. The initial codes we used 
before the presentation to count the number of words is [len(s) for s in huck_finn_
chapters], which actually gave us the number of characters in each chapter and gave us much larger 
average sentence length than it should be. After we realized the number was so off, 
we made some changes on our original codes and used count() function to count the number 
of “ ” (empty space) in each chapter. Then, we counted the number of sentences by 
counting the number of appearance of comma, period and exclamation marks and added them 
together to obtain the total number of sentences in each chapter. Later, we used 
the number of words divided by the total number of sentences to obtain the average 
sentence length in each chapter. 

The table above summarizes the general information of the average sentence length in 
both works. As we can see the average sentence length in Huckleberry Finn is longer 
than that in Tom Sawyer. Meanwhile, the standard deviation of the sentence length 
decreased a lot from Tom Sawyer to Huckleberry Finn, which somehow signified major change
of writing style for Mark Twain in these nine years. The author switched from shorter 
sentence to longer sentence with more consistent writing style. 

After we plotted the sentence length frequency chart based on chapters, 
we can see that the majority sentence length of Tom Sawyer clustered around 15 words 
and the distribution skewed to the left side. While, the sentence length of 
Huckleberry Finn follows a more normal distribution and most chapters have average 
sentence length around 18 to 20 words. 





