# run python scripts

if [ -e $1 ]
then
	if [ -f $1 ]
	then
		python3 $1

	else
		echo "$1 is not a file!!"
	fi

else
	echo "$1 doesnot exist!!"
fi
