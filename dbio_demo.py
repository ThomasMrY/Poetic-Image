# coding=utf-8
from dbio import DBIO

io = DBIO(username='adminstor', password=None)
io.submit(10, u'床前明月光， 疑是地上霜', 0.5, ['moon', 'bed'], [u'非常牛逼', u'李白'])