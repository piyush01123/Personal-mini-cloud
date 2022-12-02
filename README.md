# Personal Mini Cloud

<p align="center">
<img src="https://user-images.githubusercontent.com/19518507/205280255-271c16f1-0cf4-4ee6-a564-1567dc15ae7d.png" height="200">
</p>


Share any file with just 1 `cURL` command:
```
curl -i -X POST -F file=@FILE_PATH  http://personal-mini-cloud.herokuapp.com
```
Replace `$FILE_PATH` with your required file path. This will return a URL like `http://personal-mini-cloud.herokuapp.com/cdn/$file` which you can share.

UPDATE: The application can also be accessed via browser at http://personal-mini-cloud.herokuapp.com/


