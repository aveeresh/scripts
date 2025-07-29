wget --save-cookies cookies.txt --post-data 'username=veeresha&password=mave8rick' http://www.virtualopensystems.com/logintrml/
wget --load-cookies cookies.txt http://www.virtualopensystems.com/PATH_TO_RESOURCE

curl -d 'username=veeresha&password=mave8rick' --dump-header headers http://www.virtualopensystems.com/logintrml/
curl -L -b headers http://www.virtualopensystems.com/PATH_TO_RESOURCE > resource_filename
