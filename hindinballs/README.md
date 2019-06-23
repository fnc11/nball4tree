# hindinballs
Data generation steps:
1. Please go through this [Informative Report](https://drive.google.com/file/d/1RaBVGAmJoC-dQThnSylH0rF7QxTdxW9h/view?usp=sharing) on how the Hindi Data is structured and how to process it to make it useful for this experiment.
2. First extract words from word2vector file, so that we can filter out the word from our database for which we don't have the vectors.
* use word_extraction.py file for that.
* since the size of w2v file is large(4 GB), it's already done here.

3. Download these three packages from the mentioned repository[https://bitbucket.org/sivareddyg/python-hindi-wordnet/src/master/], 
WordSynsetDict.pk, SynsetHypernym.pk, SynsetWords.pk(this can be skipped). These are also available in data folder.

4. Run the print_path.py file it will generate tree structure or paths from leaves to last parent.

5. Run the mk_tree.py file to generate the tree out of the paths and also generate the wordSenseChildren.txt and catCodes.txt file which we ultimately need.

6. some modification has to be done in both the files
* in wordSenseChildren.txt file change root to \*root\*
* in catCodes.txt also make root to \*root\* and the make the second 1 as 0 in it's code.

Now you are ready to use these files for experiments

Of-course these steps are all done here you can use the files directly, the above steps has to follow if you want to regenerate the whole data.