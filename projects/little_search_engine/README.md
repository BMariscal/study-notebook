
Enron Email search:

The legal team suing Enron needs your help. They need to search through the email corpus from their mobile phone to reference material. A few interesting restrictions:

- This will be running in a mobile environment, so we don't have a lot of memory. You can't just load everything into RAM. You need to be as efficient as possible about organizing the data on disk, keeping as little data as possible in memory.
- We don't have access to the Internet. The entire corpus will live on the device.
- You _do_ have access to a server if you want to pre-process the data somehow before placing on the device. But once it's on their phone, it's there forever.
- Because typing on a phone is annoying, we want results to appear as you type. For example, if I type "app", I'd see emails matching on "app", "apple" and "application".
- Please implement a solution yourself. Don't use a library (e.g. install Lucene).
- You don't have to build an iOS app. We're just looking for a method that we can call — e.g. search(term) — that can return results. You can use Python, Ruby, Go or just Jeff Dean it and write binary in a text editor. (Kidding -- please don't do that last one).

The dataset is [here](https://www.cs.cmu.edu/~enron/enron_mail_20150507.tar.gz). 

---

My Approach:

1. Create *B-Tree* structure with file paths and documents from data file.

2. Create *inverted index* [the list of words, and the documents in which they appear] mapping each email address found in the files to the email file paths where each email is found and the index where the email address is found in that document.

3. Create *Trie for autocomplete* [research Bloom Filter for possible alternative (faster?)] for the *inverted index* indexes.  [Relevant mini-project](https://docs.google.com/document/d/1yDk36HGJlvxbAP3xxe1g5es7MVtAmJGsUvITISQ_9pg/edit#heading=h.y41ubj2hqa5m)


----
Notes:

* What's the difference between an inverted index and a plain old index? [Answer](https://stackoverflow.com/questions/7727686/whats-the-difference-between-an-inverted-index-and-a-plain-old-index)


![inverted index](https://i.imgur.com/yDLdxbU.jpg)

[paper 1](https://www.academia.edu/10327128/Reduction_in_Searching_Time_of_Inverted_Index_Using_Bloom_Filter),
[paper 2](http://pages.cs.wisc.edu/~jignesh/publ/sigmatch.pdf)