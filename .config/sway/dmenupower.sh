#!/bin/sh

icon_path="/usr/share/icons/Papirus/48x48/apps/"
shutdown="system-shutdown.svg"
reboot="system-reboot.svg"
log_out="system-log-out.svg"
suspend="system-suspend.svg"
suspend_hibernate="system-suspend-hibernate.svg"

LOGOFF_CMD="sway exit"


SELECT=$(printf " Poweroff\nﰇ Reboot\n﫼 Logout\n鈴 Suspend\n Hibernate" |dmenu -i -l 10)

case $SELECT in
        " Poweroff")
                notify-send -i $icon_path$shutdown "Shutting down..."
                sleep 1
                poweroff
                ;;
        "ﰇ Reboot")
                notify-send -i $icon_path$reboot "Rebooting..."
                sleep 1
                reboot
                ;;
        "﫼 Logout")
                notify-send -i $icon_path$log_out "Logging off..."
                sleep 1
                $LOGOFF_CMD
                ;;
        "鈴 Suspend")
                notify-send -i $icon_path$suspend "Suspending..."
                sleep 1
               	systemctl suspend
                ;;
	" Hibernate")
                notify-send -i $icon_path$suspend_hibernate "Hibernating..."
                sleep 1
               	systemctl hibernate
                ;;
esac
