maxb="$(sudo cat /sys/class/backlight/*/max_brightness)"
curb="$(sudo cat /sys/class/backlight/*/brightness)"

echo "Max Brightness: $maxb"
echo "Current Brightness: $curb"

printf "Brightness: "

read brightness
if [ $brightness -gt $maxb ]
then
	echo "Too Big."
else
	echo $brightness | sudo tee -a /sys/class/backlight/*/brightness > /dev/null
fi
