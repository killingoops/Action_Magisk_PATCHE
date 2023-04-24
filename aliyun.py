from aligo import Aligo
from aligo import Auth


Auth._EMAIL_HOST = 'smtp.qq.com'
Auth._EMAIL_PORT = '465'
Auth._EMAIL_USER = '3129118466@qq.com'
Auth._EMAIL_PASSWORD = 'heisjndpkbwxdcfe'
# 提供 email 参数即可
ali = Aligo(email=('jaxoncai3@gmail.com', 'asd'))

ali.upload_file('payload-dumper-go', parent_file_id='64460e3d011411c9632c46fdbba2e2651aab3cfa')   