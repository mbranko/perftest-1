set terminal png size 1280,720
set output "binned.png"
set key left top
set title "uWSGI + Django + PosgreSQL"
set grid y
set ylabel "response time (ms)"
plot for [i=100:1000:100] ''.i.'.tsv' using 9 title "".i
