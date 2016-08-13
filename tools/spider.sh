#/bin/bash
cd /www/Recoder/tools
/usr/bin/python2.7 getmain.py
sleep 10s
/usr/bin/mysql -h 63.221.138.138 -urecoder -pkYKQBGfsJMVy00y6PDl0 -e "delete from recoder.spider_taskinfo where downloadstatus=0;"
sleep 3s
cd /www/Recoder/tools/VNSC/VNSC
/usr/local/python-2.7/bin/scrapy crawl hphim
sleep 10s
/usr/local/python-2.7/bin/scrapy crawl hphim_movie
sleep 10s
cd /www/Recoder/tools
/usr/bin/python2.7 download.py &
