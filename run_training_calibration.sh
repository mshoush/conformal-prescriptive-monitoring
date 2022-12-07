!/bin/sh
echo "Prepare bpic2017..." ;
python  prepare_data_bpic2017.py &
echo "Prepare bpic2012..." ;
python  prepare_data_bpic2012.py ;

echo "Start prediction..." ;
python get_catboost_pred_uncer.py "bpic2017"  results_pred 50 &
python get_catboost_pred_uncer.py "bpic2012"  results_pred 50;


echo "Start ORF...";
python orf.py "bpic2012" results_orf &
python orf.py "bpic2017" results_orf ;

echo "Start Conformal...";
python conformal_prediction.py bpic2012 &
python conformal_prediction.py bpic2017 ;
