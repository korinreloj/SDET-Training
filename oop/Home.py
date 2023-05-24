#import Authentication as auth
import Authentication

username = "user"
password = "User123"

Authentication.valid_login()
#Authentication.valid_login(username, password)

username = "user"
password = "abc123"

Authentication.invalid_login()
#Authentication.invalid_login(username, password)

username = ""
password = "User123"
Authentication.blank_login()
#Authentication.blank_login(username, password)
