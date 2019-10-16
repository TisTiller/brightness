location="/sys/class/power_supply/"
pslevel="$(sudo cat $location/BAT*/capacity)"
psstate="$(sudo cat $location/BAT*/status)"
echo $pslevel%: $psstate
