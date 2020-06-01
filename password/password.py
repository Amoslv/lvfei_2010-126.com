password_length = input('请输入密码长度')
# 密码长度
password_length = int(password_length)

if password_length<8 or password_length > 20 :
    raise ValueError('密码长度不符合')

# 生成密码
password = generate_password(password_length)
print(password)

def generate_password(length):
    