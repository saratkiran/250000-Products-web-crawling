#!/usr/bin/env python
import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document
import cookielib
import urllib
import simplejson
import re
import time
import csv
import random
import os
import re
import shutil
if __name__ == "__main__":
    
    ### importing beautiful soup
    sys.path.append("./BeautifulSoup")
    from bs4 import BeautifulSoup
    currentdir = os.getcwd()
    count = 0
    prod_count = 0
    total_count = 0
    os.makedirs("temp_del")
    for each in [x[0] for x in os.walk("htmldata")]:
        print each
        count+=1
        prod_count =0
    ### reading the html txt files
        if count == 1:
            asdjlh = "asldjk"
        else:    
            
            os.chdir(currentdir)
            source = each
            os.chdir(source)
            for files in os.listdir("."):
                if files.endswith(".txt"):
                    txtfile = open(files, 'r')
                    soup = BeautifulSoup(txtfile)
                    filename = files[0:-16]
                    prod_count += 1
                    total_count +=1
                    print filename
                    print each
                    print "product count = "
                    print prod_count
                    print "total count = "
                    print total_count 
                    os.chdir(currentdir)
                    with open("temp_del/"+filename+ ".txt", "a") as text_file1:
                        opentag = "<html><body>"
                        closetag = "</body></html>"
                        text_file1.write("{}".format(opentag))
                        
                        about_product = soup.find('div', { "class" : "product_section" })
                        if about_product:
                            try:
                                product_tofile =  "<b>Name: </b>" + about_product.contents[1].text + "<br />" + "<b>Type: </b>" + about_product.contents[3].text + "<br />"+ about_product.contents[5].text + "<br />" 
                                text_file1.write("{}".format(product_tofile))
                            except (UnicodeEncodeError, UnicodeDecodeError):
                                pass
                            
                        
                        searchtext_nl = re.compile(r'NutritionFacts',re.IGNORECASE)
                        foundtext_nl = soup.find('a', attrs={'name':searchtext_nl})# Find the first <p> tag with the search text
                        if foundtext_nl:
                            about_nl = foundtext_nl.findNext('p') # Find the first <table> tag that follows it
                            #about_nl_text =  about_nl.text + '\n'
                            
                            text_file1.write("{}".format(about_nl))
                        alltables = soup.findAll("table")
                        if alltables:
                        #print alltables
                            stringtomilk = " "           
                            for table in alltables:
                                text_file1.write("{}".format(stringtomilk))
                                text_file1.write("{}".format(table))
                                stringtomilk = "With 0.5 Cup Skim Milk"
                                
                                
                        searchtext_is = re.compile(r'Ingredients',re.IGNORECASE)
                        foundtext_is = soup.find('a', attrs={'name':searchtext_is}) # Find the first <p> tag with the search text
                        if foundtext_is:
                            about_is = foundtext_is.findNext('p') # Find the first <table> tag that follows it
                            ing_tofile = "<br /><b>Ingredients: </b>"
                            text_file1.write("{}".format(ing_tofile))
                            text_file1.write("{}".format(about_is))
                            
                        searchtext_ws = re.compile(r'Warnings',re.IGNORECASE)
                        foundtext_ws = soup.find('a', attrs={'name':searchtext_ws}) # Find the first <p> tag with the search text
                        if foundtext_ws:
                            try: 
                                about_ws = foundtext_ws.findNext('p') # Find the first <table> tag that follows it
                                wr_tofile = "<br /><b>Warnigs:</b>"
                                text_file1.write("{}".format(wr_tofile))
                                text_file1.write("{}".format(about_ws))
                            except (UnicodeEncodeError, UnicodeDecodeError):
                                pass
                            
                            
                                
                        text_file1.write("{}".format(closetag))
                    os.chdir(source)
                            
            dic = {'Total Fat':'<a href="http://en.wikipedia.org/wiki/Total_fat">Total Fat</a>',
                   'Saturated Fat':'<a href="http://en.wikipedia.org/wiki/Saturated_fat">Saturated Fat</a>',
                   'Calories':'<a href="http://en.wikipedia.org/wiki/Calories">Calories</a>',
                   'Calories from Fat':'<a href="http://en.wikipedia.org/wiki/Calories">Calories from Fat</a>',
                   'Polyunsaturated Fat':'<a href="http://en.wikipedia.org/wiki/Polyunsaturated_fat">Polyunsaturated Fat</a>',
                   'Monounsaturated Fat':'<a href="http://en.wikipedia.org/wiki/Monounsaturated_fat">Monounsaturated Fat</a>',
                   'Potassium':'<a href="http://en.wikipedia.org/wiki/Potassium">Potassium</a>',
                   'Total Carbohydrate':'<a href="http://en.wikipedia.org/wiki/Carbohydrate">Total Carbohydrate</a>',
                   'Dietary Fiber':'<a href="http://en.wikipedia.org/wiki/Dietary_fiber">Dietary Fiber</a>',
                   'Sugars':'<a href="http://en.wikipedia.org/wiki/Sugar">Sugars</a>',
                   'Protein':'<a href="http://en.wikipedia.org/wiki/Protein">Protein</a>',
                   'Iron':'<a href="http://en.wikipedia.org/wiki/Iron">Iron</a>',
                   'Niacin':'<a href="http://en.wikipedia.org/wiki/Niacin">Niacin</a>',
                   'Thiamin':'<a href="http://en.wikipedia.org/wiki/Thiamin">Thiamin</a>',
                   'Sodium':'<a href="http://en.wikipedia.org/wiki/Sodium">Sodium</a>',
                   'Vitamin A':'<a href="http://en.wikipedia.org/wiki/Vitamin_A">Vitamin A</a>',
                   'Vitamin C':'<a href="http://en.wikipedia.org/wiki/Vitamin_C">Vitamin C</a>',
                   'Calcium':'<a href="http://en.wikipedia.org/wiki/Calcium">Calcium</a>',
                   'Riboflavin':'<a href="http://en.wikipedia.org/wiki/Riboflavin">Riboflavin</a>',
                   'Folic Acid':'<a href="http://en.wikipedia.org/wiki/Folic_acid">Folic Acid</a>',
                   'Soluble Fiber':'<a href="http://en.wikipedia.org/wiki/Soluble_Fiber">Soluble Fiber</a>',
                   'Magnesium':'<a href="http://en.wikipedia.org/wiki/Magnesium">Magnesium</a>',
                   'Phosphorus':'<a href="http://en.wikipedia.org/wiki/Phosphorus">Phosphorus</a>',
                   'Zinc':'<a href="http://en.wikipedia.org/wiki/Zinc">Zinc</a>',
                   'Other Carbohydrate':'<a href="http://en.wikipedia.org/wiki/Carbohydrate">Other Carbohydrate</a>',
                   'Copper':'<a href="http://en.wikipedia.org/wiki/Copper">Copper</a>',
                   'Insoluble Fiber':'<a href="http://en.wikipedia.org/wiki/Insoluble_fiber">Insoluble Fiber</a>',
                   'Vitamin B6':'<a href="http://en.wikipedia.org/wiki/Vitamin_B6">Vitamin B6</a>',
                   'Vitamin D':'<a href="http://en.wikipedia.org/wiki/Vitamin_D">Vitamin D</a>',
                   'Vitamin B12':'<a href="http://en.wikipedia.org/wiki/Vitamin_B12">Vitamin B12</a>',
                   'Trans Fat':'<a href="http://en.wikipedia.org/wiki/Trans_Fat">Trans Fat</a>',
                   'Cholesterol':'<a href="http://en.wikipedia.org/wiki/Cholesterol">Cholesterol</a>',
                   'Policosanol':'<a href="http://en.wikipedia.org/wiki/Policosanol">Policosanol</a>',
                   'CoQ10':'<a href="http://en.wikipedia.org/wiki/CoQ10">CoQ10</a>'}
            
            # define our method
            def replace_all(text, dic):
                for i, j in dic.iteritems():
                    text = text.replace(i, j)
                return text
            
            
            os.chdir(currentdir)
            doutput = "prod_links/" + each
            os.makedirs(doutput)
            os.chdir(currentdir)
            os.chdir("temp_del")
            for files in os.listdir("."):
                if files.endswith(".txt"):
                    txtfile = open(files, 'r')
                    os.chdir(currentdir)
                    
                    with open(doutput+"/"+files, "a") as text_file1:
                        for line in txtfile:
                            text_file1.write("{}".format(replace_all(line,dic)))
                        #print (replace_all(line,dic))
                    os.chdir("temp_del")
            os.chdir(currentdir)
            os.chdir("temp_del")
            
            filelist = [ f for f in os.listdir(".") if f.endswith(".txt") ]
            for f in filelist:
                os.remove(f)
            os.chdir(currentdir)
           
                
        
        
            
                    
                    
            
            #try:
            #    searchtext_is = re.compile(r'Ingredients',re.IGNORECASE)
            #    foundtext_is = soup.find('a', attrs={'name':searchtext_is}) # Find the first <p> tag with the search text
            #    if foundtext_is:
            #        about_is = foundtext_is.findNext('p') # Find the first <table> tag that follows it
            #        ing_tofile = "Ingredients " + '\n' + about_is.text + '\n'
            #        with open("output/"+filename+ ".txt", "a") as text_file:
            #                text_file.write("{}".format(ing_tofile))
            #except:
            #    with open("errors/"+filename +".txt", "a") as text_file:
            #        text_file.write("{}".format(prod_url))
            #    pass
            
            
        
    
    
