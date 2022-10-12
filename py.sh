# run python scripts by detecting extensions!!

case ${1##*.} in
	"py")
		python3 $1
		;;

	*)
		echo "Please enter a .py file!!"
		;;

	esac
