# the file is organized as:
# up1
# down1
# up2
# down2
# ...


file=$1
sed '/^$/d' $file > $file.clean
awk 'NR%2==1' $file.clean > $file.clean.up
awk 'NR%2==0' $file.clean > $file.clean.down
