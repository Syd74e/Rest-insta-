import requests
import uuid
import random
import string
print("""    
        ____            __     ____           __       
      / __ \___  _____/ /_   /  _/___  _____/ /_____ _
     / /_/ / _ \/ ___/ __/   / // __ \/ ___/ __/ __ `/
    / _, _/  __(__  ) /_   _/ // / / (__  ) /_/ /_/ / 
   /_/ |_|\___/____/\__/  /___/_/ /_/____/\__/\__,_/  
                                 /By:@d74.e                  """)
print("\n")
user = input('  [+] Enter Your Email: ')

# إعداد طلب HTTP لإعادة تعيين كلمة المرور
url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
data = {
    '_csrftoken': ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
    'username': user,
    'guid': str(uuid.uuid4()),
    'device_id': str(uuid.uuid4())
}
headers = {
    'user-agent': f'''Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}; en_GB;)'''
}

# إرسال الطلب
response = requests.post(url, headers=headers, data=data).text

# التحقق من نجاح العملية
if '"obfuscated_email"' in response:
    print(f'       [+] DONE RESET GMAIL ✓ : {user}')
else:
    print(f'      [-] ERROR RESET GMAIL X : {user}')