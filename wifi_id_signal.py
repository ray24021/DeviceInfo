# -*- coding:UTF-8 -*-
import NetworkManager
for dev in NetworkManager.NetworkManager.GetDevices():
    if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
        continue
    aps = [ap for ap in dev.SpecificDevice().GetAccessPoints()]
    for ap in sorted(aps, key=lambda ap: ap.Ssid):
        print(u"%s:: %s" % (ap.Ssid, ap.Strength.encode("unicode_escape")))