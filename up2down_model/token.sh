#token input file by add space

file=$1

cat $file | sed 's/./& /g' > $file.tok
sed -i 's/ $//' $file.tok
