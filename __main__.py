import sys
import piano
token = sys.argv[0]
username = sys.argv[1]

piano.ember(token, username, days=365, save_path='1.png')