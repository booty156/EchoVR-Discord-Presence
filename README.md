# Echo VR Discord Presence

EchoVR Discord Presence using EchoVR API.

## Getting started

If you haven't already, [install Python 3](https://www.python.org/downloads/) and [Pipenv](https://pipenv.readthedocs.io/en/latest/install/).

Now, to install all Python package dependencies, run:

```
pipenv install
```

## Usage

Download and run exe

[Releases](https://github.com/booty156/EchoVR-Discord-Presence/releases)

Open and edit these files:

		C:\Program Files\Oculus\Software\Manifests\ready-at-dawn-echo-arena.json
		
		C:\Program Files\Oculus\Software\Manifests\ready-at-dawn-echo-arena.json.mini
	
Edit the line:	"launchParameters": null,

And replace with:	"launchParameters": -http,

## Known Issues

Time and score may be delayed, as discord will update every 15 secs.

Cannot tell the difference between public matches and private matches. - Waiting on API update for this

Cannot tell the difference between Arena matches and Combat matches. - Waiting on API update for this

Being in a private on your own will show 0-0 for amount of players playing and scores.

## Road Map

Support for Combat, when released:

	Changes main image to combat
  
 	Displays 'PLaying Arena' For Echo Arena or 'Playing Combat' For Echo Combat
  
Private Support:

	Shows, 'Playing Private'. When in a private
  
 	Score and points, for when you're in a private, on your own.
  
Bug Fixes:

.dll file, to be put in EchoVR directioary and will start when EchoVR.exe is ran

  
