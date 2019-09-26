
g=$(( 1 + $RANDOM % 10))
for i in `seq 1 100`; do
    for j in `seq 1 $g`; do
        printf "$RANDOM "
    done
    printf "\n"
done
