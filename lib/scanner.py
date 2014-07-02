# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:10:36 2014

@author: josh
"""
import string
class TextScanner(object):
      wordsum = 0
      factorlist = {"one" : 1, "two" : 2, "three" : 3 , "four" : 4,
                "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9 , "ten" : 10 ,"eleven" : 11,
                "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16 ,
                "seventeen" : 17, "eighteen" : 18, "nineteen" : 19,"twenty" : 20 ,"thirty" : 30, "forty" : 40, "fifty" : 50 , "sixty" :60,
                "seventy" : 70, "eighty" : 80, "ninety" : 90}
                
      powers_of_ten = {"hundred" : 100 , "thousand" : 1000 , "million" : 1000000  , "billion" : 1000000000, 
      "trillion" : 1000000000000}
      def __init__(self, text):
          self.text = text
          file = open(text, 'r')
          lyrics = file.read().lower()
          file.close()
          self.text =  [word.strip(string.punctuation) for word in lyrics.split()]
    
      def wordsum(self):
          factor = 0
          sum = 0
          for word in self.text:
              if word in self.factorlist:
                 factor = self.factorlist[word]
                 
              if word in self.powers_of_ten :
                 sum = sum + factor * self.powers_of_ten[word] - factor 
                 
              else:
                  sum = sum + factor
                 
          self.wordsum = sum
          
      def displayresult(self):
          print "The sum of the number words in this song is " + str(self.wordsum)
          
     
          
      
                 
            
              
              
                  
       
         
         
    
