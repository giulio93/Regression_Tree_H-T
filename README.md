# Regression_Tree_H-T
Predict humidity and temperature in a room, using a regression tree trained taking as input daily forecast.<br />

The project is divided in 4 indipendent folder:

 * Data_Scraper: scripts used to retrive information from forecast website and mydashboard where humidity
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
   
Every folder is stand-alone, you have just to jump inside and run the script.<br />
The core part of the script is the initialization of the Decision Tree Regressor.<br/>
For example:<br/>
regr_1 = DecisionTreeRegressor(max_depth=2,criterion="mse",splitter="best",min_samples_leaf=0.20)<br/>

Try to play with this method in order to get different/better results, you can find a full explanationa about it in the link above. <br />

That's pretty everything you need to know in order to understand explore this project.
I will let here a complete run of the projects documented unfortunately only in Italian, but i think you can have a sigth if you have understood the structure of the project that i have explaine above.

[Italian Complete Run] (https://docs.google.com/document/d/1ukRpVLagxdrSSCTLWuBy2rVhjsfUj768p9I8OayYH0M/edit?usp=sharing)
   





