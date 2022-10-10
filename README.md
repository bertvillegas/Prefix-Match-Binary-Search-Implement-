# Prefix-Match-Binary-Search-Implement-
Identifies words in a list with a similar prefix using a Binary Search method

Implement the method called prefix_match in main.py. This method takes a list of words in natural sorted order which we'll call the dicctionary and a query word.

prefix_match will locate the range of entries in dictionary which have a prefix equal to query. The result should be returned as a tuple of two integers describing the start (inclusive) and end (exclusive) of this range. Specifically, the first integer in the result should be the smallest index where a word prefix-matches query, and the second integer should be 1 + the largest index where a word prefix-matches query.

Assumptions
All entries in dictionary are lower case
The query word is lower case
A word has a prefix equal to query if it's first n letters exactly match query where n is len(query). For example, if query is "bes" then
'best' - is a prefix match because it's first 3 characters are "bes"
'bes' - is a prefix match because it exactly equals the query word
'better' - is not a prefix match because it's 3rd character doesn't match the query word
'be' - is not a prefix match because it is shorter than the query word
If no words match the given query then None should be returned
A prefix of the empty string, ie '', matches every word in the dictionary

Example

prefix_match(['alphabet', 'be', 'bes', 'best', 'bestiary', 'better'], 'bes')
should return

(2,5)
because the first word that has a prefix matching 'bes' is 'bes' which is at index 2. The final word with a prefix matching 'bes' is 'bestiary' which is located at index 4, and since we want an exclusive final bound, the result is 4+1 == 5.


