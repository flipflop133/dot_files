from i3pystatus import Status
from i3pystatus.updates import yay
from i3pystatus.weather import weathercom
status = Status()

# Notification-center
status.register("notification_center", format='', color="#000000")
# Open Rofi power menu
status.register("power_menu", color="#000000")

# Displays clock
status.register("clock", format=" %I:%M", color="#000000")

# Displays date
status.register("custom_calendar",
                format=" {date}",
                interval=600,
                color="#000000")

# Pacman updates
status.register("updates",format = " {count}", backends = [yay.Yay(False)], color="#000000")

# XRP
#status.register("xrp",
#                format="XRP {wallet}€ {price}€ {percent}",
#                color="#000000")

# Weather
# status.register("custom_weather", format="{weather}", color="#000000")

# Weather
status.register("weather_com", format="{icon}  {temp}°C", color="#000000")

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
# status.register("load")

# Shows avg cpu freq
status.register("cpufreq", format=" {freq}Ghz", color="#000000")

# Shows avg cpu usage
status.register("cpu_usage", format=" {usage}%", color="#000000")

# Shows avg cpu temp
status.register("cputemp", format=" {temp}°C", color="#000000")

# Shows avg gpu usage
# status.register("gpumem", format=" {gpu_mem}Mb")

# Shows mem usage
status.register("mem",
                format=" {used_mem}Gb",
                divisor=1 * (10**9),
                color="#000000")

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
# status.register(
#     "network",
#     interface="enp3s0",
#     format_up=" {v4cidr}",
# )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk", path="/", format=" {avail}G", color="#000000")

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
                color_unmuted="#000000",
                color_muted="#000000",
                format=" {volume}",
                format_muted=" {volume}",
                on_leftclick="switch_mute")

# Shows Spotify song
status.register("custom_spotify",
                format=" {song}{artist}",
                interval=3,
                color="#000000")

status.run()