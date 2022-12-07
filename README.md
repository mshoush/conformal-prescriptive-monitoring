# Intervening With Confidence: Conformal Prescriptive Monitoring of Business Processes

This project contains supplementary material for the article ["Intervening With Confidence: Conformal
Prescriptive Monitoring of Business Processes"](https://deepai.org/publication/when-to-intervene-prescriptive-process-monitoring-under-uncertainty-and-resource-constraints) by [Mahmoud Shoush](https://scholar.google.com/citations?user=Jw4rBlkAAAAJ&hl=en) and [Marlon Dumas](https://kodu.ut.ee/~dumas/). We propose a prescriptive process monitoring approach that relies on conformal prediction to learn when to intervene in order to maximize a gain function when resources are limited.


The proposed method consists of three main phases, training, calibration, and testing—In the training phase, we clean and enrich the event log and use it to train predictive and causal models. In the calibration phase, we use an Inductive Conformal Prediction (ICP) algorithm to produce predictions with a guaranteed level of confidence. While the testing phase show how to operationalize the proposed approach during runtime, and it includes filtering, ranking, and a resource allocator.




# Dataset: 
Datasets can be found in the following link.
* [BPIC2017 and BPIC2012, i.e., a loan application process.](https://owncloud.ut.ee/owncloud/s/XRFidFxpw58j4zY)



# Reproduce results:
To reproduce the results, please run the following:

* First, you need to install the environment using

                                     conda create -n <environment-name> --file requirements.txt

* Next, download the data from the abovementioned link

* Then run the following shell script to start experiments w.r.t the training, calibration phases.


                                     ./run_training_calibration.sh
                                     

* Collect results according to EQ1 by running the following script and replace dataname with "bpic2012" or "bpic2017". 

                                     python  plot_EQ1.py <dataname>
