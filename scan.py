import base64
exec(base64.b64decode('aW1wb3J0IG9zDQppbXBvcnQgcmVxdWVzdHMNCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwIGFzIGJzDQpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0LCBGb3JlLCBTdHlsZQ0KZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvcg0KDQp0cnk6DQoJb3MubWtkaXIoJ0NoZWNrZXInKSAjb3V0cHV0cmVzdWx0DQpleGNlcHQ6DQogICAgcGFzcw0KDQpzID0gcmVxdWVzdHMuU2Vzc2lvbigpDQp1YWdlbnQgPSB7J1VzZXItQWdlbnQnOidNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFVidW50dSBDaHJvbWl1bS8zNy4wLjIwNjIuOTQgQ2hyb21lLzM3LjAuMjA2Mi45NCBTYWZhcmkvNTM3LjM2J30gI3VzZXJhZ2VudA0KDQpvcy5zeXN0ZW0oJ2NscycgaWYgb3MubmFtZSA9PSAnbnQnIGVsc2UgJ2NsZWFyJykgI2NsZWFydGVybWluYWwNCg0KaW5pdCgpDQptZXJhaCA9IEZvcmUuUkVEICNjb2xvcg0KaGlqYXUgPSBGb3JlLkdSRUVOICNjb2xvcg0KY3lhbiA9IEZvcmUuQ1lBTiAjY29sb3INCmt1bmluZyA9IEZvcmUuWUVMTE9XICNjb2xvcg0KcmVzZXQgPSBGb3JlLlJFU0VUICNjb2xvcg0KY2VyYWggPSBTdHlsZS5CUklHSFQgI2JyaWdodA0KDQpkZWYgc2hlbGwoZG9tYWluKToNCiAgICB0cnk6DQogICAgICAgIHNpdGUgPSBkb21haW4ucmVwbGFjZSgiaHR0cHM6Ly8iLCAiIikucmVwbGFjZSgiaHR0cDovLyIsIiIpLnJlcGxhY2UoIlxuIiwiIikNCiAgICBleGNlcHQ6DQogICAgICAgIHBhc3MNCiAgICByZXEgPSBzLmdldCgnaHR0cDovLycgKyBzaXRlLCBoZWFkZXJzPXVhZ2VudCwgdGltZW91dD0yMCkudGV4dA0KICAgIGlmICJPd25lci9Hcm91cCIgaW4gcmVxOg0KICAgICAgICBwcmludChmJ1t7Y2VyYWgraGlqYXV9I3tyZXNldH1dICcrc2l0ZStmJyB8IHtjZXJhaCtoaWphdX1BY3RpdmV7cmVzZXR9JykNCiAgICAgICAgd2l0aCBvcGVuKCdDaGVja2VyL3Jlc3VsdHMudHh0JywgJ2ErJykgYXMgZjoNCiAgICAgICAgICAgIGYud3JpdGUoJ2h0dHA6Ly8nICsgc2l0ZSArICJcbiIpDQogICAgZWxpZiAiUGVybWlzc2lvbiIgaW4gcmVxOg0KICAgICAgICBwcmludChmJ1t7Y2VyYWgraGlqYXV9I3tyZXNldH1dICcrc2l0ZStmJyB8IHtjZXJhaCtoaWphdX1BY3RpdmV7cmVzZXR9JykNCiAgICAgICAgd2l0aCBvcGVuKCdDaGVja2VyL3Jlc3VsdHMudHh0JywgJ2ErJykgYXMgZjoNCiAgICAgICAgICAgIGYud3JpdGUoJ2h0dHA6Ly8nICsgc2l0ZSArICJcbiIpDQogICAgZWxpZiAiJm5ic3A7VVBMT0FEIiBpbiByZXE6DQogICAgICAgIHByaW50KGYnW3tjZXJhaCtoaWphdX0je3Jlc2V0fV0gJytzaXRlK2YnIHwge2NlcmFoK2hpamF1fUFjdGl2ZXtyZXNldH0nKQ0KICAgICAgICB3aXRoIG9wZW4oJ0NoZWNrZXIvcmVzdWx0cy50eHQnLCAnYSsnKSBhcyBmOg0KICAgICAgICAgICAgZi53cml0ZSgnaHR0cDovLycgKyBzaXRlICsgIlxuIikNCiAgICBlbGlmICJTb2Z0d2FyZSIgaW4gcmVxOg0KICAgICAgICBwcmludChmJ1t7Y2VyYWgraGlqYXV9I3tyZXNldH1dICcrc2l0ZStmJyB8IHtjZXJhaCtoaWphdX1BY3RpdmV7cmVzZXR9JykNCiAgICAgICAgd2l0aCBvcGVuKCdDaGVja2VyL3Jlc3VsdHMudHh0JywgJ2ErJykgYXMgZjoNCiAgICAgICAgICAgIGYud3JpdGUoJ2h0dHA6Ly8nICsgc2l0ZSArICJcbiIpDQogICAgZWxpZiAiWyBTSVpFIF0iIGluIHJlcToNCiAgICAgICAgcHJpbnQoZidbe2NlcmFoK2hpamF1fSN7cmVzZXR9XSAnK3NpdGUrZicgfCB7Y2VyYWgraGlqYXV9QWN0aXZle3Jlc2V0fScpDQogICAgICAgIHdpdGggb3BlbignQ2hlY2tlci9yZXN1bHRzLnR4dCcsICdhKycpIGFzIGY6DQogICAgICAgICAgICBmLndyaXRlKCdodHRwOi8vJyArIHNpdGUgKyAiXG4iKQ0KICAgIGVsaWYgIlsgUEVSTSBdIiBpbiByZXE6DQogICAgICAgIHByaW50KGYnW3tjZXJhaCtoaWphdX0je3Jlc2V0fV0gJytzaXRlK2YnIHwge2NlcmFoK2hpamF1fUFjdGl2ZXtyZXNldH0nKQ0KICAgICAgICB3aXRoIG9wZW4oJ0NoZWNrZXIvcmVzdWx0cy50eHQnLCAnYSsnKSBhcyBmOg0KICAgICAgICAgICAgZi53cml0ZSgnaHR0cDovLycgKyBzaXRlICsgIlxuIikNCiAgICBlbHNlOg0KICAgICAgICBwcmludChmJ1t7Y2VyYWgraGlqYXV9I3tyZXNldH1dICcrc2l0ZStmJyB8IHttZXJhaH1FUlJPUntyZXNldH0nKQ0KDQpiYW5uZXIgPWYiIiINCntoaWphdX0gICAgX19fX18gX18gICAgICAgICBfX19fX19fX18gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCntoaWphdX0gICAvIF9fXy8vIC9fICBfX18gIC8gLyAvIF9fXy9fX19fX19fX18gX19fX18gIF9fX18gIF9fXyAgX19fX18gIHtyZXNldH0gQXV0aG9yICA6IEphdmFYcGxvaXRlcg0Ke2hpamF1fSAgIFxfXyBcLyBfXyBcLyBfIFwvIC8gL1xfXyBcLyBfX18vIF9fIGAvIF9fIFwvIF9fIFwvIF8gXC8gX19fLyAge3Jlc2V0fSBWZXJzaW9uIDogMS4zDQp7aGlqYXV9ICBfX18vIC8gLyAvIC8gIF9fLyAvIC9fX18vIC8gL19fLyAvXy8gLyAvIC8gLyAvIC8gLyAgX18vIC8gICAgICB7cmVzZXR9IFRlbGVnYW0gOiBASmF2YUREb1MNCntoaWphdX0gL19fX18vXy8gL18vXF9fXy9fL18vL19fX18vXF9fXy9cX18sXy9fLyAvXy9fLyAvXy9cX19fL18vICAgICAgIHtyZXNldH0gQ2hhbm5lbCA6IEBCZXJrYWhTaGVsbA0KIiIiDQppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOg0KICAgIHRyeToNCiAgICAgICAgcHJpbnQoYmFubmVyKQ0KICAgICAgICBzaXRlID0gaW5wdXQoJ1s/XSBFbnRlciBZb3VyIFNoZWxsIExpc3QgPj4gJykgI2RvbWFpbmxpc3QNCiAgICAgICAgcGVybGluZSA9IG9wZW4oc2l0ZSwncicpLnJlYWQoKS5zcGxpdGxpbmVzKCkNCiAgICAgICAgcHJpbnQoJycpDQogICAgICAgIHdpdGggVGhyZWFkUG9vbEV4ZWN1dG9yKG1heF93b3JrZXJzPWludCgxMCkpIGFzIGU6DQogICAgICAgICAgICBbZS5zdWJtaXQoc2hlbGwsIGkpIGZvciBpIGluIHBlcmxpbmVdDQogICAgZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0Og0KICAgICAgICBwcmludChmJ1xuXG57bWVyYWh9WyFdIHtyZXNldH1DVFJMICsgQyBERVRFQ1Qge21lcmFofVshXScpICNmb3JrZXlib2FyZGludGVycnVwdA0KICAgIGV4Y2VwdDoNCiAgICAgICAgcHJpbnQoZidcbnttZXJhaH1bIV0ge3Jlc2V0fUlOQ09SUkVDVCB7bWVyYWh9WyFdJykNCg=='))