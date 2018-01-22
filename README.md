# Regression_Tree_H-T
Predict humidity and temperature in a room, using a regression tree trained taking as input daily forecast.
The project is divided in 4 indipendent folder:

 * Data_Scraper: scripts used to retrive information from forecast website and mydashboard where umidity
          and temperature of my room are stored.   
 * Regresion_1: script used to run the first experiment
   * input_train: data collected by the forecast scraper from Jan to Feb 2017
   * input_test:  data collecetd by the forecast scaper from Jan to Feb 2017
   * label_train: data collected by the dashboard scraper from Jan to Feb 2017 from sensor 1
   * label_test:  data collected by the dashboard scraper from Jan to Feb 2017 from sensor 2  
   
 * Regresion_2: script used to run the second experiment (same structure of the first, but with more records)
   * input_train: data collected by the forecast scraper from Jan to Feb 2017
   * input_test:  data collecetd by the forecast scaper from Jan to Feb 2017
   * label_train: data collected by the dashboard scraper from Jan to Feb 2017 from sensor 1
   * label_test:  data collected by the dashboard scraper from Jan to Feb 2017 from sensor 2     
   
 * Regresion_3: script used to run the third experiment,train the tree in 2016 and use to predict T and H in 2017
   * input_train: data collected by the forecast scraper from Jan to March 2016
   * input_test:  data collecetd by the forecast scaper from Jan to March 2017
   * label_train: data collected by the dashboard scraper from Jan to March 2016 from sensor 1
   * label_test:  data collected by the dashboard scraper from Jan to March 2017 from sensor 1
   
 * Regresion_tree_example: script used to run the tutorial script published by sci-kit leanr.
   *  [Decision Regression Tree](http://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)
 
   
   
 
