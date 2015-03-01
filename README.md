# /r/hapso.py

/r/hapso.py


Bill Garate (@billwritescode), Michael Garate (@mpgarate), and Katie Simon (@katiewsimon) built /r/hapso.py at the Automated Music Hackathon at Spotify in February. The program reads in JSON data from specified subreddits on reddit.com (/r/Music in the example) and transforms data points for use in a SuperCollider script that outputs sounds. The program uses data to specify instrument, pitch, duration, and volume.


### Requirements

Install [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/)

Install pip and portaudio
```sh
easy_install pip
brew install portaudio // or sudo apt-get install portaudio
```
