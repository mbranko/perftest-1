#!/bin/bash
REQUESTS=${1:-10000}
echo "Ukupan broj zahteva: $REQUESTS"
echo "Broj istovremenih: 100 200 300 400 500 600 700 800 900 1000"
echo "Proveri da li server radi na portu 8000"
read -n 1 -s -r -p "Pritisni taster za pocetak..."
rm -f *.tsv
for i in {100..1000..100}
do
  COMMAND="ab -n $REQUESTS -c $i -g $i.tsv localhost/v2/api/testovi/1/"
  eval $COMMAND
  sleep 5
done
gnuplot timeline.p
gnuplot binned.p
