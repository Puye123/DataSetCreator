# DataSetCreator

## Description
This application can create learning data set using web camera.

## Demo
* Execution screen  
![demo](https://user-images.githubusercontent.com/32557553/44408415-4b801800-a59b-11e8-8166-395dc356069c.gif)

* The "dog" directory
![dogs](https://user-images.githubusercontent.com/32557553/44408544-8c782c80-a59b-11e8-9d59-177c3547a57c.png)  
Image file name is unique name based on time.

## Operation check environment
### Software
* Windows10 64-bit
* python 3.6.4 (Anaconda 5.1.4)
* opencv 3.4.1
* progressbar2
### Hardware 
* Web Camera (I use [ELECOM UCAM-C0220FBWH](http://www2.elecom.co.jp/multimedia/pc-camera/ucam-c0220fb/))

## Usage
```
python dataset_creator.py
```

### Options
* -h : show this help massage and exit
* -d : directory name (default = 'images')
* -n : number of pictures (default = 10)
* -s : size of pictures (default = 224)
* -f : image format <jpg | png | bmp>  (default = 'jpg')

## Licence
This software is released under the MIT License, see LICENSE.

## Authors
[Puye123](https://github.com/Puye123)
