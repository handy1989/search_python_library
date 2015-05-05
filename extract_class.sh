ls ./library | while read file
do
    class_name=${file%.html}
    grep -Eo "id=\"[^\"]*\"" ./library/$file | awk -v class=$class_name -F'"' '{print class"\t"$2}'
done > ./class_and_functions.txt
