version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
if [[ -z "$version" ]]
then
    echo "Python is not installed"
    echo "Installing Python"
    bash host/linux/python.sh
else python3 -m vision
fi
