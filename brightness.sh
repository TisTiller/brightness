maxb="$(sudo cat /sys/class/backlight/*/max_brightness)"
echo "Max Brightness: $maxb"
printf "Brightness: "

read brightness
if [ $brightness -gt $maxb ]
then
	echo "Too Big."
else
	echo $brightness | sudo tee -a /sys/class/backlight/intel_backlight/brightness > /dev/null
fi
