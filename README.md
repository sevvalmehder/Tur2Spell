# Tur2Spell

This project is a Turing Machine simulator for spelling Turkish words.The detailed information about spelling and turing machine is [here](presentation/Tur2Spell.pdf).

## Examples
According to 3 rules for spelling:  
1. If there is consonant between two vowels in word, this consonant has a syllable with the next vowel. 
![For example: ara –> a-ra  ](https://github.com/sevvalmehder/Tur2Spell/blob/master/presentation/ara.png)  
2. If there are two repeated consonant in word, the first one has a syllable with the previous vowel and the second one has a syllable with the next vowel.  
![For example: sevmek –> sev-mek  ](https://github.com/sevvalmehder/Tur2Spell/blob/master/presentation/sevmek.png)  
3. If there are three repeated consonant in word, the last one has a syllable with the next vowel.  
![For example: altlık -> alt-lık](https://github.com/sevvalmehder/Tur2Spell/blob/master/presentation/altl%C4%B1k.png)  

## Usage  
### Linux  
For run with GUI: python3 gui.py  
For run without GUI: python3 main.py  
### Windows  
You can run [Tur2Spell.exe](Tur2Spell.exe) directly.  

## Resources  
For spelling rules: [TDK](http://tdk.gov.tr/icerik/yazim-kurallari/hece-yapisi-ve-satir-sonunda-kelimelerin-bolunmesi/)  
For Turing Machine details: Introduction to the Theory of Computation by Michael Sipser
