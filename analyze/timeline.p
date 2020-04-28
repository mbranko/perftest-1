set terminal png size 1280,720
set output "timeline.png"
set key left top
set title "uWSGI + Django + PostgreSQL"
set grid y
set xdata time
set timefmt "%s"
set format x "%S"
set xlabel "seconds"
set ylabel "response time (ms)"
set datafile separator '\t'
plot for [i=100:1000:100] ''.i.'.tsv' every ::2 using 2:5 title ''.i.' req/s' with points
