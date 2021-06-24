regex='<coverage.+line-rate="([0-9).[0-9]+)".+>'

line=$(grep -oP $regex coverage.xml)

[[ $line =~ $regex ]]

echo ${BASH_REMATCH[1]}