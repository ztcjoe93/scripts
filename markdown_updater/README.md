# Automatic markdown updater
Convenience script to have **inotifywait** wait for changes in a set directory while using Linux's [_inotify_](https://en.wikipedia.org/wiki/Inotify) interface.  
When an event occurs, it's chained to the Python script which does a lookup for all ## headers and populate them into a declared _"table of content"_ header.  

## Running the script

Run the watcher shell script (preferably in a separate tmux session or in the background)
```shell
$ chmod +x watcher.sh
$ ./watcher.sh /path/to/python/script.py /path/to/watched/file
```
