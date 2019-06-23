# Install the package

* for Ubuntu platform please first install python3-tk
```
sudo apt-get install python3-tk
```

* for Ubuntu or Mac platform type:

```
$ git clone https://github.com/gnodisnait/nball4tree.git
$ cd nball4tree
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```

# Experiment 1:  Training and evaluating nball embeddings
## Experiment 1.1: Training nball embeddings
* For Hindi data generation follow instructions in the hindinballs directory.
* Files used for Hindi data generation are taken from this github repo[https://bitbucket.org/sivareddyg/python-hindi-wordnet/src/master/] which mainly took data from IIT Bombay University[http://www.cfilt.iitb.ac.in/]. 
* You need to download w2v from this website[https://fasttext.cc/docs/en/crawl-vectors.html] and make sure you remove first line of this file as it contains information about number of words and dimensions.
```
% you need to create an empty file nball.txt for output

$ python nball.py --train_nball /Users/<user-name>/data/nball.txt --w2v /Users/<user-name>/data/cc.hi.300.vec  --ws_child /Users/<user-name>/data/wordSenseChildren.txt  --ws_catcode /Users/<user-name>/data/glove/catCodes.txt  --log log.txt
% --train_nball: output file of nball embeddings
% --w2v: file of pre-trained word embeddings
% --ws_child: file of parent-children relations among word-senses
% --ws_catcode: file of the parent location code of a word-sense in the tree structure
% --log: log file, shall be located in the same directory as the file of nball embeddings
```
The training process can take around 3 days. 


## Experiment 1.2: Checking whether tree structures are perfectly embedded into word-embeddings
* main input is the output directory of nballs created in Experiment 1.1
* shell command for running the nball construction and training process
```
$ python nball.py --zero_energy <output-path> --ball <output-file> --ws_child /Users/<user-name>/data/wordSenseChildren.txt
% --zero_energy <output-path> : output path of the nballs of Experiment 1.1, e.g. ```/Users/<user-name>/data/data_out```
% --ball <output-file> : the name of the output nball-embedding file
% --ws_child /Users/<user-name>/data/wordSenseChildren.txt: file of parent-children relations among word-senses
```
The checking process can take a very long time around 3-4 hours.
* result

If zero-energy is achieved, a big nball-embedding file will be created ```<output-path>/<output-file>```
otherwise, failed relations and word-senses will be printed.

** Test result at Ubuntu platform:
![](https://github.com/fnc11/nball4tree/blob/master/pic/ubuntu_result.jpeg)
 
- [nball embeddings with 67152 balls](https://drive.google.com/open?id=1d-D7AF9rl2g_QFAGLD-m3N0DT_5-uZLS)
- [nball.txt file](https://drive.google.com/open?id=1JWNuc2eBTWDrbG1MCdHlWtxenGVKX8to) 

# Experiment 2: Observe neighbors of word-sense using nball embeddings
* [pre-trained nball embeddings](https://drive.google.com/open?id=1d-D7AF9rl2g_QFAGLD-m3N0DT_5-uZLS)
```
$ python nball.py --neighbors दिल्ली.n.01 फिलीपीन्स.n.01 मंगलवार.n.01 --ball /Users/<user-name>/data/data_out/  --num 6
% --neighbors: list of word-senses
% --ball: file location of the nball embeddings
% --num: number of neighbors
```

* Results of nearest neighbors look like below:

{   'दिल्ली.n.01':
 [   'पटना.n.01',  
        'देहली.n.01',  
        'कोलकाता.n.01',  
        'बंगलूर.n.01',  
        'त्रिवेंद्रम.n.01',  
        'बंगलुरु.n.01'],  
    'फिलीपीन्स.n.01': 
 [   'फिलीपींस.n.01',  
                          'फिलिपीन्स.n.01',  
                          'फिलिपींस.n.01',  
                          'बोसनिया.n.01',  
                          'बोट्सवाना.n.01',  
                          'मलयेशिया.n.01'],  
    'मंगलवार.n.01': 
 [   'बुधवार.n.01',  
                        'सोमवार.n.01',  
                        'शुक्रवार.n.01',  
                        'शनिवार.n.01',  
                        'गुरुवार.n.01',  
                        'रविवार.n.01']}  

English Translation:
{ ‘Delhi.n.01’: 
 [   ‘Patna.n.01’,  
		‘Delhi.n.01’,  <----- Different written form of Delhi in Hindi  
		‘Kolkata.n.01’  
		‘Bangalur.n.01’,  
		‘Trivandrum.n.01’,  
		‘Bangaluru.n.01’],  
‘Philippines.n.01’: 
 [   ‘Philippines.n.01’,  <----- Different written form of Philippines in Hindi  
		      ‘Philippines.n.01’,  <----- Different written form of Philippines in Hindi  
		      ‘Philippines.n.01’,  <----- Different written form of Philippines in Hindi  
		      ‘Bosnia.n.01’,  
		      ‘Botswana.n.01’,  
		      ‘Malaysia.n.01’],  
‘Tuesday.n.01’: 
 [   ‘Wednesday.n.01’,  
		      ‘Monday.n.01’,  
		      ‘Friday.n.01’,  
		      ‘Saturday.n.01’,  
		      ‘Thrusday.n.01’,  
		      ‘Sunday.n.01’]}  


# Cite

If you use the code, please cite the following paper:

Tiansi Dong, Chrisitan Bauckhage, Hailong Jin, Juanzi Li, Olaf Cremers, Daniel Speicher, Armin B. Cremers, Joerg Zimmermann (2019). *Imposing Category Trees Onto Word-Embeddings Using A Geometric Construction*. **ICLR-19** The Seventh International Conference on Learning Representations, May 6 – 9, New Orleans, Louisiana, USA.

